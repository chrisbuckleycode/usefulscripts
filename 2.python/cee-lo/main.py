import random
import time
import os

def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def roll_dice():
    return [random.randint(1, 6) for _ in range(3)]

def evaluate_roll(roll):
    roll.sort()
    if roll == [4, 5, 6]:
        return "456", 7  # Instant win, but lower than triples
    elif roll[0] == roll[1] == roll[2]:
        return "Triple", roll[0] + 7  # Triples are instant wins, scored 8-13
    elif roll[0] == roll[1] or roll[1] == roll[2]:
        if roll[0] == roll[1]:
            point = roll[2]
        else:
            point = roll[0]
        if point == 6:
            return "Point 6", 6  # Instant win, but lower than 456 and triples
        elif point == 1:
            return "Point 1", 0  # Instant loss
        else:
            return f"Point {point}", point  # Regular points
    elif roll == [1, 2, 3]:
        return "123", -1  # Instant loss, but distinguish from Point 1
    else:
        return "No score", -2  # Indeterminate, needs re-roll

def display_roll(player, roll):
    print(f"{player} rolled: {roll[0]}, {roll[1]}, {roll[2]}")

def display_leaderboard(player_wins, cpu_wins):
    print("\n----- LEADERBOARD -----")
    print(f"Player: {player_wins} wins")
    print(f"CPU   : {cpu_wins} wins")
    print("-----------------------")

def play_ceelo():
    player_wins = 0
    cpu_wins = 0
    
    while True:
        clear_screen()
        input("Press Enter to roll dice...")
        player_roll = roll_dice()
        display_roll("You", player_roll)
        player_result, player_score = evaluate_roll(player_roll)
        print(f"Your result: {player_result}")
        
        print("\nNow it's the CPU's turn.")
        time.sleep(1)
        input("Press Enter to let CPU roll dice...")
        cpu_roll = roll_dice()
        display_roll("CPU", cpu_roll)
        cpu_result, cpu_score = evaluate_roll(cpu_roll)
        print(f"CPU result: {cpu_result}")
        
        if player_score == -2 and cpu_score == -2:
            print("\nBoth rolls are indeterminate. Re-rolling...")
            time.sleep(2)
            continue
        elif player_score == -2:
            print("\nCPU wins due to your indeterminate roll.")
            cpu_wins += 1
        elif cpu_score == -2:
            print("\nCongratulations! You win due to CPU's indeterminate roll.")
            player_wins += 1
        elif player_score > cpu_score:
            print("\nCongratulations! You win!")
            player_wins += 1
        elif cpu_score > player_score:
            print("\nCPU wins. Better luck next time!")
            cpu_wins += 1
        else:
            print("\nIt's a tie! Roll again.")
            time.sleep(2)
            continue
        
        display_leaderboard(player_wins, cpu_wins)
        
        play_again = input("\nDo you want to play again? (yes/no, or just press Enter for yes): ").lower()
        if play_again not in ['yes', 'y', '']:
            print("Thanks for playing Cee-lo!")
            break

if __name__ == "__main__":
    clear_screen()
    print("Welcome to Cee-lo!")
    print("Rules: 4-5-6 is the highest, followed by triples, then point value. 1-2-3 is the lowest.")
    print("For points, the odd die determines the value, with the pair as a tiebreaker.")
    print("The game is played without a bank, winner takes all.")
    print("\nPress Enter to start the game...")
    input()
    play_ceelo()