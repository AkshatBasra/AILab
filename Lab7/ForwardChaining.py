import re

def is_variable(term):
    return term[0].islower()

def parse_predicate(expr):
    match = re.match(r"([A-Za-z_][A-Za-z0-9_]*)\(([^)]*)\)", expr)
    if match:
        pred, args = match.groups()
        args = [a.strip() for a in args.split(",")]
        return pred, args
    else:
        return expr, []

def unify(x, y, subs=None):
    if subs is None:
        subs = {}
    if x == y:
        return subs
    if isinstance(x, list) and isinstance(y, list):
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
    if var in subs:
        return unify(subs[var], x, subs)
    elif x in subs:
        return unify(var, subs[x], subs)
    else:
        new_subs = subs.copy()
        new_subs[var] = x
        return new_subs

def substitute(expr, subs):
    pred, args = parse_predicate(expr)
    new_args = [subs.get(a, a) for a in args]
    return f"{pred}({','.join(new_args)})"

def forward_chain(kb_rules, facts, query):
    inferred = set(facts)
    while True:
        new_inferred = set()
        for (premise, conclusion) in kb_rules:
            pred_p, args_p = parse_predicate(premise)
            pred_c, args_c = parse_predicate(conclusion)
            for fact in inferred:
                pred_f, args_f = parse_predicate(fact)
                if pred_p == pred_f:
                    subs = unify(args_p, args_f)
                    if subs is not None:
                        new_fact = substitute(conclusion, subs)
                        if new_fact not in inferred:
                            new_inferred.add(new_fact)
                            if new_fact == query:
                                return True
        if not new_inferred:
            return False
        inferred |= new_inferred

rules = [
    ("P(x)", "Q(x)")
]
facts = [
    "P(a)"
]
query = "Q(a)"

print("Entailed?", forward_chain(rules, facts, query))
