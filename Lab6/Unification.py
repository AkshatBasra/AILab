import re

def parse(expr):
    tokens = re.findall(r"[A-Za-z_][A-Za-z0-9_]*|[(),]", expr)

    def parse_rec():
        token = tokens.pop(0)
        if tokens and tokens[0] == '(':
            tokens.pop(0)
            args = []
            while tokens[0] != ')':
                args.append(parse_rec())
                if tokens[0] == ',':
                    tokens.pop(0)
            tokens.pop(0)
            return (token, args)
        return token

    return parse_rec()

isvar = lambda x: isinstance(x, str) and x[0].islower()

def occurs(v, x, s):
    if v == x: return True
    if isvar(x) and x in s: return occurs(v, s[x], s)
    if isinstance(x, tuple): return any(occurs(v, a, s) for a in x[1])
    return False

def unify(x, y, s=None):
    s = {} if s is None else s

    if s == "fail": return "fail"
    if x == y: return s

    if isinstance(x, list) and isinstance(y, list) and len(x) == len(y):
        for a, b in zip(x, y):
            s = unify(a, b, s)
            if s == "fail": return "fail"
        return s

    if isvar(x): return unify_var(x, y, s)
    if isvar(y): return unify_var(y, x, s)

    if isinstance(x, tuple) and isinstance(y, tuple):
        if x[0] != y[0] or len(x[1]) != len(y[1]): return "fail"
        return unify(x[1], y[1], s)

    return "fail"

def unify_var(v, x, s):
    if v in s: return unify(s[v], x, s)
    if isvar(x) and x in s: return unify(v, s[x], s)
    if occurs(v, x, s): return "fail"
    s[v] = x
    return s

def to_str(e):
    return e if isinstance(e, str) else f"{e[0]}({', '.join(to_str(a) for a in e[1])})"

def show(s):
    if s == "fail":
        print("Unification failed.")
    else:
        for v, x in s.items():
            print(f"{v} = {to_str(x)}")


expr1 = "P(f(x), g(y), y)"
expr2 = "P(f(g(z)), g(f(a)), f(a))"

X = parse(expr1)
Y = parse(expr2)

subs = unify(X, Y)
show(subs)
