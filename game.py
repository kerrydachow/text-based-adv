"""
Name: Kerry Chow[A01245034]
Name: Tomo Kaneko[A01250261]
Date:
"""
import itertools
import random
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


def PURPLE():
    """Return ANSI escape for text color purple.
    """
    return "\033[35m"


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


def PLAYER_UNSUCCESSFUL_FLEE_RATE():
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


def MONSTER_DESCRIPTION_AMOUNT():
    return 2


def EVALUATE_MONSTER_HARD_HP():
    return 15


def EVALUATE_MONSTER_HARD_DAMAGE():
    return 10


def EVALUATE_MONSTER_MEDIUM_DAMAGE():
    return 8


def EVALUATE_MONSTER_HARD_HIT_RATE():
    return 50


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


def MAX_FLEE_RATE():
    return 100


def MAX_FLEE_DAMAGE():
    return 15


def MAX_ROLL_NUMBER():
    return 100


def FLEE_RATE():
    return 20


def PLAYER_ICON():
    return "🧙"  # for now


def BOSS_ICON():
    return "👹"


def BOARD_DIMENSION():
    return 25


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


def ENDING_MESSAGE():
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
    """Make board for game

    :param:
    :precondition:
    :postcondition: create list of tuple to represent board
    :return: a dictionary to represent game board
    """
    return [(y, x) for y in range(dimension) for x in range(dimension)]


def print_map(dimension, board, player):
    """Print game board to user

    :param board: a list with tuple item
    :param player: a dictionary
    :param dimension: a integer
    :precondition: board must be a dictionary representing game board
    :precondition: player must be a dictionary representing player
    :postcondition: print game board to the user
    :postcondition: print player icon on board corresponding to player location
    :postcondition: print boss icon on board corresponding to boss location
    :return: None
    """
    key_counter = 0
    for x_axis in range(dimension):
        for y_axis in range(dimension):
            if board[key_counter] == tuple(player["location"]):
                print(BLINK() + PLAYER_ICON() + END() + " ", end="")
            elif board[key_counter] == tuple(BOSS_LOCATION()):
                print(BOSS_ICON(), end="")
            else:
                print("[ ]", end="")
            key_counter += 1
        print()


def class_description():
    print("\nClasses\n\n"
          "%s0%s %sSorcerer%s:\nSorcerers uses magic to attack."
          "\nTheir damage is amplified, but not the most accurate!\n\n"
          "%s1%s %sThief%s:\nThieves lurk through the shadows with striking with deadly accuracy."
          "\nTheir accuracy is near-perfect, but lack the strength to damage!\n\n"
          "%s2%s %sAmazon%s:\nAmazons specialize in archery, swordplay, and a bit of magic."
          "\nAmazon's are the most well-balanced class!\n\n"
          "%s3%s %sFighter%s:\nFighters have incredible yet, uncontrollable strength. "
          "\nTheir uncontrollable strength can easily dissipate weak monsters!\n"
          % (RED(), END(), UNDERLINE(), END(), RED(), END(), UNDERLINE(), END(), RED(), END(), UNDERLINE(), END(),
             RED(), END(), UNDERLINE(), END()))


def class_stats(player: dict):  # amazon no stat changes
    """Add unique status for each class

    :param player: a dictionary
    :precondition: player must be a dictionary with key "master_class", "min_damage", "max_damage", "hit_rate"
    :postcondition: increment key values for each unique class
    :return: None
    """
    if player["master_class"] == "Sorcerer":
        player["max_damage"] += 10  # low chance of hit high damage
        player["min_damage"] += 5
        player["hit_rate"] -= 15
    elif player["master_class"] == "Thief":
        player["max_damage"] -= 5  # high hit rate low damage
        player["min_damage"] += 2
        player["hit_rate"] += 10
    elif player["master_class"] == "Fighter":
        player["max_damage"] += 10  # high damage low chance of deadly hit
        player["min_damage"] -= 4
    elif player["master_class"] == "Hidden Lord":
        player["max_damage"] += 80
        player["HP"] += 50  # test
        player["max_HP"] += 50


def class_level(player: dict) -> list:
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
    list_increment = player["level"]
    player["sub_class"] = class_level(player)[-1 + list_increment]
    return player["sub_class"]


def class_choice():
    class_list = enumerate(("Sorcerer", "Thief", "Amazon", "Fighter"))
    valid_class_num = ["0", "1", "2", "3", "1337"]
    while True:
        player_class = input("What class will you choose? Enter number for class: ")
        if player_class in valid_class_num:
            for jobs in class_list:
                if player_class == str(jobs[0]):
                    return jobs[1]
                elif player_class == "1337":
                    return "Hidden Lord"
        else:
            print("\nPlease input valid input\n")


def make_player():
    """Create player

    :postcondition: create a dictionary representing game player
    :return: a dictionary representing player
    """
    name = input("What's your name, explorer?: ")
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
              "max_damage": PLAYER_START_DAMAGE(),
              "location": PLAYER_START_LOCATION()}
    class_stats(player)
    player_sub_class(player)
    return player


