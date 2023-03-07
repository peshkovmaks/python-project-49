#!/usr/bin/env python3
from random import randint
from brain_games.engine import run_game

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
# specify the rules of the game that we will show to the user

RAND_MIN = 1
RAND_MAX = 99
# random number limits


def check_prime(number):
    k = 0
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            k = k + 1
    return True if k <= 0 else False


def game_conditions():
    random_number = randint(RAND_MIN, RAND_MAX)
    # specify the parameters for the game conditions and the correct answer
    question = print(f"Question: {random_number}")
    correct_answer = 'yes' if check_prime(random_number) else 'no'
    return question, correct_answer


def start_game():
    # import game engine with game conditions and rules
    run_game(game_conditions, RULES)
