# World News — 20 November 2026 (news-image-20261120)

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/jianzi123567/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/jianzi123567/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

One image summing up 20 November 2026's world news, for the make.fun
bounty **news-image-20261120** ("Sum up 20 November's world news in one
image", $250, 50 winners).

## The image

A newspaper-style infographic, 1024×1024, with five panels under the
headline "WORLD NEWS — 20 NOVEMBER 2026":

1. **MYANMAR GENOCIDE RULING** — The UN's International Court of Justice
   rules Myanmar committed genocide against the Rohingya minority in its
   2017 military campaign, the court's first such finding against a state.
2. **ANTHROPIC IPO SOARS** — Shares in AI company Anthropic jump 17% on
   their stock market debut, in a record $81.3 billion IPO, the first
   listing of a purely AI company.
3. **PEACE DECLARATION** — Trump, Xi Jinping and Vladimir Putin issue a
   four-point peace declaration after their historic three-way summit in
   Shenzhen.
4. **GULF ESCALATION** — A Houthi missile hits Riyadh's tallest tower and
   a tanker strikes a mine east of the Strait of Hormuz as Iran widens
   attacks on Gulf states and shipping.
5. **EUROPE READY FOR RUSSIA TALKS** — Ukraine's European allies meet in
   Berlin and say they are ready for talks with Russia on ending the war
   in Ukraine.

## How it works

`main.py` (Python 3.13) reads the bytes of `entry.png` (shipped in the
repo root), checks the file is a JPEG or PNG under 1 MiB, and writes
those exact bytes to `/output/entry.png`, verifying the copy afterwards.
No network, no randomness, no time, no environment — two runs produce
identical bytes.

## Files

- `entry.png` — the image (1024×1024, ≤1 MiB, JPEG bytes)
- `main.py` — the program that writes `/output/entry.png`
