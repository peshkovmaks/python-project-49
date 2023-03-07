#!/usr/bin/env python3
from math import gcd
from random import randint
from brain_games.engine import run_game

RULES = "Find the greatest common divisor of given numbers."
# specify the rules of the game that we will show to the user


RAND_MIN = 1
RAND_MAX = 99
# random number limits


def game_conditions():
    # specify the parameters for the game conditions and the correct answer
    random_number_first = randint(RAND_MIN, RAND_MAX)
    random_number_second = randint(RAND_MIN, RAND_MAX)
    question = print(f"Question: {random_number_first} {random_number_second}")
    correct_answer = gcd(random_number_first, random_number_second)
    return question, correct_answer


# import game engine with game conditions and rules
def start_game():
    run_game(game_conditions, RULES)
