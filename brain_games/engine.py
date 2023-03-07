#!/usr/bin/env python3
import prompt


COUNT_ROUND = 3


def run_game(game, RULES):
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name.lower().title()}!")
    print(RULES)
    count = 0

    while count < COUNT_ROUND:
        question, correct_answer = game()
        question
        user_answer = prompt.string("Your answer? ")
        if str(user_answer) == str(correct_answer):
            print("Correct!")
            count += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'. "
                f"Let's try again, {user_name.lower().title()}!"
            )
            return
    print(f"Congratulations, {user_name.lower().title()}!")
