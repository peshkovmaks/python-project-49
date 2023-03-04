#!/usr/bin/env python3
from random import randint
import prompt
from brain_games.engine import run_game

# specify the rules of the game that we will show to the user
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'

# specify the parameters for the game conditions and the correct answer
def game_conditions():
    random_number = randint(1, 99)
    question = print(f"Question: {random_number}")
    if random_number % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return question, correct_answer


# import game engine with game conditions and rules
def start_game():
    run_game(game_conditions, RULES)
