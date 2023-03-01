#!/usr/bin/env python3
from random import randint
import prompt
from brain_games.scripts.engine import compare_answer_question


def even_game():
    print("Welcome to Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello,  {name.lower().title()}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        random_number = randint(1, 99)
        if random_number % 2 == 0:
            correct_answer = "yes"
        else:
            correct_answer = "no"
        print(f"Question: {random_number}")
        user_answer = prompt.string("Your answer? ")
        compare_answer_question(user_answer, correct_answer)


def main():
    even_game()


if __name__ == "__main__":
    main()
