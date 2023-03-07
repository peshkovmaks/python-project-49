from random import randint
from brain_games.engine import run_game

RULES = "What number is missing in the progression?"
# specify the rules of the game that we will show to the user

RAND_MIN_START = 1
RAND_MAX_START = 12
RAND_MIN_STEP = 1
RAND_MAX_STEP = 9
RAND_MIN_END = 6
RAND_MAX_END = 13


# specify random leght and step progression


def game_conditions():
    # specify the parameters for the game conditions and the correct answer
    progression_start = randint(RAND_MIN_START, RAND_MAX_START)
    progression_step = randint(RAND_MIN_STEP, RAND_MAX_STEP)
    progression_end = (progression_step + 1) * (randint(RAND_MIN_END, 
                                                        RAND_MAX_END))
    progression = list(range(progression_start, progression_end, 
                             progression_step))
    # specify hidden number and hidden symbol
    index_hidden_number = randint(0, len(progression) - 1)
    correct_answer = progression[index_hidden_number]
    progression[index_hidden_number] = ".."

    question = print(f'Question: {" ".join(map(str, progression))}')
    return question, correct_answer


# import game engine with game conditions and rules
def start_game():
    run_game(game_conditions, RULES)
