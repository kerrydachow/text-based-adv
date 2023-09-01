import sys
from time import sleep


# CONSTANTS
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


def typing_effect(words):
    """Print a string character by character with a delay.

    :param words: any string
    :precondition: words must be a string
    :postcondition: print a string character by character with a delay between every character
    :return: None
    """
    for char in words:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()