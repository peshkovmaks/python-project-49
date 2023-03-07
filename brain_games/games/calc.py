#!/usr/bin/env python3
from random import randint, choice
import operator
from brain_games.engine import run_game

RULES = "What is the result of the expression?"
# specify the rules of the game that we will show to the user

RANDOM_NUMBER_FIRST = randint(1, 99)
RANDOM_NUMBER_SECOND = randint(1, 99)
# limits of random numbers


def game_conditions():
    # specify the parameters for the game conditions and the correct answer
    # get random math operator
    list_operation = {"*": operator.mul, "-": operator.sub, "+": operator.add}
    random_operation = choice(list(list_operation))
    operation = list_operation[random_operation]
    question = print(
        f"Question: {RANDOM_NUMBER_FIRST}"
        f" {random_operation} {RANDOM_NUMBER_SECOND}"
    )

    correct_answer = operation(RANDOM_NUMBER_FIRST, RANDOM_NUMBER_SECOND)

    return question, correct_answer


def start_game():
    # import game engine with game conditions and rules
    run_game(game_conditions, RULES)
