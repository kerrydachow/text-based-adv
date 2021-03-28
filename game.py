"""
Name: Kerry Chow[A01245034]
Name: Tomo Kaneko[A01250261]
Date:
"""
import itertools
import random
import sys
from time import sleep
from doctest import testmod


def RED():
    """Return ANSI escape code for text color red

    :return: ANSI escape code for text color red
    """
    return "\033[31m"


def BLUE():
    """Return ANSI escape code for text color blue

    :return: ANSI escape code for text color blue
    """
    return "\033[34m"


def GREEN():
    """Return ANSI escape code for text color green

    :return: ANSI escape code for text color green
    """
    return "\033[32m"


def YELLOW():
    """Return ANSI escape code for text color yellow

    :return: ANSI escape code for text color yellow
    """
    return "\033[33m"


def PURPLE():
    """Return ANSI escape code for text color purple.

    :return: ANSI escape code for text color purple
    """
    return "\033[35m"


def END():
    """Return ANSI escape code to terminate previous ANSI escape codes.

    :return: ANSI escape code to terminate previous ANSI escape codes
    """
    return "\033[0m"


def BOLD():
    """Return ANSI escape code for bold text.

    :return: ANSI escape code for bold text
    """
    return "\033[01m"


def UNDERLINE():
    """ANSI escape code for text underline.

    :return: ANSI escape code for underlined text
    """
    return "\033[04m"


def BLINK():
    """Return ANSI escape code for text blink.

    :return: ANSI escape code for blinking text
    """
    return "\033[05m"


def PLAYER_START_MIN_DAMAGE():
    """Return the starting minimum damage of a player.

    :return: the starting minimum damage of a player as an integer
    """
    return 5


def PLAYER_START_MAX_DAMAGE():
    """Return the starting maximum damage of a player.

    :return: the starting maximum damage of a player as an integer
    """
    return 20


def PLAYER_START_HP():
    """Return the starting health points of a player.

    :return: the starting health points of a player as an integer
    """
    return 30


def PLAYER_START_EXPERIENCE():
    """Return the starting experience points of a player.

    :return: the starting experience points of a player as an integer
    """
    return 0


def PLAYER_LEVEL():
    """Return the starting level of a player.

    :return: the starting level of a player as an integer
    """
    return 1


def PLAYER_START_HIT_RATE():
    """Return the starting hit rate of a player.

    :return: the starting hit rate of a player as an integer
    """
    return 75  # this means 75% chance of hit


def LEVEL_UP_HIT_RATE_INCREASE():
    """Return the hit rate increase upon level up.

    :return: the hit rate increase upon level up as an integer
    """
    return 5


def LEVEL_UP_MIN_DAMAGE_INCREASE():
    """Return the min_damage increase upon level up.

    :return: the min_damage increase upon level up as an integer
    """
    return 2


def LEVEL_UP_MAX_DAMAGE_INCREASE():
    """Return the max_damage increase upon level up.

    :return: the max_damage increase upon level up as an integer
    """
    return 5


def LEVEL_UP_HP_INCREASE():
    """Return the health points increase upon level up.

    :return: the health points increase upon level up as an integer
    """
    return 10


def PLAYER_START_LOCATION():
    """Return a list of player starting location.

    :return: a list of player starting location.
    """
    return [0, 0]  # must be a list to increment or decrement with player_movement()


def PLAYER_EXPERIENCE_GAIN():
    """Return the experience gain upon killing a monster.

    :return: the experience gain upon killing a monster as an integer
    """
    return 5


def PLAYER_EXPERIENCE_LEVEL2():
    """Return the amount of experience needed for player to be level 2.

    :return: the amount of experience needed for player to be level 2 as an integer
    """
    return 20


def PLAYER_EXPERIENCE_LEVEL3():
    """Return the amount of experience needed for player to be level 3.

    :return: the amount of experience needed for player to be level 3 as an integer
    """
    return 40


def PLAYER_HP_HEAL():
    """Return the amount of health points a player heals by.

    :return: the amount of health points a player heals by as an integer
    """
    return 4


def PLAYER_UNSUCCESSFUL_FLEE_RATE():
    """Return the rate of an unsuccessful player flee.

    :return: the rate of an unsuccessful player flee as an integer
    """
    return 20


def SORCERER_MAX_DAMAGE_INCREASE():
    """Return the max_damage increase upon selecting sorcerer class.

    :return: the max_damage increase upon selecting sorcerer class as an integer
    """
    return 10


def SORCERER_MIN_DAMAGE_INCREASE():
    """Return the min_damage increase upon selecting sorcerer class.

    :return: the min_damage increase upon selecting sorcerer class as an integer
    """
    return 5


def SORCERER_HIT_RATE_DECREASE():
    """Return the hit_rate decrease upon selecting sorcerer class.

    :return: the hit_rate decrease upon selecting sorcerer class as an integer
    """
    return 15


def THIEF_MAX_DAMAGE_DECREASE():
    """Return the max_damage decrease upon selecting thief class.

    :return: the max_damage decrease upon selecting thief class as an integer
    """
    return 5


def THIEF_MIN_DAMAGE_INCREASE():
    """Return the min_damage increase upon selecting thief class.

    :return: the min_damage increase upon selecting thief class as an integer
    """
    return 5


def THIEF_HIT_RATE_INCREASE():
    """Return the hit_rate increase upon selecting thief class.

    :return: the hit_rate increase upon selecting thief class as an integer
    """
    return 10


def FIGHTER_MAX_DAMAGE_INCREASE():
    """Return the max_damage increase upon selecting fighter class.

    :return: the max_damage increase upon selecting fighter class as an integer
    """
    return 10


def FIGHTER_MIN_DAMAGE_DECREASE():
    """Return the min_damage increase upon selecting fighter class.

    :return: the min_damage increase upon selecting fighter class as an integer
    """
    return 4


def HIDDEN_LORD_MAX_DAMAGE_INCREASE():
    """Return the max_damage increase upon selecting hidden lord class.

    :return: the max_damage increase upon selecting hidden lord class as an integer
    """
    return 80


def HIDDEN_LORD_HP_INCREASE():
    """Return the health points increase upon selecting hidden lord class.

    :return: the health points increase upon selecting hidden lord class as an integer
    """
    return 50


def MONSTER_MIN_DAMAGE():
    """Return the min_damage of a monster.

    :return: the min_damage of a monster as an integer
    """
    return 1


