#!/usr/bin/env python3
from random import randint
import prompt


def prime_game():
    print("Welcome to Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello,  {name.lower().title()}!")
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    index = 0
    while index < 3:
        random_number = randint(1, 99)
        k = 0
        for i in range(2, random_number // 2 + 1):
            if random_number % i == 0:
                k = k + 1
        if k <= 0:
            correct_answer = "yes"
        else:
            correct_answer = "no"
        print(f"Question: {random_number}")

        user_answer = prompt.string("Your answer? ")

        if str(user_answer) == str(correct_answer):
            print("Correct!")
            index += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'. Let's try again, {name.lower().title()}!"
            )
            return
    print(f"Congratulations {name.lower().title()}!")


def main():
    prime_game()


if __name__ == "__main__":
    main()
