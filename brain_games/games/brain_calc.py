#!/usr/bin/env python3
from random import randint, choice
import prompt, operator


def calc_game():
    print("Welcome to Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello,  {name.lower().title()}!")
    print('What is the result of the expression?')
    i = 0
    while i < 3:
        random_number_first = randint(1, 99)
        random_number_second = randint(1, 99)
        list_operation = {'*': operator.mul, '-': operator.sub, '+': operator.add}
        random_operation = choice(list(list_operation))
        operation = list_operation[random_operation]
        expression = f'{random_number_first} {random_operation} {random_number_second}'
        correct_answer = operation(random_number_first, random_number_second)
        print(expression)
        user_answer = prompt.string("Your answer? ")
        if str(user_answer) == str(correct_answer):
            print("Correct!")
            i += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'. Let's try again, {name.lower().title()}!"
            )
            return
    print(f"Congratulations {name.lower().title()}!")



def main():
    calc_game()


if __name__ == "__main__":
     main()
