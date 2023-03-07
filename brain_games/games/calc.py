#!/usr/bin/env python3
from random import randint, choice
import operator
from brain_games.engine import run_game

RULES = "What is the result of the expression?"
# specify the rules of the game that we will show to the user

RAND_MIN = 1
RAND_MAX = 99
# random number limits


def game_conditions():
    # specify the parameters for the game conditions and the correct answer
    # get random math operator
    random_number_first = randint(RAND_MIN, RAND_MAX)
    random_number_second = randint(RAND_MIN, RAND_MAX)
    list_operation = {"*": operator.mul, "-": operator.sub, "+": operator.add}
    random_operation = choice(list(list_operation))
    operation = list_operation[random_operation]
    question = print(
        f"Question: {random_number_first}"
        f" {random_operation} {random_number_second}"
    )

    correct_answer = operation(random_number_first, random_number_second)

    return question, correct_answer


def start_game():
    # import game engine with game conditions and rules
    run_game(game_conditions, RULES)
