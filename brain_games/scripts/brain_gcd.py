#!/usr/bin/env python3
from brain_games.games import gcd
from brain_games import engine


def main():
    engine.run_game(gcd.game_conditions, gcd.RULES)


if __name__ == "__main__":
    main()