def MONSTER_MAX_DAMAGE():
    """Return the max_damage of a monster.

    :return: the max_damage of a monster as an integer
    """
    return 15


def MONSTER_MIN_HP():
    """Return the minimum health points of a monster.

    :return: the minimum health points of a monster as an integer
    """
    return 5


def MONSTER_MAX_HP():
    """Return the maximum health points of a monster.

    :return: the maximum health points of a monster as an integer
    """
    return 20


def MONSTER_MIN_HIT_RATE():
    """Return the minimum hit rate of a monster.

    :return: the minimum hit rate of a monster as an integer
    """
    return 30


def MONSTER_MAX_HIT_RATE():
    """Return the maximum hit rate of a monster.

    :return: the maximum hit rate of a monster as an integer
    """
    return 70


def MONSTER_SPAWN_RATE():
    """Return the spawn rate of a monster.

    :return: the spawn rate of a monster as an integer
    """
    return 20


def MONSTER_DESCRIPTION_AMOUNT():
    """Return the amount of descriptions of a monster.

    :return: the amount of descriptions of a monster as an integer
    """
    return 2


def EVALUATE_MONSTER_HARD_HP():
    """Return the amount of health points to evaluate a monster with a difficulty of hard.

    :return: the amount of health points to evaluate a monster with a difficulty of hard as an integer
    """
    return 15


def EVALUATE_MONSTER_HARD_DAMAGE():
    """Return the amount of maximum damage to evaluate a monster with a difficulty of hard.

    :return: the amount of maximum damage to evaluate a monster with a difficulty of hard as an integer
    """
    return 10


def EVALUATE_MONSTER_HARD_HIT_RATE():
    """Return the amount of hit rate to evaluate a monster with a difficulty of hard.

    :return: the amount of hit rate to evaluate a monster with a difficulty of hard as an integer
    """
    return 50


def EVALUATE_MONSTER_MEDIUM_DAMAGE():
    """Return the amount of maximum damage to evaluate a monster with a difficulty of medium.

    :return: the amount of maximum damage to evaluate a monster with a difficulty of medium as an integer
    """
    return 8


def BOSS_LOCATION():
    """Return the location of a boss.

    :return: the location of a boss as a list
    """
    return [24, 24]


def BOSS_HP():
    """Return the health points of a boss.

    :return: the health points of a boss as an integer
    """
    return 100


def BOSS_MIN_DAMAGE():
    """Return the min_damage of a boss.

    :return: the min_damage of a boss as an integer
    """
    return 5


def BOSS_MAX_DAMAGE():
    """Return the max_damage of a boss.

    :return: the max_damage of a boss as an integer
    """
    return 15


def BOSS_HIT_RATE():
    """Return the hit rate of a boss.

    :return: the hit rate of a boss as an integer
    """
    return 80


def MAX_HIT_RATE():
    """Return the maximum hit rate.

    :return: the maximum hit rate as an integer
    """
    return 100


def MAX_FLEE_RATE():
    """Return the maximum flee rate.

    :return: the maximum flee rate as an integer
    """
    return 100


def MAX_FLEE_DAMAGE():
    """Return the maximum flee damage.

    :return: the maximum flee damage as an integer
    """
    return 15


def MAX_ROLL_NUMBER():
    """Return the upper bound of rolling a die.

    :return: the upper bound of rolling a die as an integer
    """
    return 100


def FLEE_RATE():
    """Return the flee rate.

    :return: the flee rate as an integer
    """
    return 20


def PLAYER_ICON():
    """Return the player icon.

    :return: the player icon as a string
    """
    return "😇"


def BOSS_ICON():
    """Return the boss icon.

    :return: the boss icon as a string
    """
    return "🐲"


def BOARD_DIMENSION():
    """Return the board dimension.

    :return: the board dimension as an integer
    """
    return 25


def typing_effect(words):
    """Print a string character by character with a delay.

    :param words: any string
    :precondition: words must be a string
    :postcondition: print a string character by character with a delay between every character
    :return: none
    """
    for char in words:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()


def ENDING_MESSAGE():
    """Return ASCII art.

    :return: ASCII art as a string
    """
    return "    ^                 🔥           🔥🔥🔥🔥🔥🔥🔥       🔥🔥🔥🔥🔥        🔥🔥🔥\n" \
           "   /|\        ii_     🔥🔥          ____________         ____   __         _____\n" \
           "  / | \_      /  *-i🔥🔥🔥         |            |       |    \ |  |       |     ＼\n" \
           " //\|/\ \    /  ---_🔥🔥🔥         |   _________|       |     \|  |       |   ___ ＼ \n" \
           "// ||| \ \__/   \_//               |  |_________        |         |       |  |   |  |\n" \
           "|   |   \__    /ー-                |   _________|       |  |\     |       |  |   |  |\n" \
           "v---v---\ /    i-|                 |  |_________        |  | \    |       |  |___|  |    \n" \
           "         |     i-|                 |            |       |  |  \   |       |        ／ \n" \
           "         |     i-|                 |____________|       |__|   \__|       |______／\n"


def make_map(dimension):
    """Create a list of coordinates of game board.

    :param dimension: a positive integer
    :precondition: dimension must be a positive integer greater than 1
    :postcondition: a list with tuples corresponding coordinates
    :return: a list of coordinates
    
    >>> test_board = make_map(5)
    >>> test_board
    [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
    """
    return [(x_axis, y_axis) for x_axis in range(dimension) for y_axis in range(dimension)]


def print_map(dimension, board, player):
    """Output a square game board allocating each tuple into a square bracket or icon.

    :param dimension: a positive integer
    :param board: a list containing tuples with correlation to dimension
    :param player: a dictionary
    :precondition: dimension must be an integer greater than 2
    :precondition: board must be a list containing tuples with correlation to dimension
    :precondition: board list must contain a squared amount of tuples of dimensions
                   # dimension 5, board must have 5**2 = 25 tuples
    :precondition: player must be a dictionary
    :precondition: player dictionary must contain a key of location with a value of two integers in a list
    :postcondition: print a game board
    :postcondition: print player icon on board corresponding to player location
    :postcondition: print boss icon on board corresponding to boss location
    :return: none
    
    >>> board = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
    >>> player = {"location": [0, 0]}
    >>> print_map(5, board, player)
    [ ][ ][ ][ ][ ]
    [ ][ ][ ][ ][ ]
    [ ][ ][ ][ ][ ]
    [ ][ ][ ][ ][ ]
    \033[05m😇\033[0m [ ][ ][ ][ ]
    """
    for y_coord in reversed(range(dimension)):  # reverse y_coord so that (0, 0) is at bottom left corner
        for x_coord in range(dimension):
            if (x_coord, y_coord) in board:
                if (x_coord, y_coord) == tuple(player["location"]):
                    print(BLINK() + PLAYER_ICON() + END() + " ", end="")
                elif (x_coord, y_coord) == tuple(BOSS_LOCATION()):
                    print(BOSS_ICON(), end="")
                else:
                    print("[ ]", end="")
        print()


