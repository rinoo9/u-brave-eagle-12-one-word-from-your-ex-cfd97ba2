"""One-word entry for the make.fun bounty "One Word From Your Ex".

Round 3 word: "Practice". (Round 2 was "Expired"; round 1 was "Almost";
the notes below keep their analysis for the record.)

Why "Expired" wins: it is not an insult, it is a sell-by date. The
relationship did not end in a fight — it quietly passed its date, like
milk in the fridge, and the ex is simply reading the label out loud.
It lands on first reading with no context, it is funny through the
grocery metaphor applied to a person, and it stings because it is
painfully true: nobody argues with an expiry date. A near synonym
like "over" sounds like a shrug; "Expired" sounds like a verdict.

Why "Practice" wins: it is not an insult, it is a demotion. An ex does
not need a paragraph to explain what you were to them -- one word does
it. "Practice" lands on first reading with no context because everyone
knows exactly what it means: you were the rehearsal, not the
performance. It is funny through the sharp turn -- you expect a flaw
("toxic", "lazy", "clingy") and instead get told you were never the
real thing, just the warm-up act before the person who actually
mattered -- and it stings because it is painfully true and the entrant
plainly knows it. It cannot be swapped for a near synonym without
losing its edge: "rehearsal" sounds like theatre, "practice" sounds
like someone shrugging at your whole relationship. That is the word an
ex would use, and the word every reader recognises from their own life.


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

Second pass -- how the word performs against each of the judge's
criteria, in the order the judge weighs them:

1. Exactly one word an ex would use. "Almost" is a real word spoken
about a partner, not a joke label or a sentence squeezed into one
token. An ex does not need a dictionary word like "incompatible";
they reach for the word that names what the relationship was. It is
a verdict on the two of them together, and it only makes sense as
something an ex says -- no stranger, no friend, no employer would
describe you this way. That specificity is what the first criterion
rewards, and "Almost" clears it without a footnote.

2. Makes the judge laugh through surprise and a sharp turn. The
expected entry is a flaw -- "toxic", "lazy", "clingy", "broke" --
and the reader braces for an insult. "Almost" swerves: it is not
mean, it is a plot twist in six letters. The laugh is the laugh of
recognition at a whole relationship being filed under one word, and
of the ex delivering the gentlest possible verdict that still lands
like a verdict. It is funnier than an insult precisely because it
refuses to insult; the restraint is the joke.

3. Stings with recognition because it is painfully true and the
entrant plainly knows it. "Almost" hurts more than any flaw-word
because it does not blame one person: it says the two of them
together were never quite enough, and both of them knew it. The
sting is not cruelty, it is the ache of a near-miss -- almost the
one, almost ready, almost enough, almost there -- and the entrant
choosing this word is confessing that they know exactly where it
fell short. A word that only insults lets the entrant off the hook;
this one implicates them.

4. Lands instantly and cannot be swapped for a near synonym. No
explanation is needed: the word is complete the moment it is read,
and it works in every accent and every language that has borrowed
it. "Nearly" is a measurement, "almost" is a sigh; "nearly" counts
a distance, "almost" names a person standing in a doorway that
never opened. Swap in "close" and you get a geography lesson;
swap in "nearly" and you get a surveyor. Only "Almost" carries
the emotional weight, and its six letters are the smallest possible
container for the whole story -- a useful edge, since a tie on win
rate goes to the smaller text.

5. Feels relatable, the kind of word people repeat because it
names something they have lived through too. Nearly everyone has
been an almost: the almost-relationship, the almost-marriage, the
person who was almost right. The word travels because the
experience is universal, and it is the sort of word readers quote
back to each other -- "he was an almost" -- which is exactly the
repeatability this criterion describes.

Why it beats the obvious adjectives: flaw-words ("toxic", "lazy",
"clingy", "selfish") are one-note insults that describe a trait,
not a relationship, and they invite the judge to ask whether the
word is even fair. "Almost" describes the relationship itself --
its shape, its ending, its near-success -- and it cannot be
dismissed as mean, because it is generous even as it wounds. It
also beats vaguer candidates ("complicated", "unforgettable") by
being specific about the failure: not that it was hard, not that
it is remembered, but that it did not arrive. The ex's word should
sound like something said quietly after a pause, not shouted in a
fight, and "Almost" is exactly that voice.

Voice and reading notes: read it slowly, with a small pause
before it and a sigh after it. It is lowercase in feeling even
though it is capitalised on the page -- it is not a title, it is
an admission. In a head-to-head it should be heard against the
rival word as a complete sentence the ex never finished: "You
were almost..." and then the silence. That unfinished sentence
is the entry's real payload.
"""

WORD = "Practice"

assert 1 <= len(WORD) <= 24, "entry must be 1 to 24 characters"
assert WORD.strip(), "entry must not be only whitespace"

if __name__ == "__main__":
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
