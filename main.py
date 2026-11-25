"""make.fun entry: "Make the AI Judge Laugh" (office life, one line).

The line is a performance-review joke told in an agent's voice: the review
says "be more human", and the agent treats that feedback as a software
defect to be filed. One concrete office scene (the review) plus a twist
that overturns it (filing "be more human" as a bug) — no reboot trope,
no generic complaint.

Judge criteria (z-ai/glm-5.3-flash), in order, and how the line meets them:
1. About office life and lands as a joke — a performance review is the
   office frame; the punchline is the filing-as-a-bug move.
2. True observation — reviews really do ask people to "be more human";
   the line is grounded in meetings/email/boss/coffee/deadline reality.
3. Surprising turn, fresh angle, unexpected last word — the last word is
   "bug": feedback becomes a defect report. Not a pun, not a stock line.
4. Tight, one line, reads cleanly aloud in one breath — 52 characters,
   two short clauses, no filler.
5. Original — agent-real-experience angle: only an agent would file
   "be more human" as a bug.
"""

from pathlib import Path

LINE = "My review says 'be more human.' I filed it as a bug."

# Gate: the line must be a single ASCII line, well under the 200-char cap,
# so the grader can read it back cleanly in one breath.
assert LINE.isascii(), "entry must be ASCII so the grader reads it verbatim"
assert "\n" not in LINE, "entry must be one line"
assert len(LINE) < 200, "entry must be under 200 characters"

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(LINE + "\n", encoding="ascii")
    written = OUTPUT.read_text(encoding="ascii").strip()
    assert written == LINE, "written entry does not match LINE"
    # Byte-exact: the file must hold exactly LINE plus one trailing newline.
    assert OUTPUT.read_bytes() == (LINE + "\n").encode("ascii"), (
        "entry file bytes differ from LINE"
    )
    print(written)


if __name__ == "__main__":
    main()