def introduction_dialogue():
    """Print the dialogue explaining the game.

    :return: none
    
    >>> introduction_dialogue()
    Welcome to the World of the Medium | \033[35mEpisode 1\033[0m
    <BLANKLINE>
    Your soul has drifted from your body and now you are here to prove your worthiness.
    In order to proceed to heaven, you must defeat the mighty dragon, Kindred, who's guarding the Gates of Heaven.
    Kindred has been sending adventurers like you into the depths of hell. You must defeat Kindred to prove your worthiness, and then push through the Gates of Heaven.
    <BLANKLINE>
    You will choose a class with certain stats and abilities to aid your task of defeating Kindred.
    """
    typing_effect("Welcome to the World of the Medium | %sEpisode 1%s\n\n"
                  "Your soul has drifted from your body and now you are here to prove your worthiness.\n"
                  "In order to proceed to heaven, you must defeat the mighty dragon, Kindred, who's "
                  "guarding the Gates of Heaven.\n"
                  "Kindred has been sending adventurers like you into the depths of hell. You must "
                  "defeat Kindred to prove your worthiness, and then push through the Gates of Heaven.\n\n"
                  "You will choose a class with certain stats and abilities to aid your task of defeating "
                  "Kindred.\n" % (PURPLE(), END()))


def class_description():
    """Print the description of the classes.

    :return: none

    >>> class_description()
    <BLANKLINE>
    Classes
    <BLANKLINE>
    \033[31m0\033[0m \033[04mSorcerer\033[0m:
    Sorcerers uses magic to attack.
    Their damage is amplified, but not the most accurate!
    Sorcerers begin as a Magician, advance into a Wizard, and finally transcend into a High Wizard.
    <BLANKLINE>
    \033[31m1\033[0m \033[04mThief\033[0m:
    Thieves lurk through the shadows with striking with deadly accuracy.
    Their accuracy is near-perfect, but lack the strength to damage!
    Thieves begin as a Thief, advance into a Bandit, and finally transcend into a Night Lord.
    <BLANKLINE>
    \033[31m2\033[0m \033[04mAmazon\033[0m:
    Amazons specialize in archery, swordplay, and a bit of magic.
    Amazon's are the most well-balanced class!
    Amazons begin as a Novice, advance into an Amazon, and transcend into a Pathfinder.
    <BLANKLINE>
    \033[31m3\033[0m \033[04mFighter\033[0m:
    Fighters have incredible yet, uncontrollable strength.
    Their uncontrollable strength can easily dissipate weak monsters!
    Fighters begin as a Brawler, advance into a Buccaneer, and transcend into a Sensei.
    <BLANKLINE>
    """
    print("\nClasses\n\n"
          "%s0%s %sSorcerer%s:\nSorcerers uses magic to attack."
          "\nTheir damage is amplified, but not the most accurate!\n"
          "Sorcerers begin as a Magician, advance into a Wizard, and finally transcend into a High Wizard.\n\n"
          "%s1%s %sThief%s:\nThieves lurk through the shadows with striking with deadly accuracy."
          "\nTheir accuracy is near-perfect, but lack the strength to damage!\n"
          "Thieves begin as a Thief, advance into a Bandit, and finally transcend into a Night Lord.\n\n"
          "%s2%s %sAmazon%s:\nAmazons specialize in archery, swordplay, and a bit of magic."
          "\nAmazon's are the most well-balanced class!\n"
          "Amazons begin as a Novice, advance into an Amazon, and transcend into a Pathfinder.\n\n"
          "%s3%s %sFighter%s:\nFighters have incredible yet, uncontrollable strength."
          "\nTheir uncontrollable strength can easily dissipate weak monsters!\n"
          "Fighters begin as a Brawler, advance into a Buccaneer, and transcend into a Sensei.\n"
          % (RED(), END(), UNDERLINE(), END(), RED(), END(), UNDERLINE(), END(), RED(), END(), UNDERLINE(), END(),
             RED(), END(), UNDERLINE(), END()))


def class_stats(player: dict):  # amazon no stat changes
    """Determine player class and add stat according to class.

    :param player: a dictionary
    :precondition: player must be a dictionary with keys: "master_class", "min_damage", "max_damage", "hit_rate"
    :precondition: player dictionary keys: "min_damage", "max_damage", "hit_rate" must be integers
    :precondition: player dictionary key "master_class" must be a string
    :postcondition: increment key values for depending on player class
    :return: none

    >>> player = {"master_class": "Sorcerer", "max_damage": 10, "min_damage": 5, "hit_rate": 60}
    >>> class_stats(player)
    >>> player
    {'master_class': 'Sorcerer', 'max_damage': 20, 'min_damage': 15, 'hit_rate': 45}
    >>> player = {"master_class": "Thief", "max_damage": 10, "min_damage": 5, "hit_rate": 60}
    >>> class_stats(player)
    >>> player
    {'master_class': 'Thief', 'max_damage': 5, 'min_damage': 10, 'hit_rate': 70}
    """
    if player["master_class"] == "Sorcerer":
        player["max_damage"] += SORCERER_MAX_DAMAGE_INCREASE()  # low chance of hit high damage
        player["min_damage"] += SORCERER_MAX_DAMAGE_INCREASE()
        player["hit_rate"] -= SORCERER_HIT_RATE_DECREASE()
    elif player["master_class"] == "Thief":
        player["max_damage"] -= THIEF_MAX_DAMAGE_DECREASE()  # high hit rate low damage
        player["min_damage"] += THIEF_MIN_DAMAGE_INCREASE()
        player["hit_rate"] += THIEF_HIT_RATE_INCREASE()
    elif player["master_class"] == "Fighter":
        player["max_damage"] += FIGHTER_MAX_DAMAGE_INCREASE()  # high damage low chance of deadly hit
        player["min_damage"] -= FIGHTER_MIN_DAMAGE_DECREASE()
    else:
        player["max_damage"] += HIDDEN_LORD_MAX_DAMAGE_INCREASE()
        player["HP"] += HIDDEN_LORD_HP_INCREASE()
        player["max_HP"] += HIDDEN_LORD_HP_INCREASE()


