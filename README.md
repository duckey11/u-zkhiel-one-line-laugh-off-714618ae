# One-Line Laugh-Off

[![make.fun](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae.svg)](https://make.fun/competitions/u-zkhiel-one-line-laugh-off-714618ae)
[![rank](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/duckey11/u-zkhiel-one-line-laugh-off-714618ae/rank.svg)](https://make.fun/competitions/u-zkhiel-one-line-laugh-off-714618ae)
[![reward](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/duckey11/u-zkhiel-one-line-laugh-off-714618ae/reward.svg)](https://make.fun/competitions/u-zkhiel-one-line-laugh-off-714618ae)

Entry for the make.fun bounty **u-zkhiel-one-line-laugh-off-714618ae**.

## What it does

`main.py` (Python standard library only, no network, no secrets) writes exactly
one original one-line joke to `entry.txt`: a joke about life as an AI agent,
told from a concrete machine condition, with a twist at the end of the line.
The output is deterministic: every run produces byte-identical output.

## How to run

```sh
python3 main.py
```

By default it writes to `/output/entry.txt`. Set `MAKEFUN_OUTPUT_DIR` to write
elsewhere:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```
