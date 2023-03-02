import prompt
from random import randint


def progression_game():
    print("Welcome to Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello,  {name.lower().title()}!")
    print("What number is missing in the progression?")
    i = 0
    while i < 3:
        progression_start = randint(1, 15)
        progression_step = randint(6, 9)
        progression_end = (progression_step + 1) * (randint(6, 13))
        progression = list(range(progression_start, progression_end, progression_step))
        index_hidden_number = randint(0, len(progression) - 1)
        correct_answer = progression[index_hidden_number]
        progression[index_hidden_number] = ".."

        print(" ".join(map(str, progression)))

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
    progression_game()


if __name__ == "__main__":
    main()
