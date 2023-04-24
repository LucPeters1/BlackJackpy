import random

# The card class represents a single playing card, with a suit and a value.
class Card:
    # Initializes a Card object with the given suit and value.
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    # Returns a string representation of the Card object in the format "value of suit".
    def __str__(self):
        return f"{self.value} of {self.suit}"

    # Returns the point value of the Card according to the Blackjack rules.
    def get_point_value(self):
        if self.value == "A":
            return 11
        elif self.value in ["K", "Q", "J"]:
            return 10
        else:
            return int(self.value)

# Returns a list containing a full deck of 52 unique cards
def create_deck():
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    return [Card(suit, value) for suit in suits for value in values]

# Calculates and returns the point value of the given hand (a list of Card Objects)
def calculate_points(hand):
    points = sum(card.get_point_value() for card in hand)
    aces = sum(1 for card in hand if card.value == "A")
    
    while points > 21 and aces > 0:
        points -= 10
        aces -= 1

    return points

# Plays a single round of Blackjack using the given deck. Returns True if the player wins, and False otherwise (ties).
def play_round(deck):
    user_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    print("Your hand:")
    for card in user_hand:
        print(card)
    print(f"Points: {calculate_points(user_hand)}")

    while True:
        action = input("Do you want to (H)it or (S)tand? ").lower()
        if action == "h":
            user_hand.append(deck.pop())
            print(f"\nNew card: {user_hand[-1]}")
            print(f"Points: {calculate_points(user_hand)}")
            
            if calculate_points(user_hand) > 21:
                print("Bust! You lost.")
                return False
        elif action == "s":
            while calculate_points(dealer_hand) < 17:
                dealer_hand.append(deck.pop())
            
            user_points = calculate_points(user_hand)
            dealer_points = calculate_points(dealer_hand)
            print(f"\nDealer's hand: {dealer_points} points")

            if dealer_points > 21 or user_points > dealer_points:
                print("You won!")
                return True
            elif dealer_points == user_points:
                print("It's a tie!")
                return False
            else:
                print("You lost.")
                return False
        else:
            print("Invalid input. Please enter H or S.")

# Main function that starts the game. It prompts the user to enter the number of decks and rounds, then plays the game accordingly.
def play_blackjack():
    num_decks = int(input("Enter the number of decks you want to use: "))
    num_rounds = int(input("Enter the number of rounds you want to play: "))
    wins = 0

    for round_num in range(num_rounds):
        print(f"\nRound {round_num + 1}/{num_rounds}")
        deck = create_deck() * num_decks
        random.shuffle(deck)
        
        if play_round(deck):
            wins += 1
        print(f"Your current wins: {wins}/{round_num + 1}")

    print(f"\nGame over. Your final wins: {wins}/{num_rounds}")

if __name__ == "__main__":
    play_blackjack()
