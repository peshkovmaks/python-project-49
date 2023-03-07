#!/usr/bin/env python3
from brain_games.games import progression
from brain_games import engine


def main():
    engine.run_game(progression.game_conditions, progression.RULES)


if __name__ == "__main__":
    main()
