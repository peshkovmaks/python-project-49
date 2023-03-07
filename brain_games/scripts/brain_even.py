#!/usr/bin/env python3
from brain_games.games import even
from brain_games import engine


def main():
    engine.run_game(even.game_conditions, even.RULES)


if __name__ == "__main__":
    main()
