# Rock Paper Scissors AI Bot

A Python solution for the **Rock Paper Scissors** project from the [freeCodeCamp Machine Learning with Python](https://freecodecamp.org) certification.

## Overview
Standard random play in Rock Paper Scissors results in a 50% win rate. This project implements a `player` function in `RPS.py` using an **n-th order Markov Chain** (sequence pattern matching) to analyze an opponent's move history, predict their next play, and win at least **60% of matches** against four built-in bots (`quincy`, `abbey`, `kris`, and `mrugesh`).

## How It Works
1. **State Reset:** At the beginning of each 1,000-game match (`prev_play == ""`), the bot clears its memory lists and dictionaries so strategies do not bleed across different opponents.
2. **Sequence Tracking:** As rounds progress, the bot records the opponent's moves and logs every 5-move sequence (`n = 5`) into a frequency dictionary (`play_order`).
3. **Prediction:** Using the opponent's most recent 4 moves, the bot looks up which 5th move (`R`, `P`, or `S`) has historically followed that exact sequence most often.
4. **Counter-Play:** Once the next move is predicted, the bot plays the winning counter (`R` beats `S`, `P` beats `R`, `S` beats `P`).

## Project Files
* `RPS.py` – Contains the custom `player()` AI logic (the only file modified for the solution).
* `RPS_game.py` – Defines the game engine and the four opponent bots (`quincy`, `abbey`, `kris`, `mrugesh`).
* `main.py` – Runs test matches and triggers the automated unit test suite.
* `test_module.py` – Contains the official freeCodeCamp unit tests verifying a ≥60% win rate against every bot.

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com
   cd boilerplate-rock-paper-scissors
   ```
2. Replace the contents of `RPS.py` with the Markov Chain `player` implementation.
3. Run the matches and unit tests:
   ```bash
   python3 main.py
   ```
