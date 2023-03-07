#!/usr/bin/env python3
from random import randint
from brain_games.engine import run_game

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
# specify the rules of the game that we will show to the user

RANDOM_NUMBER = randint(1, 99)
# random number limits


def game_conditions():
    # specify the parameters for the game conditions and the correct answer
    question = print(f"Question: {RANDOM_NUMBER}")
    correct_answer = 'yes' if RANDOM_NUMBER % 2 == 0 else 'no'
    return question, correct_answer


def start_game():
    # import game engine with game conditions and rules
    run_game(game_conditions, RULES)
