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
