#!/usr/bin/env python3
from random import randint
from brain_games.engine import run_game

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
# specify the rules of the game that we will show to the user

RANDOM_NUMBER = randint(1, 99)
# random number limits


def check_prime(number):
    k = 0
    for i in range(2, number // 2 + 1):
        if RANDOM_NUMBER % i == 0:
            k = k + 1
    return 'yes' if k <= 0 else 'no'


def game_conditions():
    # specify the parameters for the game conditions and the correct answer
    question = print(f"Question: {RANDOM_NUMBER}")
    correct_answer = check_prime()
    return question, correct_answer


def start_game():
    # import game engine with game conditions and rules
    run_game(game_conditions, RULES)
