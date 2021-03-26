"""
Name: Kerry Chow[A01245034]
Name: Tomo Kaneko[A01250261]
Date:
"""
import itertools
import random
import time
import sys
from time import sleep


def RED():
    """Return ANSI escape for text color red
    """
    return "\033[31m"


def BLUE():
    """Return ANSI escape for text color blue
    """
    return "\033[34m"


def GREEN():
    """Return ANSI escape for text color green
    """
    return "\033[32m"


def YELLOW():
    """Return ANSI escape for text color yellow
    """
    return "\033[33m"


def CYAN():
    """Return ANSI escape for text color cyan
    """
    return "\033[36m"


def END():
    """Return ANSI escape to terminate previous ANSI escape codes
    """
    return "\033[0m"


def BOLD():
    """Return ANSI escape for bold text
    """
    return "\033[01m"


def UNDERLINE():
    """Return ANSI escape for text underline
    """
    return "\033[04m"


def BLINK():
    """Return ANSI escape for text blink
    """
    return "\033[05m"


def typing_effect(words):
    """Print stdout pretty

    :param words: a string
    :precondition: words must be type string
    :postcondition: print stdout with style
    :return: None
    """
    for char in words:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()

def PLAYER_START_MIN_DAMAGE():
    return 5


def PLAYER_START_DAMAGE():
    return 20


def PLAYER_START_HP():
    return 20


def PLAYER_START_EXPERIENCE():
    return 0


def PLAYER_LEVEL():
    return 1


def PLAYER_START_HIT_RATE():
    return 75  # this means 75% chance of hit


def PLAYER_HIT_RATE_INCREASE():
    return 5


def PLAYER_MIN_DAMAGE_INCREASE():
    return 2


def PLAYER_MAX_DAMAGE_INCREASE():
    return 5


def PLAYER_HP_INCREASE():
    return 10


def PLAYER_START_LOCATION():
    return [0, 0]


def PLAYER_EXPERIENCE_GAIN():
    return 5


def PLAYER_EXPERIENCE_LEVEL2():
    return 20


def PLAYER_EXPERIENCE_LEVEL3():
    return 40


def PLAYER_HP_HEAL():
    return 4


def PLAYER_UNSUCESSFUL_FLEE_RATE():
    return 20


def MONSTER_MIN_DAMAGE():
    return 1


def MONSTER_MAX_DAMAGE():
    return 15


def MONSTER_MIN_HP():
    return 5


def MONSTER_MAX_HP():
    return 20


def MONSTER_MIN_HIT_RATE():
    return 30


def MONSTER_MAX_HIT_RATE():
    return 70


def MONSTER_SPAWN_RATE():
    return 20


def BOSS_LOCATION():
    return [24, 24]


def BOSS_HP():
    return 100


def BOSS_MIN_DAMAGE():
    return 5


def BOSS_MAX_DAMAGE():
    return 15


def BOSS_HIT_RATE():
    return 80


def MAX_HIT_RATE():
    return 100


def ICON():
    return "🧙"  # for now


def BOSS_ICON():
    return "👹"


def BOARD_WIDTH():
    return 25


def BOARD_HEIGHT():
    return 25


def make_map():
    """Make board for game

    :param:
    :precondition:
    :postcondition: create list of tuple to represent board
    :return: a dictionary to represetn game board
    """
    return [(y, x) for y in range(BOARD_HEIGHT()) for x in range(BOARD_WIDTH())]


def print_map(board, player):
    """Print game board to user

    :param board: a dictionary
    :param player: a dictionary
    :precondition: board must be a dictionary representing game board
    :precondition: player must be a dictionary representing player
    :postcondition: print game board to the user
    :postcondition: print player icon on board corresponding to player location
    :postcondition: print boss icon on board corresponding to boss location
    :return: None
    """
    key_counter = 0
    for x_axis in range(25):
        for y_axis in range(25):
            if board[key_counter] == tuple(player["location"]):
                print(BLINK() + "🧙" + END() + " ", end="")
            elif board[key_counter] == tuple(BOSS_LOCATION()):
                print("👹", end="")
            else:
                print("[ ]", end="")
            key_counter += 1
        print()


def get_player_move():
    """Get players direction

    :postcondition: return player_direction if valid else print Invalid message
    :return: a string representing players moving direction
    """
    print("\nInstructions: \n 0: Up \n 1: Down \n 2: Left\n 3: Right\n")
    valid_user_input = ["0", "1", "2", "3", "q", "Q"]
    while True:
        player_direction = input("Which direction will you go? ")
        if player_direction in valid_user_input:
            return player_direction
        else:
            print("\nInvalid Input\nPlease Try Again\n")


