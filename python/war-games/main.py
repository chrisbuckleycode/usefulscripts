import random
import calendar
import os

class Country:
    def __init__(self, name, budget, manpower, land_forces, air_forces, navy):
        self.name = name
        self.budget = budget
        self.manpower = manpower
        self.land_forces = land_forces
        self.air_forces = air_forces
        self.navy = navy

    def update_statistics(self, multipliers):
        self.budget *= multipliers["budget"]
        self.manpower *= multipliers["manpower"]
        self.land_forces *= multipliers["land_forces"]
        self.air_forces *= multipliers["air_forces"]
        self.navy *= multipliers["navy"]

class ChanceCard:
    def __init__(self, message, user_choice_required, stat1_effect, stat2_effect=None):
        self.message = message
        self.user_choice_required = user_choice_required
        self.stat1_effect = stat1_effect
        self.stat2_effect = stat2_effect

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_statistics(player_country, other_country, month, year):
    clear_screen()
    month_name = calendar.month_abbr[month]
    print(f"Current Date: {month_name} {year}")
    print(f"You are playing as {player_country.name}\n")
    print("Statistic (unit), Your Country, Opponent Country")
    print("-----------------------------------")
    print(f"Military Budget (billions), {player_country.budget:.1f}, {other_country.budget:.1f}")
    print(f"Military manpower (thousands), {player_country.manpower:.1f}, {other_country.manpower:.1f}")
    print(f"Land forces (thousands), {player_country.land_forces:.2f}, {other_country.land_forces:.2f}")
    print(f"Air forces (thousands), {player_country.air_forces:.2f}, {other_country.air_forces:.2f}")
    print(f"Navy (thousands), {player_country.navy:.2f}, {other_country.navy:.2f}\n")

def create_chance_deck():
    deck = [
        ChanceCard("Tax bonanza! Military Budget boosted by 1%", 0, lambda c: setattr(c, 'budget', c.budget * 1.01)),
        ChanceCard("Old army equipment must be retired! Land forces reduced by 2%", 0, lambda c: setattr(c, 'land_forces', c.land_forces * 0.98)),
        ChanceCard("250 new military units! Choose Air forces or Navy", 1,
                   lambda c: setattr(c, 'air_forces', c.air_forces + 0.25),
                   lambda c: setattr(c, 'navy', c.navy + 0.25)),
        ChanceCard("Necessary personnel investment! Spend 0.5 billion on 1000 new personnel", 0,
                   lambda c: setattr(c, 'budget', c.budget - 0.5),
                   lambda c: setattr(c, 'manpower', c.manpower + 1))
    ]
    return deck * 5  # Create 5 copies of each card to make a 20-card deck

def draw_chance_card(deck):
    card = random.choice(deck)
    deck.remove(card)
    deck.append(card)  # Put the card at the bottom of the deck
    return card

def apply_chance_card(card, country, is_player=True):
    messages = []
    if card.user_choice_required and is_player:
        print(f"\nChance Event: {card.message}")
        choice = input("Choose (1) for the first option or (2) for the second option: ")
        if choice not in ['1', '2']:
            choice = random.choice(['1', '2'])
            messages.append(f"Invalid input. A random choice ({choice}) was made for you.")
        
        if choice == '1':
            card.stat1_effect(country)
        else:  # choice == '2'
            card.stat2_effect(country)
    else:
        if is_player:
            messages.append(f"\nPlayer Chance Event: {card.message}")
        else:
            messages.append(f"\n{country.name} Chance Event: {card.message}")
        
        if card.user_choice_required:
            # For opponent, make a random choice
            choice = random.choice(['1', '2'])
            messages.append(f"{country.name} chose option {choice}")
            if choice == '1':
                card.stat1_effect(country)
            else:
                card.stat2_effect(country)
        else:
            card.stat1_effect(country)
            if card.stat2_effect:
                card.stat2_effect(country)
        
        if not is_player:
            messages.append(f"Effect applied to {country.name}")
    
    return messages

def main():
    player_choice = input("Choose your country (USA or China, or enter the first character of the country): ").upper()
    if player_choice == "U" or player_choice == "USA":
        player_country = Country("USA", 800, 1358, 5.652, 13.175, 0.460)
        other_country = Country("China", 700, 2035, 5.750, 4.630, 0.742)
        player_deck = create_chance_deck()
        opponent_deck = create_chance_deck()
    elif player_choice == "C" or player_choice == "CHINA":
        player_country = Country("China", 700, 2035, 5.750, 4.630, 0.742)
        other_country = Country("USA", 800, 1358, 5.652, 13.175, 0.460)
        player_deck = create_chance_deck()
        opponent_deck = create_chance_deck()
    else:
        print("Invalid country choice. Exiting the game.")
        return

    month = 1
    year = 2025

    player_multipliers = {
        "budget": 1.0004,
        "manpower": 1.0004,
        "land_forces": 1.0004,
        "air_forces": 1.0001,
        "navy": 1.0002
    }

    other_multipliers = {
        "budget": 1.0015,
        "manpower": 1.0005,
        "land_forces": 1.0005,
        "air_forces": 1.0050,
        "navy": 1.0002
    }

    while True:
        display_statistics(player_country, other_country, month, year)

        choice = input("\n(q) to quit\n(p) to proceed with the next game loop\n(m) to modify multipliers\n(d) to dispose Military Budget\nYour choice: ")
        print("-----------------------------------")
        if choice == 'q':
            print("Exiting the game. Final statistics:")
            display_statistics(player_country, other_country, month, year)
            break
        elif choice == 'm':
            for key in player_multipliers:
                current_value = player_multipliers[key]
                new_value = input(f"Enter the new multiplier for {key} for your country (current: [{current_value}], press Enter to retain current value): ")
                if new_value:
                    player_multipliers[key] = float(new_value)

            for key in other_multipliers:
                current_value = other_multipliers[key]
                new_value = input(f"Enter the new multiplier for {key} for the opponent country (current: [{current_value}], press Enter to retain current value): ")
                if new_value:
                    other_multipliers[key] = float(new_value)
        elif choice == 'd':
            amount = float(input("Enter the amount (in billions) to reduce the Military Budget by: "))
            player_country.budget -= amount
        elif choice == 'p' or choice == '':
            player_country.update_statistics(player_multipliers)
            other_country.update_statistics(other_multipliers)

            # Draw and apply a chance card for the player
            player_card = draw_chance_card(player_deck)
            player_messages = apply_chance_card(player_card, player_country, is_player=True)

            # Draw and apply a chance card for the opponent
            opponent_card = draw_chance_card(opponent_deck)
            opponent_messages = apply_chance_card(opponent_card, other_country, is_player=False)

            # Display all messages
            for message in player_messages + opponent_messages:
                print(message)
            
            # Add the "Press Enter to continue..." message after all chance event messages
            input("\nPress Enter to continue...")

            # Update month and year
            month += 1
            if month > 12:
                month = 1
                year += 1

if __name__ == "__main__":
    main()