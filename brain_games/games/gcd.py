#!/usr/bin/env python3
from math import gcd
from random import randint
from brain_games.engine import run_game

RULES = "Find the greatest common divisor of given numbers."
# specify the rules of the game that we will show to the user

RANDOM_NUMBER_FIRST = randint(1, 99)
RANDOM_NUMBER_SECOND = randint(1, 99)
# limits of random numbers


def game_conditions():
    # specify the parameters for the game conditions and the correct answer
    question = print(f"Question: {RANDOM_NUMBER_FIRST} {RANDOM_NUMBER_SECOND}")
    correct_answer = gcd(RANDOM_NUMBER_FIRST, RANDOM_NUMBER_SECOND)
    return question, correct_answer


# import game engine with game conditions and rules
def start_game():
    run_game(game_conditions, RULES)
