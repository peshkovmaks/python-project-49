#!/usr/bin/env python3
from random import randint
import prompt
from brain_games.engine import run_game

# specify the rules of the game that we will show to the user
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'

# specify the parameters for the game conditions and the correct answer
def game_conditions():
    random_number = randint(1, 99)
    question = print(f"Question: {random_number}")
    k = 0
    for i in range(2, random_number // 2 + 1):
        if random_number % i == 0:
            k = k + 1
    if k <= 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return question, correct_answer


# import game engine with game conditions and rules
def start_game():
    run_game(game_conditions, RULES)
