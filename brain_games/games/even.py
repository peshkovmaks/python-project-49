#!/usr/bin/env python3
from random import randint
from brain_games.engine import run_game

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
# specify the rules of the game that we will show to the user

RAND_MIN = 1
RAND_MAX = 99
# random number limits


def game_conditions():
    # specify the parameters for the game conditions and the correct answer
    random_number = randint(RAND_MIN, RAND_MAX)
    question = print(f"Question: {random_number}")
    correct_answer = 'yes' if random_number % 2 == 0 else 'no'
    return question, correct_answer


def start_game():
    # import game engine with game conditions and rules
    run_game(game_conditions, RULES)