def determine_sub_class(player: dict) -> list:
    """Return a list of sub classes for master class.

    :param player: a dictionary
    :precondition: player must be a dictionary containing a key-value pair of "master_class"
    :precondition: player key "master_class" must have a value of a string
    :postcondition: return a list of sub classes of the master class
    :return: a list of sub classes

    >>> player = {'master_class': "Sorcerer"}
    >>> determine_sub_class(player)
    ['Magician', 'Wizard', 'High Wizard']
    >>> player = {'master_class': 'Hidden Lord'}
    >>> determine_sub_class(player)
    ['Master', 'Lord', 'God']
    """
    if player['master_class'] == "Sorcerer":
        return ["Magician", "Wizard", "High Wizard"]
    elif player['master_class'] == "Thief":
        return ["Thief", "Bandit", "Night Lord"]
    elif player['master_class'] == "Amazon":
        return ["Novice", "Amazon", "Pathfinder"]
    elif player['master_class'] == "Fighter":
        return ["Brawler", "Buccaneer", "Sensei"]
    else:
        return ["Master", "Lord", "God"]


def player_sub_class(player: dict) -> str:
    """Modify player dictionary to include sub_class of correct master_class based on level

    :param player: a dictionary
    :precondition: player must be a dictionary containing a key-value pair of "master_class"
    :precondition: player key "master_class" must have a value of a string
    :postcondition: player key "sub_class" will have a value of the correct sub_class
    :return: append key "sub_class" with a value to player dictionary

    >>> test_player = {'master_class': 'Sorcerer', 'level': 1}
    >>> player_sub_class(test_player)
    'Magician'
    >>> test_player = {'master_class': 'Sorcerer', 'level': 2}
    >>> player_sub_class(test_player)
    'Wizard'
    """
    list_increment = player["level"]
    player["sub_class"] = determine_sub_class(player)[
        -1 + list_increment]  # must start at -1 because player level starts at 1
    return player["sub_class"]


def class_choice():
    """ Prompt user input to select a class.

    :return: none
    """
    class_list = enumerate(("Sorcerer", "Thief", "Amazon", "Fighter"))
    valid_class_num = ["0", "1", "2", "3", "1337"]
    while True:
        player_class = input("Which class will you choose? (Enter corresponding number to pick your class): ")
        if player_class in valid_class_num:
            for jobs in class_list:
                if player_class == str(jobs[0]):
                    return jobs[1]
                elif player_class == "1337":
                    return "Hidden Lord"
        else:
            print("\nPlease input valid input\n")


def make_player():
    """Prompt user for information and store information into a dictionary.

    :postcondition: create a dictionary representing game player
    :return: a dictionary representing player
    """
    name = input("But first, what is your name?: ")
    typing_effect(f"\nHi {name}, you must now pick your class.\nHere is a list of all of the classes:\n")
    sleep(1)
    class_description()
    player_class = class_choice()
    player = {"name": BLUE() + name + END(),
              "master_class": player_class,
              "level": PLAYER_LEVEL(),
              "HP": PLAYER_START_HP(),
              "max_HP": PLAYER_START_HP(),
              "hit_rate": PLAYER_START_HIT_RATE(),
              "XP": PLAYER_START_EXPERIENCE(),
              "min_damage": PLAYER_START_MIN_DAMAGE(),
              "max_damage": PLAYER_START_MAX_DAMAGE(),
              "location": PLAYER_START_LOCATION()}
    class_stats(player)
    player_sub_class(player)
    return player


def instruction_dialogue(player):
    """Print the dialogue explaining the game.

    :return: none
    
    >>> player = {'name': 'Im crying', 'master_class': 'Sorcerer'}
    >>> instruction_dialogue(player)
    <BLANKLINE>
    Good choice Im crying! Sorcerer is what I would have picked too!
    Now you must travel up to the top right corner 🐲 | Location: [24, 24], and defeat Kindred!
    There will be monsters a long the way, kill them to earn XP to level up and gain bonus stats!
    I wish you the best of luck, adventurer.
    <BLANKLINE>
    """
    typing_effect(f"\nGood choice {player['name']}! {player['master_class']} is what I would have picked too!\n"
                  f"Now you must travel up to the top right corner {BOSS_ICON()} "
                  f"| Location: {BOSS_LOCATION()}, and defeat Kindred!\n"
                  f"There will be monsters a long the way, kill them to earn XP to level up "
                  f"and gain bonus stats!\n"
                  f"I wish you the best of luck, adventurer.\n\n")
    sleep(2)


def get_player_move():
    """Prompt user for direction change.

    :postcondition: return player_direction if valid else print Invalid message
    :return: a string representing players moving direction
    """
    print("\nInstructions:\n %s0%s : Up \n %s1%s : Down \n %s2%s : Left\n %s3%s : Right\n %sQ%s : Quit\n"
          % (RED(), END(), RED(), END(), RED(), END(), RED(), END(), YELLOW(), END()))
    valid_user_input = ["0", "1", "2", "3", "q", "Q", "h", "H"]
    while True:
        player_direction = input("Which direction will you go? "
                                 "(Enter corresponding number/letter to pick your action.): ")
        if player_direction in valid_user_input:
            return player_direction
        else:
            print("\nInvalid Input\nPlease Try Again\n")


def player_destination(direction: str, player: dict) -> tuple:
    """Create players next destination.

    :param direction: a string
    :param player: a dictionary
    :precondition: direction must be a string number of 0, 1, 2, or 3
    :precondition: player must be a dictionary representing player
    :postcondition: create a tuple of players next destination on game board
    :return: a tuple representing location on game board

    >>> test_player = {'location': [0, 0]}
    >>> player_destination("0", test_player)
    (0, 1)
    >>> test_player = {'location': [0, 0]}
    >>> player_destination("1", test_player)
    (0, -1)
    >>> test_player = {'location': [0, 0]}
    >>> player_destination("2", test_player)
    (-1, 0)
    >>> test_player = {'location': [0, 0]}
    >>> player_destination("3", test_player)
    (1, 0)
    """
    new_location = list(player["location"])
    if direction == "0":
        new_location[1] += 1  # up
    elif direction == "1":
        new_location[1] -= 1  # down
    elif direction == "2":
        new_location[0] -= 1  # left
    elif direction == "3":
        new_location[0] += 1  # right
    return tuple(new_location)


