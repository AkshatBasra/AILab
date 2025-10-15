import re
from itertools import product

def pl_true(sentence, model):
    """Evaluates a propositional logic sentence under a given model."""
    try:
        return eval(sentence, {}, model)
    except NameError:
        return False

def translate(sentence):
    """Convert logic symbols to Python syntax."""
    # Order matters! Handle longer symbols first
    sentence = sentence.replace('↔', '==')
    # sentence = sentence.replace('→', '<=')
    sentence = sentence.replace('¬', ' not ')
    sentence = sentence.replace('∧', ' and ')
    sentence = sentence.replace('∨', ' or ')
    
    # Replace implications properly: P → Q becomes (not P or Q)
    sentence = re.sub(r'([A-Z])\s*→\s*(not [A-Z]|[A-Z])', r'(not \1 or \2)', sentence)
    return sentence

def tt_entails(kb_list, alpha):
    """Truth table entailment: KB ⊨ α"""
    # Combine multiple KB statements
    kb = " and ".join(f"({translate(stmt)})" for stmt in kb_list)
    alpha = translate(alpha)

    # Collect all unique propositional symbols (A-Z)
    symbols = sorted(list(set(re.findall(r'[A-Z]', kb + alpha))))
    # print(f"Symbols found: {symbols}")

    # Iterate through all possible truth assignments
    for values in product([True, False], repeat=len(symbols)):
        model = dict(zip(symbols, values))
        if pl_true(kb, model):
            if not pl_true(alpha, model):
                # print(f"Counterexample: {model}")
                return False
    return True

if __name__ == "__main__":
    kb_list = [
        "(A ∨ B) ∧ (B ∨ ¬C)"
    ]
    alpha_formula = "A ∨ B"

    print("Knowledge Base (KB):")
    for stmt in kb_list:
        print(" ", stmt)
    print(f"\nQuery (α): {alpha_formula}\n")

    result = tt_entails(kb_list, alpha_formula)

    # print("\n------ RESULT ------")
    if result:
        print(f"The Knowledge Base entails the Query.")
        print(f"   KB ⊨ {alpha_formula}")
    else:
        print(f"The Knowledge Base does NOT entail the Query.")
        print(f"   KB ⊭ {alpha_formula}")