def player_destination(direction, player):
    """Create players next destination

    :param direction: a string
    :param player: a dictionary
    :precondition: direction must be a string number of 0, 1, 2, or 3
    :precondition: player must be a dictionary representing player
    :postcondition: create a tuple of players next destination on game board
    :return: a tuple representing location on game board
    """
    new_location = list(player["location"])
    if direction == "0":
        new_location[0] -= 1
    elif direction == "1":
        new_location[0] += 1
    elif direction == "2":
        new_location[1] -= 1
    elif direction == "3":
        new_location[1] += 1
    return tuple(new_location)


def validate_move(new_location, board):
    """Validate the destination the player wants to go

    :param new_location: a tuple
    :param board: a list of tuples
    :precondition: new_location must be a tuple of coordinates
    :precondition: board must be a list of tuples representing game board
    :postcondition: check if new_location is within board
    :return: True if new_location is in board else False
    """
    if new_location in board:
        return True
    else:
        return False


def move_player(direction, character):
    """Move the player on game board

    :param direction: a string
    :param character: a dictionary
    :precondition: direction must be a string number of 0, 1, 2, 3
    :precondition: character must be a dictionary representing player
    :postcondition: modify character['location'] value according to direction
    :return: None
    """
    if direction == "0":
        character["location"][0] -= 1
    elif direction == "1":
        character["location"][0] += 1
    elif direction == "2":
        character["location"][1] -= 1
    elif direction == "3":
        character["location"][1] += 1


def flee(player):
    """Flee from foe

    :param player: a dictionary
    :precondition: player must be a dictionary representing game player
    :postcondition: take damage with 20% chance and print message
                    else print message
    :return: None
    """
    if random.randint(1, 100) <= 20:
        flee_damage = random.randint(0, 15)
        player["HP"] -= flee_damage
        print(f"You fled but took a stab to the back {flee_damage}")
    else:
        print("You fled successfully!")


def heal(player):
    pass


def class_description():
    print("\nClasses\n\n"
          "{}0{} {}Sorcerer{}:\nSorcerers uses magic to attack."
          "\nTheir damage is amplified, but not the most accurate!\n\n"
          "{}1{} {}Thief{}:\nThieves lurk through the shadows with striking with deadly accuracy."
          "\nTheir accuracy is near-perfect, but lack the strength to damage!\n\n"
          "{}2{} {}Amazon{}:\nAmazons specialize in archery, swordplay, and a bit of magic."
          "\nAmazon's are the most well-balanced class!\n\n"
          "{}3{} {}Fighter{}:\nFighters have incredible yet, uncontrollable strength. "
          "\nTheir uncontrollable strength can easily dissipate weak monsters!\n"
          .format(RED(), END(), UNDERLINE(), END(), RED(), END(), UNDERLINE(), END(), RED(), END(), UNDERLINE(), END(),
                  RED(), END(), UNDERLINE(), END()))


def class_stats(player):  # amazon no stat changes
    if player["class"] == "sorcerer":
        player["max_damage"] += 10  # low chance of hit high damage
        player["min_damage"] += 5
        player["hit_rate"] -= 15
    elif player["class"] == "thief":
        player["max_damage"] -= 5  # high hit rate low damage
        player["min_damage"] += 2
        player["hit_rate"] += 10
    elif player["class"] == "fighter":
        player["max_damage"] += 10  # high damage low chance of deadly hit
        player["min_damage"] -= 2
    elif player["class"] == "hidden lord":
        player["max_damage"] += 80
        player["HP"] += 50
        player["max_HP"] += 50
        player["hit_rate"] += 25


def class_choice(player_class):
    class_list = enumerate(["sorcerer", "thief", "amazon", "fighter"])
    for jobs in class_list:
        if player_class == str(jobs[0]):  # int must be converted to str to prevent TypeError
            return jobs[1]
    else:
        return "hidden lord"


def make_player():
    """Create player

    :postcondition: create a dictionary representing game player
    :return: a dictionary representing player
    """
    name = input("What's your name, explorer?: ")
    class_description()
    player_class = input("What class will you choose? Enter number for class: ")
    player = {"name": name,
              "master_class": class_choice(player_class),
              "level": PLAYER_LEVEL(),
              "HP": PLAYER_START_HP(),
              "max_HP": PLAYER_START_HP(),
              "hit_rate": PLAYER_START_HIT_RATE(),
              "XP": PLAYER_START_EXPERIENCE(),
              "min_damage": PLAYER_START_MIN_DAMAGE(),
              "max_damage": PLAYER_START_DAMAGE(),
              "location": PLAYER_START_LOCATION()}
    class_stats(player)
    return player


def game():
    """Play game
    """
    player = make_player()
    board = make_map()
    achieve_goal = False
    print_map(board, player)


def main():
    """Execute game
    """
    game()


if __name__ == "__main__":
    main()
