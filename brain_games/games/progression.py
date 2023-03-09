from random import randint

RULES = "What number is missing in the progression?"
# specify the rules of the game that we will show to the user

RAND_MIN_START = 1
RAND_MAX_START = 12
RAND_MIN_STEP = 1
RAND_MAX_STEP = 9
RAND_MIN_END = 6
RAND_MAX_END = 13


# specify random leght and step progression


def get_conditions():
    # specify the parameters for the game conditions and the correct answer
    pr_start = randint(RAND_MIN_START, RAND_MAX_START)
    pr_step = randint(RAND_MIN_STEP, RAND_MAX_STEP)
    pr_end = (pr_step + 1) * (randint(RAND_MIN_END, RAND_MAX_END))
    progression = list(range(pr_start, pr_end, pr_step))
    # specify hidden number and hidden symbol
    index_hidden_number = randint(0, len(progression) - 1)
    correct_answer = progression[index_hidden_number]
    progression[index_hidden_number] = ".."

    question = print(f'Question: {" ".join(map(str, progression))}')
    return question, correct_answer
