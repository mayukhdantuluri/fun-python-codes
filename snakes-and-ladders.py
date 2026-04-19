import random
import time

print ("Welcome to Snakes and Ladders.")

while True:
    try:
        num_players = int(input("Enter the number of players (2-10): ").strip())
        time.sleep(0.75)
        if 2 <= num_players <= 10:
            break
        elif num_players < 2:
            print("Not enough players. You need at least 2 players to play.")
            time.sleep(0.5)
        elif num_players > 10:
            print("Too many players. Maximum of 10 players allowed.")
            time.sleep(0.5)
    except ValueError:
        time.sleep(0.5)
        print("Please enter a valid integer.")

player_names = []
for i in range(num_players):
    name = input(f"Player {i + 1}'s name: ")
    player_names.append(name)
    time.sleep(0.5)

for i, name in enumerate(player_names, 1):
    print(f"Player {i}: {name}")
time.sleep(1)

starting_player = random.randint(1, num_players)
print("Order of play will go up by player #. Now picking starting player...")
time.sleep(1)
print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)
print(f"Starting player is: Player {starting_player} ({player_names[starting_player - 1]})")
time.sleep(2)

def roll_dice():
    return random.randint(1, 6)

snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

print("Snakes & Ladders Board Setup:")
print("Snakes: 16->6, 47->26, 49->11, 56->53, 62->19, 64->60, 87->24, 93->73, 95->75, 98->78")
print("Ladders: 1->38, 4->14, 9->31, 21->42, 28->84, 36->44, 51->67, 71->91, 80->100")

def move_player(player_name, player_position, roll):
    new_position = player_position + roll
    print(f"{player_name} rolled a {roll}.")
    if new_position > 100:
        new_position = player_position
        time.sleep(0.75)
        print(f"{player_name} cannot move beyond 100. Staying at {player_position}.")
    elif new_position in snakes:
        time.sleep(0.75)
        print(f"{player_name} landed on a snake's head at {new_position}. Sliding down to {snakes[new_position]}.")
        new_position = snakes[new_position]
    elif new_position in ladders:
        time.sleep(0.75)
        print(f"{player_name} landed at the base of a ladder at {new_position}. Climbing up to {ladders[new_position]}.")
        new_position = ladders[new_position]
    else:
        time.sleep(0.75)
        print(f"{player_name} moved to {new_position}.")
    return new_position

def play_game():
    player_positions = [0] * num_players
    current_player = starting_player - 1

    while True:
        player_num = current_player + 1
        player_name = player_names[current_player]
        input(f"{player_name}'s turn. Press Enter to roll the dice...")
        roll = roll_dice()
        player_positions[current_player] = move_player(player_name, player_positions[current_player], roll)
        time.sleep(1)

        if player_positions[current_player] == 100:
            print(f"{player_name} made it to 100 and wins the game.")
            rankings = []
            for idx, pos in enumerate(player_positions):
                rankings.append((pos, player_names[idx], idx))

            rankings_sorted = sorted(rankings, key=lambda x: x[0], reverse=True)

            winner_idx = current_player
            for i, item in enumerate(rankings_sorted):
                if item[2] == winner_idx:
                    winner_item = rankings_sorted.pop(i)
                    rankings_sorted.insert(0, winner_item)
                    break

            print("Final ranking:")
            for place, (pos, name, idx) in enumerate(rankings_sorted, start=1):
                if idx == winner_idx:
                    print(f"{place}. {name} = 100 (Winner)")
                else:
                    print(f"{place}. {name} = {pos}")
            break

        current_player = (current_player + 1) % num_players

play_game()