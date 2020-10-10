from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # A is either a knight or knave, but not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    # If a is a knight, then what it says is true (it says it is both a knight and a knave)
    Implication(AKnight, And(AKnight, AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # A is either a knight or knave, but not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    # B is either a knight or knave, but not both
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    # If a is a knight, then what it says is true, and vice-versa
    Biconditional(AKnight, And(AKnave, BKnave)),
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # A is either a knight or knave, but not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    # B is either a knight or knave, but not both
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    # If a is a knight, then what it says is true, and vice-versa
    Biconditional(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),

    # If b is a knight, then what it says is true, and vice-versa
    Biconditional(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
whatASaid = Or(AKnight, AKnave)
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # A is either a knight or knave, but not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    # B is either a knight or knave, but not both
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    # C is either a knight or knave, but not both
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),

    # If a is a knight, then what it says is true, and vice-versa
    Biconditional(AKnight, whatASaid),

    # If b is a knight, then what it says is true, and vice-versa
    Biconditional(BKnight, Symbol(whatASaid == AKnave)),
    Biconditional(BKnight, CKnave),

    # If c is a knight, then what it says is true, and vice-versa
    Biconditional(CKnight, AKnight),
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
