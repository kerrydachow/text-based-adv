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
    """Return ANSI escape for text color red.
    """
    return "\033[31m"


def BLUE():
    """Return ANSI escape for text color blue.
    """
    return "\033[34m"


def GREEN():
    """Return ANSI escape for text color green.
    """
    return "\033[32m"


def YELLOW():
    """Return ANSI escape for text color yellow.
    """
    return "\033[33m"


def CYAN():
    """Return ANSI escape for text color cyan.
    """
    return "\033[36m"


def END():
    """Return ANSI escape to terminate previous ANSI escape codes.
    """
    return "\033[0m"


def BOLD():
    """Return ANSI escape for bold text.
    """
    return "\033[01m"


def UNDERLINE():
    """Return ANSI escape for text underline.
    """
    return "\033[04m"


def BLINK():
    """Return ANSI escape for text blink.
    """
    return "\033[05m"


def typing_effect(words):
    for char in words:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()

def PLAYER_MIN_DAMAGE():
    return 5


def PLAYER_START_DAMAGE():
    return 20


def FOE_MAX_DAMAGE():
    return 10


def PLAYER_START_HP():
    return 20


def FOE_MAX_HP():
    return 10


def INITIAL_HIT_RATE():
    return 75  # this means 75% chance of hitting opponent


def FOE_HIT_RATE():
    return 60


def INITIAL_LOCATION():
    return [0, 0]


def BOSS_LOCATION():
    return [24, 24]


def make_map():
    return [(y, x) for y in range(25) for x in range(25)]


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
    name = input("What's your name, explorer?: ")
    class_description()
    player_class = input("What class will you choose? Enter number for class: ")
    player = {"name": name,
              "class": class_choice(player_class),
              "HP": PLAYER_START_HP(),
              "max_HP": PLAYER_START_HP(),
              "hit_rate": INITIAL_HIT_RATE(),
              "XP": 0,
              "min_damage": PLAYER_MIN_DAMAGE(),
              "max_damage": PLAYER_START_DAMAGE(),
              "location": INITIAL_LOCATION()}
    class_stats(player)
    return player


