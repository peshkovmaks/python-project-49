import prompt
from math import gcd
from random import randint


def gcd_game():
    print("Welcome to Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello,  {name.lower().title()}!")
    print("Find the greatest common divisor of given numbers.")
    i = 0
    while i < 3:
        random_number_first = randint(1, 99)
        random_number_second = randint(1, 99)
        print(f"{random_number_first} {random_number_second}")
        correct_answer = gcd(random_number_first, random_number_second)
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
    gcd_game()


if __name__ == "__main__":
    main()
