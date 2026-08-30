# ipai — working instructions

Loaded automatically by any Claude Code session opened in this folder.

> **This file starts nearly empty and that is correct.** It is not documentation.
> It is the place where things that cost an evening get written down so they cost
> an evening once. Add to it when something surprises you, not when you set up.
> `radi/CLAUDE.md` reached 383 lines and `arena/CLAUDE.md` reached 1,307 that way —
> neither was written up front.

## What this repo is

**A CHAMY·XYZ broadside on AI and intellectual property**, made as a resource for
attendees of the *AI + Intellectual Property* panel he moderated for Oolite Arts'
Skills Program, April 2026.

**The line worth remembering about how this came about**, because it decides who owns
it: the Incubator asked him to *moderate the panel*. That was the assignment. Making
a digital broadside as a resource for attendees was **entirely his own idea and his
own work**, and was never required. The deliverable requested and the thing made are
different objects.

Published rather than proprietary — its value is reputational and it should
circulate. See LICENSE.

Remote: `git@github.com:2urn/ipai.git`

## Who you're working with

An artist, teacher and designer — real front-end experience in his past, not a
professional programmer. He dictates his messages, so expect transcription
artefacts and read for intent.

**He is observant and his bug reports are accurate.** When he says something is not
working, it is not. Do not close a report as a false alarm; check three places and
report what you checked rather than contradicting him.

**He works in the Claude Mac app, not a terminal.** An answer that resolves to
"open a terminal and type this" is a failure of the tooling.

**Lead with the headline.** He skims. Put the decision-changing fact in line one.

**Only ask when a question is both expensive AND unpredictable** — both, not either.
Cheap or predictable calls get made, then reported. When you do ask, ask as a
multiple-choice question; he is often driving.

**Separate what was verified from what was inferred.** Never blend them into one
confident number.

## Conventions

- **One folder per thing, named after the thing.**
- **Re-runnable scripts in `Modules/`**, not remembered steps. If a task needs
  repeated judgement, build the instrument before the feature — it nearly always
  pays back in the same session.
- **Name the purpose, not the mechanism.** A control named after how it works makes
  the tool feel arbitrary.
- **Say what is wrong AND how to fix it.** "Short by 3 — raise a capacity or drop
  the floor" beats "invalid configuration".
- **State the arithmetic impossibility before the output**, rather than producing a
  result with quiet holes in it.

## Commit and push, and write the commit like it will be read

Commit after each working change and push. Git is the safety net; a mis-save is a
`git checkout` away.

**`HISTORY.md` is generated from the log** by `python3 Modules/history.py`, so the
commit messages ARE this project's written history. That is deliberate: a hand-kept
changelog is a second record of the same events and the two diverge the first time
somebody is in a hurry.

So write the message with the reasoning in it — what broke, what was *measured*,
why a decision went the way it did, and what was ruled out. A terse commit makes a
poorer history, which is the intended pressure.

## Hard-won rules

### CREDIT WHAT WAS NOT HIS, IN NOTICE, NOT IN SILENCE

The panel involved two practising IP attorneys, and the legal-landscape material
draws on work by **Somara Jacques**. Those contributions belong to their authors.
`NOTICE` acknowledges them rather than absorbing them, and `LICENSE` does not claim
them.

Substantial quotation of a named person is also a courtesy question before it is a
legal one. Ask before publishing anything that puts words in their mouth.

### THIS IS A RESOURCE PEOPLE CITE, SO IT HAS TO STAY WHERE THEY LEFT IT

The no-derivatives condition is not defensiveness. A page somebody cited in a grant
application or a licensing negotiation has to still say what it said. Correct errors
and date the correction; do not silently rewrite.