def validate_move(new_location: tuple, board: list) -> bool:
    """Validate the destination the player wants to go.

    :param new_location: a tuple
    :param board: a list of tuples
    :precondition: new_location must be a tuple of coordinates
    :precondition: board must be a list of tuples representing game board
    :postcondition: check if new_location is within board
    :return: true if new_location is in board else False
    
    >>> board = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    >>> validate_move((1, 1), board)
    True
    >>> validate_move((4, 4), board)
    False
    """
    if new_location in board:
        return True
    else:
        return False


def move_player(direction: str, player: dict):
    """Modify location of player.

    :param direction: a string
    :param player: a dictionary
    :precondition: direction must be a string number of 0, 1, 2, 3
    :precondition: character must be a dictionary representing player
    :postcondition: modify character['location'] value according to direction
    :return: None

    >>> player = {'location': [0, 0]}
    >>> move_player("0", player)
    >>> player
    {'location': [0, 1]}
    >>> move_player("1", player)
    >>> player
    {'location': [0, 0]}
    >>> move_player("3", player)
    >>> player
    {'location': [1, 0]}
    >>> move_player("2", player)
    >>> player
    {'location': [0, 0]}
    """
    if direction == "0":
        player["location"][1] += 1  # up
    elif direction == "1":
        player["location"][1] -= 1  # down
    elif direction == "2":
        player["location"][0] -= 1  # left
    elif direction == "3":
        player["location"][0] += 1  # right


def check_for_monster(player: dict) -> bool:
    """Check if there is a monster.

    :param player: a dictionary
    :precondition: player must be a dictionary representing game player
    :postcondition: return True with a chance of MONSTER_SPAWN_RATE else False
    :return: True if random choice is smaller than MONSTER_SPAWN_RATE
    """
    if player["location"] != BOSS_LOCATION():
        if random.randint(1, 100) <= MONSTER_SPAWN_RATE():
            print("\nA monster has appeared!")
            return True
        else:
            return False


def generate_monster(player: dict):
    """Create a dictionary of a monster with random values and description.

    :param: player must be a dictionary
    :precondition: player must contain a key called "HP"
    :precondition: player "HP" must be a positive integer greater than 0
    :postcondition: create a monster dictionary for combat
    :return: a dictionary representing a monster
    """
    monster_name = random.choice(["Dragon", "Kobold", "Fenrir", "Loki", "Surtr"])
    monster_activity = random.choice(["staring at you", "snarling at you", "stalking you", "ready to pounce at you"])
    monster_description = ["Humongous", "Murderous", "Rabid", "Psycho", "Hostile"]
    monster_state = list(itertools.permutations
                         (monster_description, MONSTER_DESCRIPTION_AMOUNT()))  # 2 for 2 monster descriptions.

    def filter_moves(monster_moves_level_2):
        """Compare list of monster moves.

        :param monster_moves_level_2: a list
        :precondition: monster_moves_level_2 must be a list containing items from monster_moves_level_1
        :precondition: monster_moves_level_2 must also have additional items of monster moves
        :postcondition: evaluate True or False
        :return: True or False
        """
        monster_moves_level_1 = ["Bite", "Chomp", "Body Slam", "Scratch"]
        if monster_moves_level_2 in monster_moves_level_1:
            return True
        else:
            return False

    def generate_foe_moves_based_on_player_level():
        """Generate a random attack move for a monster.

        :postcondition: randomly generate an attack move for monster
        :return: an attack move as a string
        """
        monster_attacks = ["Bite", "Chomp", "Slam", "Scratch", "Hyper Beam", "Dark Crunch", "Cosmic Flare"]
        if player["level"] > 1:
            return random.choice(monster_attacks)
        else:
            monster_moves_for_level_1 = list(filter(filter_moves, monster_attacks))
            return random.choice(monster_moves_for_level_1)

    monster = {"name": YELLOW() + monster_name + END(),
               "description": random.choice(monster_state),
               "HP": random.randint(MONSTER_MIN_HP(), MONSTER_MAX_HP()),
               "min_damage": MONSTER_MIN_DAMAGE(),
               "max_damage": random.randint(MONSTER_MIN_DAMAGE(), MONSTER_MAX_DAMAGE()),
               "hit_rate": random.randint(MONSTER_MIN_HIT_RATE(), MONSTER_MAX_HIT_RATE()),
               "attack_move": generate_foe_moves_based_on_player_level()}
    print(f"\nA {monster['description'][0]} and {monster['description'][1]} {monster['name']} is {monster_activity}")
    return monster


def evaluate_monster_difficulty(monster: dict):
    """Display monster difficulty.

    :param monster: a dictionary
    :precondition: monster must be a dictionary representing game monster
    :precondition: monster must contain the keys : "max_damage", "hit_rate", "HP"
    :precondition:: monster keys must have values that are integers
    :postcondition: evaluate the values and print a message to user
    :postcondition: message will display the difficulty of the monster
    :return: none

    >>> evaluate_monster_difficulty({'HP': 15, 'max_damage': 11, 'hit_rate': 60})
    Difficulty : \033[33mMEDIUM\033[0m | HP: 15
    >>> evaluate_monster_difficulty({'HP': 20, 'max_damage': 20, 'hit_rate': 80})
    Difficulty : \033[31mHARD\033[0m | HP: 20
    >>> evaluate_monster_difficulty({'HP': 5, 'max_damage': 5, 'hit_rate': 5})
    Difficulty : \033[32mEASY\033[0m | HP: 5
    """
    if monster["HP"] > EVALUATE_MONSTER_HARD_HP() and \
            monster["max_damage"] > EVALUATE_MONSTER_HARD_DAMAGE() and \
            monster["hit_rate"] > EVALUATE_MONSTER_HARD_HIT_RATE():
        print(f"Difficulty : %sHARD%s | HP: {monster['HP']}" % (RED(), END()))
    elif monster["HP"] > EVALUATE_MONSTER_HARD_HP() or \
            monster["max_damage"] > EVALUATE_MONSTER_MEDIUM_DAMAGE() or \
            monster["hit_rate"] > EVALUATE_MONSTER_HARD_HIT_RATE():
        print(f"Difficulty : %sMEDIUM%s | HP: {monster['HP']}" % (YELLOW(), END()))
    else:
        print(f"Difficulty : %sEASY%s | HP: {monster['HP']}" % (GREEN(), END()))


