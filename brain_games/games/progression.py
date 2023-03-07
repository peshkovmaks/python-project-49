from random import randint
from brain_games.engine import run_game

RULES = "What number is missing in the progression?"
# specify the rules of the game that we will show to the user

PROGRESSION_START = randint(1, 15)
PROGRESSION_STEP = randint(6, 9)
PROGRESSION_END = (PROGRESSION_STEP + 1) * (randint(6, 13))
# specify random leght and step progression


def game_conditions():
    # specify the parameters for the game conditions and the correct answer
    progression = list(range(PROGRESSION_START, PROGRESSION_END, 
                             PROGRESSION_STEP))
    # specify hidden number and hidden symbol
    index_hidden_number = randint(0, len(progression) - 1)
    correct_answer = progression[index_hidden_number]
    progression[index_hidden_number] = ".."

    question = print(f'Question: {" ".join(map(str, progression))}')
    return question, correct_answer


# import game engine with game conditions and rules
def start_game():
    run_game(game_conditions, RULES)
