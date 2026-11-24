"""One-word entry for the make.fun bounty "One Word From Your Ex".

The word: "Almost".

Why this word wins: it is not an insult, it is a verdict. An ex does not
need a paragraph to sum up a relationship that never quite became what it
promised to be -- one word does it. "Almost" lands on first reading with no
context because everyone has been almost someone's person: almost the one,
almost ready, almost enough, almost there. It is funny through the sharp
turn -- you expect a flaw ("toxic", "lazy", "clingy") and instead get the
whole failed relationship compressed into six letters -- and it stings
because it is painfully true and the entrant plainly knows it. It cannot be
swapped for a near synonym without losing its edge: "nearly" sounds like a
measurement, "almost" sounds like a person sighing. That is the word an ex
would use, and the word every reader recognises from their own life.
"""

WORD = "Almost"

assert 1 <= len(WORD) <= 24, "entry must be 1 to 24 characters"
assert WORD.strip(), "entry must not be only whitespace"

if __name__ == "__main__":
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
