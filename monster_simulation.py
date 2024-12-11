# Name: Johnathan Sullivan
# Date: 11/10/2024
# Project Title: The Final Project

# Program Description: The world of Eryndor Battle Game Part Two Monster Simulation


#Import Random



import random

# Define function for run_simulation_for_class(class_name, num_battles=500):
def run_simulation_for_class(class_name, num_battles=500):
    # This runs multiple simulations for a given class
    DODGE_INCREMENT = 2.5 / 100

    character_classes = {
        "Fighter": (80, (5, 10), 0.05 + (10 * DODGE_INCREMENT)),
        "Wizard": (50, (8, 15), 0.05 + (14 * DODGE_INCREMENT)),
        "Rogue": (65, (7, 12), 0.05 + (17 * DODGE_INCREMENT)),
        "Cleric": (70, (6, 11), 0.05 + (12 * DODGE_INCREMENT)),
        "Barbarian": (85, (4, 12), 0.05 + (7 * DODGE_INCREMENT))
    }

    health, damage_range, dodge_chance = character_classes[class_name]
    player_wins = 0

    for _ in range(num_battles):
        winner = simulate_battle(health, damage_range, dodge_chance)
        if winner == "Player":
            player_wins += 1

    return player_wins

# Define the simulate_battle(player_health, player_damage_range, player_dodge_chance): per clients request
def simulate_battle(player_health, player_damage_range, player_dodge_chance):
    monster_health = 60
    monster_damage_range = (3, 11)
    monster_dodge_chance = 0.15

    winner = None

    while winner is None:
        damage_to_monster = turn_damage(*player_damage_range)
        if dodge_check(monster_dodge_chance):
            damage_to_monster //= 2
        monster_health -= damage_to_monster

        winner = check_for_winner(player_health, monster_health)
        if winner:
            return winner

        damage_to_player = turn_damage(*monster_damage_range)
        if dodge_check(player_dodge_chance):
            damage_to_player = 0
        player_health -= damage_to_player

        winner = check_for_winner(player_health, monster_health)

    return winner

# Define the function turn damage (x , y) per clients request
def turn_damage(x, y):
    return random.randint(x, y)

# Define the function doge_check(chance_doge) per clients request
def dodge_check(chance_dodge):
    return random.random() < chance_dodge

# Define the check_winner (player_health, monster_health): per clients request
def check_for_winner(player_health, monster_health):
    if player_health <= 0:
        return "Monster"
    elif monster_health <= 0:
        return "Player"
    return None

# Define the function run_all_simulations():
def run_all_simulations():
    character_classes = ["Fighter", "Wizard", "Rogue", "Cleric", "Barbarian"]
    num_battles = 500
    class_win_counts = {}

    for class_name in character_classes:
        wins = run_simulation_for_class(class_name, num_battles)
        class_win_counts[class_name] = wins
        print(f"{class_name} won {wins} battles out of {num_battles}.")

    most_successful_class = max(class_win_counts, key=class_win_counts.get)
    print(f"\nThe most successful class is {most_successful_class}!")


if __name__ == "__main__":
    run_all_simulations()