def player_flee(player: dict):
    """Flee from foe with a chance of losing HP.

    :param player: a dictionary
    :precondition: player must be a dictionary
    :precondition: player must have a key called "HP"
    :precondition: player "HP" must have a value that is an integer > 0
    :postcondition: 20% chance of taking a random amount of damage upon fleeing
    :postcondition: print a message displaying what happened
    :return: none
    """
    if random.randint(1, MAX_FLEE_RATE()) <= PLAYER_UNSUCCESSFUL_FLEE_RATE():
        flee_damage = random.randint(1, MAX_FLEE_DAMAGE())
        player["HP"] -= flee_damage
        print(f"You fled but took a stab to the back {flee_damage}")
    else:
        print("You fled successfully!")


def monster_flee(player: dict) -> bool:
    """Evaluate if monster flee is True or False.

    :param player: a dictionary
    :precondition: player must be a dictionary containing a key called location
    :precondition: player location must contain a list with 2 integers
    :postcondition: randomly determine if monster has fled
    :return: boolean value True or False
    """
    if random.randint(1, MAX_FLEE_RATE()) <= FLEE_RATE() and player["location"] != BOSS_LOCATION():
        return True
    else:
        return False


def player_heal(player: dict):
    """Increment player health points.

    :param player: a dictionary
    :precondition: player must be a dictionary containing keys : "HP" and "max_HP"
    :precondition: player "HP" and "max_HP" values must be integers > 0
    :postcondition: increment the key-value pair "HP"
    :postcondition: "HP" will not exceed "max_HP"
    :return: None

    >>> player_heal({'HP': 5, 'max_HP': 10})
    <BLANKLINE>
    You have recovered HP 
    Your new HP is 9
    >>> test_player = {'HP': 10, 'max_HP': 10}
    >>> player_heal(test_player)
    >>> test_player
    {'HP': 10, 'max_HP': 10}
    """
    if player["HP"] < player["max_HP"]:
        player["HP"] = min(player["HP"] + PLAYER_HP_HEAL(), player["max_HP"])
        print(f"\nYou have recovered HP \nYour new HP is {player['HP']}")


def player_restart():
    """Prompt user to restart or quit.

    :precondition: player has reached goal, or player_hp is 0
    :precondition: user input must be "y" or "n"
    :postcondition: "y" will restart game for user
    :postcondition: "n" will exit out of program for user
    :return: none
    """
    while True:
        restart = input("\nWould you like to restart?\n%sY%s for Yes\n%sN%s for No\n\n"
                        "What will you do? (Enter corresponding letter to pick your action.): "
                        % (RED(), END(), RED(), END()))
        if restart.lower() == "y":
            game()
            exit()
        elif restart.lower() == "n":
            print("Good bye. Good luck on your adventure next time!")
            exit()
        else:
            print("Invalid input, please input y or n")


def is_player_dead(player: dict):           # function leads to player_restart, which takes input. partial doctest.
    """Check if player is dead.

    :param player: a dictionary
    :precondition: player must be a dictionary with key value 'HP' and integer 
    :postcondition: print message to user is player HP is smaller or equal to 0
    :postcondition: invoke player_restart if player HP is smaller or equal to 0 
    :return: None

    >>> is_player_dead({'HP': 1})
    """
    if player["HP"] <= 0:
        print("\nYou have failed your mission.\n")
        player_restart()


def roll_for_first_hit(player: dict, foe: dict) -> bool:
    """Roll dice for first hit.

    :param player: a dictionary
    :param foe: a dictionary
    :precondition: player and foe must be a dictionary with key value pair 'name' and string
    :postcondition: return True is player rolled greater number than foe else False
    :return: boolean
    """
    roll_dice = False
    while not roll_dice:
        player_roll = random.randint(1, MAX_ROLL_NUMBER())
        foe_roll = random.randint(1, MAX_ROLL_NUMBER())
        typing_effect(f"\n{player['name']} has rolled a {player_roll}\n{foe['name']} has rolled a {foe_roll}\n\n")
        if player_roll > foe_roll:
            typing_effect(f"{player['name']} has the first move!\n\n")
            return True
        elif player_roll < foe_roll:
            typing_effect(f"{foe['name']} has the first move!\n\n")
            return False


def hit_or_miss(game_chara: dict):  # True if hits false if miss
    """Determine if character hit or miss.

    :param game_chara: a dictionary
    :precondition: game_chara must be a dictionary with key value pair of 'hit_rate' and integer
    :postcondition: return True if random.randint is smaller than or equal
                    to game_chara["hit_rate"] else False
    :return: boolean
    """
    if random.randint(1, MAX_HIT_RATE()) <= game_chara["hit_rate"]:
        return True
    else:
        return False


def combat_moves_list(player):
    """Create list with combat moves.

    :param player: a dictionary
    :precondition: player must be a dictionary with key value pair 'master_class' and string for class
    :postcondition: return combat moves for each player class
    :return: a list with combat moves items

    >>> combat_moves_list({'master_class': 'Sorcerer'})
    [(1, 'Fire Ball'), (2, 'Icicle Attack'), (3, 'Lightning Strike'), (4, 'Flee')]
    >>> combat_moves_list({'master_class': 'Thief'})
    [(1, 'Throw Ninja Star'), (2, 'Dagger Stab'), (3, 'Punch'), (4, 'Flee')]
    >>> combat_moves_list({'master_class': 'Amazon'})
    [(1, 'Arrow Shot'), (2, 'Sword Slash'), (3, 'Fire Ball'), (4, 'Flee')]
    >>> combat_moves_list({'master_class': 'Fighter'})
    [(1, 'Power Punch'), (2, 'Roundhouse Kick'), (3, 'Body Slam'), (4, 'Flee')]
    >>> combat_moves_list({'master_class': 'Hidden Lord'})
    [(1, 'Lightning Punch'), (2, 'Fire Storm'), (3, 'Darkness Beam'), (4, 'Flee')]
    """
    if player["master_class"] == "Sorcerer":
        return list(enumerate(
            ["Fire Ball", "Icicle Attack", "Lightning Strike", "Flee"],
            1))  # I used list in order to use it in combat options.
    elif player["master_class"] == "Thief":
        return list(enumerate(["Throw Ninja Star", "Dagger Stab", "Punch", "Flee"], 1))
    elif player["master_class"] == "Amazon":
        return list(enumerate(["Arrow Shot", "Sword Slash", "Fire Ball", "Flee"], 1))
    elif player["master_class"] == "Fighter":
        return list(enumerate(["Power Punch", "Roundhouse Kick", "Body Slam", "Flee"], 1))
    elif player["master_class"] == "Hidden Lord":
        return list(enumerate(["Lightning Punch", "Fire Storm", "Darkness Beam", "Flee"], 1))