def get_player_move():
    """Get players direction

    :postcondition: return player_direction if valid else print Invalid message
    :return: a string representing players moving direction
    """
    print("\nInstructions:\n %s0%s : Up \n %s1%s : Down \n %s2%s : Left\n %s3%s : Right\n %sQ%s : Quit\n"
          % (RED(), END(), RED(), END(), RED(), END(), RED(), END(), YELLOW(), END()))
    valid_user_input = ["0", "1", "2", "3", "q", "Q", "h", "H"]
    while True:
        player_direction = input("Which direction will you go? ")
        if player_direction in valid_user_input:
            return player_direction
        else:
            print("\nInvalid Input\nPlease Try Again\n")


def player_destination(direction: str, player: dict) -> tuple:
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


def validate_move(new_location: tuple, board: list) -> bool:
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


def move_player(direction: str, player: dict):
    """Move the player on game board

    :param direction: a string
    :param player: a dictionary
    :precondition: direction must be a string number of 0, 1, 2, 3
    :precondition: character must be a dictionary representing player
    :postcondition: modify character['location'] value according to direction
    :return: None
    """
    if direction == "0":
        player["location"][0] -= 1
    elif direction == "1":
        player["location"][0] += 1
    elif direction == "2":
        player["location"][1] -= 1
    elif direction == "3":
        player["location"][1] += 1


def check_for_monster(player: dict):
    """Check if there is monster

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


def generate_monster(player):
    """Create monster

    :postcondition: create a monster dictionary for combat
    :return: a dictionary representing a monster
    """
    monster_name = random.choice(["Dragon", "Kobold", "Fenrir", "Loki", "Surtr"])
    monster_activity = random.choice(["staring at you", "snarling at you", "stalking you", "ready to pounce at you"])
    monster_description = ["Humongous", "Murderous", "Rabid", "Psycho", "Hostile"]
    monster_state = list(itertools.permutations(monster_description, MONSTER_DESCRIPTION_AMOUNT()))  # 2 for 2 monster descriptions.

    def filter_moves(moves):
        monster_moves_level_1 = ["Bite", "Chomp", "Body Slam", "Scratch"]
        if moves in monster_moves_level_1:
            return True
        else:
            return False

    def generate_foe_moves_based_on_player_level():
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
    """Display monster difficulty

    :param monster: a dictionary
    :precondition: monster must be a dictionary representing game monster
    :postcondition: display monster difficulty to user
    :return: None
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
    """Flee from foe

    :param player: a dictionary
    :precondition: player must be a dictionary representing game player
    :postcondition: take damage with 20% chance and print message
                    else print message
    :return: None
    """
    if random.randint(1, MAX_FLEE_RATE()) <= PLAYER_UNSUCCESSFUL_FLEE_RATE():
        flee_damage = random.randint(1, MAX_FLEE_DAMAGE())
        player["HP"] -= flee_damage
        print(f"You fled but took a stab to the back {flee_damage}")
    else:
        print("You fled successfully!")


def monster_flee(player: dict) -> bool:
    """Flee for monster

    :param:
    :precondition:
    :postcondition:
    :return:
    """
    if random.randint(1, MAX_FLEE_RATE()) <= FLEE_RATE() and player["location"] != BOSS_LOCATION():
        return True
    else:
        return False


def player_heal(player: dict):
    """Heal player HP

    :param player: a dictionary
    :precondition: player must be a dictionary representing game player
    :postcondition: increase player["HP"] to not exceed player["max_HP"]
    :return: None
    """
    if player["HP"] < player["max_HP"]:
        player["HP"] = min(player["HP"] + PLAYER_HP_HEAL(), player["max_HP"])
        print(f"\nYou have recovered HP \nYour new HP is {player['HP']}\n")


def player_restart():
    while True:
        restart = input("\nWould you like to restart?\n%sY%s for Yes\n%sN%s for No\n\n"
                        "What will you do? (Enter corresponding letter to pick your action.) "
                    % (RED(), END(), RED(), END()))
        if restart.lower() == "y":
            game()
            exit()
        elif restart.lower() == "n":
            print("Good bye. Good luck on your adventure next time!")
            exit()
        else:
            print("Invalid input, please input y or n")

def is_player_dead(player: dict):
    if player["HP"] <= 0:
        print("\nYou have failed your mission.\n")
        player_restart()


def roll_for_first_hit(player: dict, foe: dict) -> bool:
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
    if random.randint(1, MAX_HIT_RATE()) <= game_chara["hit_rate"]:
        return True
    else:
        return False


