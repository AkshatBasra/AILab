import itertools
import re

def is_variable(term):
    return isinstance(term, str) and term[0].islower()

def parse_literal(literal):
    negated = literal.startswith("¬")
    if negated:
        literal = literal[1:]
    match = re.match(r"([A-Za-z_][A-Za-z0-9_]*)\(([^)]*)\)", literal)
    if match:
        pred, args = match.groups()
        args = [a.strip() for a in args.split(",")] if args.strip() else []
        return negated, pred, args
    else:
        return negated, literal, []

def unify(x, y, subs):
    if subs is None:
        return None
    elif x == y:
        return subs
    elif isinstance(x, list) and isinstance(y, list):
        if len(x) != len(y):
            return None
        for xi, yi in zip(x, y):
            subs = unify(xi, yi, subs)
            if subs is None:
                return None
        return subs
    elif is_variable(x):
        return unify_var(x, y, subs)
    elif is_variable(y):
        return unify_var(y, x, subs)
    else:
        return None

def unify_var(var, x, subs):
    if not isinstance(var, str):
        return None
    if var in subs:
        return unify(subs[var], x, subs)
    elif isinstance(x, str) and x in subs:
        return unify(var, subs[x], subs)
    elif occurs_check(var, x, subs):
        return None
    else:
        new_subs = subs.copy()
        new_subs[var] = x
        return new_subs

def occurs_check(var, x, subs):
    if var == x:
        return True
    elif isinstance(x, list):
        return any(occurs_check(var, xi, subs) for xi in x)
    elif isinstance(x, str) and x in subs:
        return occurs_check(var, subs[x], subs)
    return False

def substitute(literal, subs):
    neg, pred, args = parse_literal(literal)
    new_args = [subs.get(a, a) for a in args]
    return ("¬" if neg else "") + f"{pred}({','.join(new_args)})" if args else literal

def resolve(ci, cj):
    resolvents = []
    for li in ci:
        for lj in cj:
            neg_i, pred_i, args_i = parse_literal(li)
            neg_j, pred_j, args_j = parse_literal(lj)
            if pred_i == pred_j and neg_i != neg_j:
                subs = unify(args_i, args_j, {})
                if subs is not None:
                    new_clause = set(substitute(l, subs) for l in (ci + cj))
                    new_clause.discard(substitute(li, subs))
                    new_clause.discard(substitute(lj, subs))
                    resolvents.append(tuple(sorted(new_clause)))
    return resolvents

def resolution(kb, query):
    clauses = kb + [(f"¬{query}",)]
    seen = set()
    while True:
        new = set()
        for (ci, cj) in itertools.combinations(clauses, 2):
            for resolvent in resolve(list(ci), list(cj)):
                if not resolvent:
                    return True
                new.add(resolvent)
        if new.issubset(set(clauses)) or new.issubset(seen):
            return False
        clauses += list(new)
        seen |= new


KB = [
    ("¬P(x)", "Q(x)"),
    ("P(a)",)
]
query = "Q(a)"

print("Entailed?", resolution(KB, query))