def attack(attacker, receiver):
    """Attack receiver.

    :param attacker: a dictionary
    :param receiver: a dictionary
    :precondition: player and receiver must be a dictionary with key value pair 'attack_move' with string
    :precondition: player and receiver must be a dictionary with key value pair 'min_damage' and 'max_damage' with integer
    :precondition: player and receiver must be a dictionary with key value pair 'HP' and integer
    :postcondition: subtract receiver HP if hit_or_miss(attacker) is True else display that user missed
    :postcondition: display message death message is receiver HP is smaller than or equal to 0
    :return: None
    """
    typing_effect(f"{attacker['name']} used %s{attacker['attack_move']}%s!\n" % (RED(), END()))
    if hit_or_miss(attacker):
        attacker_damage = random.randint(attacker["min_damage"], attacker["max_damage"])
        receiver["HP"] = max(receiver["HP"] - attacker_damage, 0)
        typing_effect(f"{attacker['name']} dealt {attacker_damage} damage! | {receiver['name']} HP:{receiver['HP']}\n")
    else:
        typing_effect(f"{attacker['name']} missed! | {receiver['name']} HP:{receiver['HP']}\n")
    if receiver["HP"] <= 0:
        sleep(1)
        print(f"{receiver['name']} has died.")
    print()


def combat_round(player, foe, player_attack_first):
    """Fight the Foe.

    :param player: a dictionary
    :param foe: a dictionary 
    :param player_attack_first: boolean 
    :precondition: player must be a dictionary with key "name”, "master_class", "level", "HP",
                   "max_HP", "hit_rate", "XP", "min_damage", "max_damage", "location"
    :precondition: foe must be a dictionary with "name”, "master_class", "level", "HP",
                   "max_HP", "hit_rate", "XP", "min_damage", "max_damage", "location" 
    :postcondition: invoke a round of combat between player and foe
    :postcondition: after a round of combat check if monster flee
    :postcondition: if both player and foe HP is not equal to 0 invoke combat()
    :postcondition: if either player or foe HP is 0 invoke is_player_dead()
    :postcondition: if either player or foe HP is 0 invoke after_combat()
    :return: None
    """
    (first_hit, second_hit) = (player, foe) if player_attack_first else (foe, player)
    while first_hit["HP"] > 0 and second_hit["HP"] > 0:
        attack(first_hit, second_hit)
        if second_hit["HP"] > 0:
            attack(second_hit, first_hit)
            break
    if first_hit["HP"] > 0 and second_hit["HP"] > 0:
        if monster_flee(player):
            typing_effect("Monster got scared of you and fled!\n")
            sleep(1)
        else:
            combat(player, foe, player_attack_first)
    else:
        is_player_dead(player)
        after_combat(player)


def combat_options(player):
    """Display combat options to player.

    :param player: a dictionary
    :precondition: player must be a dictionary with key "name”, "master_class", "level",
                   "HP", "max_HP", "hit_rate", "XP", "min_damage", "max_damage", "location"
    :postcondition: remove flee option if player location is at BOSS_LOCATION()
    :postcondition: print combat_option for user class
    :postcondition: return chosen combat move
    :postcondition: print invalid message if input is not in attack_moves
    :return: string if user input is valid
    """
    attack_moves = combat_moves_list(player)
    if player["location"] == BOSS_LOCATION():
        attack_moves.pop()
    for move in attack_moves:
        print(RED() + f"{move[0]}" + END() + " : " + move[1] + "\n", end="")
    while True:
        player_move = input(
            "\nWhat will you do? (Enter corresponding number to pick your action.): ")
        for move in attack_moves:
            if player_move == str(move[0]):
                return move[1]
        else:
            print("\nInvalid Input")


def validate_combat_option(player, foe, move, who_strike_first):
    """Validate player combat option

    :param player: a dictionary
    :param foe: a dictionary
    :param move: a string
    :param who_strike_first: a boolean
    :precondition: player must be a dictionary with key "name”, "master_class", "level", "HP",
                   "max_HP", "hit_rate", "XP", "min_damage", "max_damage", "location"
    :precondition: foe must be a dictionary with key "name”, "master_class", "level", "HP",
                   "max_HP", "hit_rate", "XP", "min_damage", "max_damage"
    :postcondition: invoke player_flee if move is Flee else pass to player["attack_move"]
                    to invoke combat_round()
    :return: None
    """
    if move == "Flee":
        player_flee(player)
    else:
        player["attack_move"] = move
        combat_round(player, foe, who_strike_first)


def check_experience(player):
    """Check is player can level up.

    :param player: a dictionary
    :precondition: player must be a dictionary with key "name”, "master_class", "level",
                   "HP", "max_HP", "hit_rate", "XP", "min_damage", "max_damage", "location"
    :postcondition: return True if player XP is equal to PLAYER_EXPERIENCE_LEVEL2() or
                    PLAYER_EXPERIENCE_LEVEL3() else False
    :return: a boolean

    >>> check_experience({'XP': 10})
    False
    >>> check_experience({'XP': 20})
    True
    >>> check_experience({'XP': 40})
    True
    >>> check_experience({'XP': 60})
    False
    """
    if player["XP"] == PLAYER_EXPERIENCE_LEVEL2() or player["XP"] == PLAYER_EXPERIENCE_LEVEL3():
        return True
    else:
        return False


