import prompt
from random import randint
from brain_games.engine import run_game

# specify the rules of the game that we will show to the user
RULES = "Find the greatest common divisor of given numbers."

# specify the parameters for the game conditions and the correct answer
def game_conditions():
    # specify random leght and step progression
    progression_start = randint(1, 15)
    progression_step = randint(6, 9)
    progression_end = (progression_step + 1) * (randint(6, 13))
    progression = list(range(progression_start, progression_end, progression_step))
    # specify hidden number and hidden symbol
    index_hidden_number = randint(0, len(progression) - 1)
    correct_answer = progression[index_hidden_number]
    progression[index_hidden_number] = ".."

    question = print(f'Question: {" ".join(map(str, progression))}')
    return question, correct_answer


# import game engine with game conditions and rules
def start_game():
    run_game(game_conditions, RULES)