def combat_moves_list(player):
    if player["master_class"] == "Sorcerer":
        return list(enumerate(
            ["Fire Ball", "Icicle Attack", "Magic Missile", "Flee"],
            1))  # I used list in order to use it in combat options.
    elif player["master_class"] == "Thief":
        return list(enumerate(["Throw Ninja Star", "Dagger Stab", "Punch", "Flee"], 1))
    elif player["master_class"] == "Amazon":
        return list(enumerate(["Arrow Shot", "Sword Slash", "Fire Ball", "Flee"], 1))
    elif player["master_class"] == "Fighter":
        return list(enumerate(["Power Punch", "Side Pick", "Body Slam", "Flee"], 1))
    elif player["master_class"] == "Hidden Lord":
        return list(enumerate(["Lightning Punch", "Fire Storm", "Darkness Beam", "Flee"], 1))


def attack(attacker, receiver):
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
    attack_moves = combat_moves_list(player)
    if player["location"] == BOSS_LOCATION():
        attack_moves.pop()
    for move in attack_moves:
        print(RED() + f"{move[0]}" + END() + " : " + move[1] + "\n", end="")
    while True:
        player_move = input(
            "\nWhat will you do? (Enter corresponding number to pick your action.) ")
        for move in attack_moves:
            if player_move == str(move[0]):
                return move[1]
        else:
            print("\nInvalid Input")


def validate_combat_option(player, foe, move, who_strike_first):
    if move == "Flee":
        player_flee(player)
    else:
        player["attack_move"] = move
        combat_round(player, foe, who_strike_first)


def check_experience(player):
    if player["XP"] == PLAYER_EXPERIENCE_LEVEL2() or player["XP"] == PLAYER_EXPERIENCE_LEVEL3():
        return True
    else:
        return False


def character_levelup(player):
    player["level"] += PLAYER_LEVEL()
    player_sub_class(player)
    if player["hit_rate"] < MAX_HIT_RATE():
        player["hit_rate"] += PLAYER_HIT_RATE_INCREASE()
    player["min_damage"] += PLAYER_MIN_DAMAGE_INCREASE()
    player["max_damage"] += PLAYER_MAX_DAMAGE_INCREASE()
    player["max_HP"] += PLAYER_HP_INCREASE()
    player["HP"] = player["max_HP"]  # When player levels up, HP will be fully restored
    typing_effect(f"\nYou have leveled up!\n"
                  f"\nYou are now Level {player['level']}\n"
                  f"\nYou have job advanced to %s{player['sub_class']}!%s\n" % (RED(), END()))
    sleep(1)
    typing_effect(f"\n Your HP increased by {PLAYER_HIT_RATE_INCREASE()}"
                  f"\n Your accuracy increased by {PLAYER_HIT_RATE_INCREASE()}"
                  f"\n Your minimum damage increased by {PLAYER_MIN_DAMAGE_INCREASE()}"
                  f"\n Your maximum damage increased by {PLAYER_MAX_DAMAGE_INCREASE()}"
                  f"\n And you have fully recovered your HP!\n")
    print(f"\nMaster Class: {player['master_class']}"
          f"\nDamage Range: {player['min_damage']} - {player['max_damage']}"
          f"\nAccuracy: {player['hit_rate']}%")


def after_combat(player):
    if not player["location"] == BOSS_LOCATION():
        player["XP"] += PLAYER_EXPERIENCE_GAIN()
        typing_effect(f"You have gained {PLAYER_EXPERIENCE_GAIN()} XP!\nYour current XP is {player['XP']}\n")
        sleep(1)
        if check_experience(player):
            character_levelup(player)


def combat(player, foe, who_strike_first):
    move = combat_options(player)
    validate_combat_option(player, foe, move, who_strike_first)


def player_reach_boss(player):
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
        typing_effect(f"\nYou have reached Kindred(HP: {boss['HP']}), the mighty Dragon who blocks the gates to Heaven\n")
        who_strike_first = roll_for_first_hit(player, boss)
        combat(player, boss, who_strike_first)
        if boss["HP"] <= 0:
            typing_effect("Congratulations! You have defeated Kindred!\n")
            print(ENDING_MESSAGE())
            player_restart()


def game():
    """Play game
    """
    character = make_player()
    board = make_map(BOARD_DIMENSION())
    achieve_goal = False
    print_map(BOARD_DIMENSION(), board, character)
    print(f"Name: {character['name']} | "
          f"HP: {character['HP']} | "
          f"Class: {character['sub_class']} | "
          f"Location: {character['location']} | "
          f"Level: {character['level']} "
          f"\n\nMaster Class: {character['master_class']}"
          f"\nDamage Range: {character['min_damage']} - {character['max_damage']}"
          f"\nAccuracy: {character['hit_rate']}%")
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
                  f"Location: {character['location']}")
            if check_for_monster(character):
                foe = generate_monster(character)
                evaluate_monster_difficulty(foe)
                player_attack_first = roll_for_first_hit(character, foe)
                combat(character, foe, player_attack_first)
            else:
                player_heal(character)
                player_reach_boss(character)
        else:
            print("You can't move in that direction.")
            sleep(2)


def main():
    """Execute game
    """
    game()


if __name__ == "__main__":
    main()
