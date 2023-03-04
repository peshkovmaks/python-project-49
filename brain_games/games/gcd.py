#!/usr/bin/env python3
from math import gcd
from random import randint
import prompt
from brain_games.engine import run_game

# specify the rules of the game that we will show to the user
RULES = "Find the greatest common divisor of given numbers."

# specify the parameters for the game conditions and the correct answer
def game_conditions():
    random_number_first = randint(1, 99)
    random_number_second = randint(1, 99)
    question = print(f"Question: {random_number_first} {random_number_second}")
    correct_answer = gcd(random_number_first, random_number_second)
    return question, correct_answer


# import game engine with game conditions and rules
def start_game():
    run_game(game_conditions, RULES)