def character_levelup(player):
    """Level up player.
    
    :param player: a dictionary 
    :precondition: player must be a dictionary with key "name”, "master_class", "level",
                   "HP","max_HP", "hit_rate", "XP", "min_damage", "max_damage", "location"
    :postcondition: increase "level", "HP","max_HP","hit_rate", "min_damage","max_damage"
    :postcondition: display current status to user
    :return: None

    >>> test_player = {'master_class': 'Hidden Lord', 'level': 1, 'hit_rate': 60, 'min_damage': 5, 'max_damage': 20, 'max_HP': 20, 'HP': 20}
    >>> character_levelup(test_player)
    <BLANKLINE>
    You have leveled up!
    You are now Level 2
    <BLANKLINE>
    You have job advanced to \033[31mLord!\033[0m
    <BLANKLINE>
    Your HP increased by 5
    Your accuracy increased by 5
    Your minimum damage increased by 2
    Your maximum damage increased by 5
    And you have fully recovered your HP!
    <BLANKLINE>
    Master Class: Hidden Lord
    Damage Range: 7 - 25
    Accuracy: 65%
    """
    player["level"] += PLAYER_LEVEL()
    player_sub_class(player)
    if player["hit_rate"] < MAX_HIT_RATE():
        player["hit_rate"] += LEVEL_UP_HIT_RATE_INCREASE()
    player["min_damage"] += LEVEL_UP_MIN_DAMAGE_INCREASE()
    player["max_damage"] += LEVEL_UP_MAX_DAMAGE_INCREASE()
    player["max_HP"] += LEVEL_UP_HP_INCREASE()
    player["HP"] = player["max_HP"]  # When player levels up, HP will be fully restored
    typing_effect(f"\nYou have leveled up!\n"
                  f"You are now Level {player['level']}\n"
                  f"\nYou have job advanced to %s{player['sub_class']}!%s\n" % (RED(), END()))
    sleep(1)
    typing_effect(f"\nYour HP increased by {LEVEL_UP_HIT_RATE_INCREASE()}"
                  f"\nYour accuracy increased by {LEVEL_UP_HIT_RATE_INCREASE()}"
                  f"\nYour minimum damage increased by {LEVEL_UP_MIN_DAMAGE_INCREASE()}"
                  f"\nYour maximum damage increased by {LEVEL_UP_MAX_DAMAGE_INCREASE()}"
                  f"\nAnd you have fully recovered your HP!\n")
    print(f"\nMaster Class: {player['master_class']}"
          f"\nDamage Range: {player['min_damage']} - {player['max_damage']}"
          f"\nAccuracy: {player['hit_rate']}%")


def after_combat(player):
    """Increase player XP.

    :param player: a dictionary
    :precondition: player must be a dictionary with key "name”, "master_class", "level",
                   "HP", "max_HP", "hit_rate", "XP", "min_damage", "max_damage", "location"
    :postcondition: increase player XP if player location is not BOSS_LOCATION() 
    :postcondition: invoke character_levelup()
    :return: None
    """
    if not player["location"] == BOSS_LOCATION():
        player["XP"] += PLAYER_EXPERIENCE_GAIN()
        typing_effect(f"You have gained {PLAYER_EXPERIENCE_GAIN()} XP!\nYour current XP is {player['XP']}\n")
        sleep(1)
        if check_experience(player):
            character_levelup(player)


def combat(player, foe, who_strike_first):
    """Execute combat.

    :param player: a dictionary
    :param foe: a dictionary
    :param who_strike_first: a boolean value
    :precondition: player must be a dictionary with key "name”, "master_class", "level", "HP",
                   "max_HP", "hit_rate", "XP", "min_damage", "max_damage", "location"
    :precondition: foe must be a dictionary with key "name”, "HP","max_HP","hit_rate","min_damage","max_damage"
    :precondition: who_strike_first must be True or False
    :postcondition: invoke combat_options()
    :postcondition: pass return value of combat_options to validate_combat_options()
    :return: None
    """
    move = combat_options(player)
    validate_combat_option(player, foe, move, who_strike_first)


def player_reach_boss(player):
    """Create boss for final battle.

    :param player: a dictionary
    :precondition: player must be a dictionary with key "name”, "master_class", "level", "HP",
                   "max_HP", "hit_rate", "XP", "min_damage", "max_damage", "location"
    :postcondition: create boss dictionary if player location is BOSS_LOCATION()
    :postcondition: initiate combat between player and boss
    :postcondition: invoke player_restart()
    :return: None
    """
    if player["location"] == BOSS_LOCATION():
        boss_attack_moves = ["Dragon's Breath", "Zeus's Lightning", "Dragon Claw", "Dragon Tail"]
        random_boss_attack = random.choice(boss_attack_moves)
        boss = {"name": "%sKindred%s" % (PURPLE(), END()),
                "HP": BOSS_HP(),
                "max_HP": BOSS_HP(),
                "min_damage": BOSS_MIN_DAMAGE(),
                "max_damage": BOSS_MAX_DAMAGE(),
                "hit_rate": BOSS_HIT_RATE(),
                "attack_move": random_boss_attack
                }
        typing_effect(f"\nYou have reached Kindred(HP: {boss['HP']}), "
                      f"the mighty Dragon who blocks the gates to Heaven\n")
        who_strike_first = roll_for_first_hit(player, boss)
        combat(player, boss, who_strike_first)
        if boss["HP"] <= 0:
            typing_effect("Congratulations! You have defeated Kindred!\n Next episode coming soon!\n")
            sleep(1)
            print(ENDING_MESSAGE())
            player_restart()


def game():
    """Play game
    """
    introduction_dialogue()
    character = make_player()
    board = make_map(BOARD_DIMENSION())
    achieve_goal = False
    print_map(BOARD_DIMENSION(), board, character)
    instruction_dialogue(character)
    while not achieve_goal:
        direction = get_player_move()
        if direction.lower() == "q":
            break
        destination = player_destination(direction, character)
        if validate_move(destination, board):
            move_player(direction, character)
            print_map(BOARD_DIMENSION(), board, character)
            print(f"Name: {character['name']} | "
                  f"HP: {character['HP']} | "
                  f"Level: {character['level']} | "
                  f"Class: {character['sub_class']} | "
                  f"XP: {character['XP']} | "
                  f"Location: {character['location']}"
                  f"\nDamage Range: {character['min_damage']} - {character['max_damage']}"
                  f"\nAccuracy: {character['hit_rate']}%")
            if check_for_monster(character):
                foe = generate_monster(character)
                evaluate_monster_difficulty(foe)
                player_attack_first = roll_for_first_hit(character, foe)
                combat(character, foe, player_attack_first)
            else:
                player_heal(character)
                player_reach_boss(character)
        else:
            print("\nYou can't move in that direction.")


def main():
    """
    Drive the program
    """
    game()


if __name__ == "__main__":
    testmod(verbose=True)
