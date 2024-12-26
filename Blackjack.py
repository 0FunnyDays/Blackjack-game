import random

# Card Ranks
ranking = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

# Cards value
card_val = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}


def deal_card():
    """Returns a random card rank from the deck"""
    rank = random.choice(ranking)
    return rank


# Function to calculate the score of a hand
def calculate_score(cards):
    """Calculates the score from the list of cards"""
    score = sum(card_val[card] for card in cards)

    # Count how many Aces are in the hand
    ace_count = cards.count('A')

    while score <= 21 and ace_count > 0:
        score += 10  # Convert an Ace from 1 to 11
        ace_count -= 1

    return score


def compare(u_score, c_score):
    """Compares user and computer scores to determine the winner"""
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, opponent has Blackjack"
    elif u_score == 0:
        return "Win with a Blackjack"
    elif u_score > 21:
        return "You went over 21. You lose"
    elif c_score > 21:
        return "Opponent went over 21. You win"
    elif u_score > c_score:
        return "You win"
    else:
        return "You lose"


# Main game loop
def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Deal two cards to the user and the computer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        # The computer draws cards until its score is 17 or higher
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    user_score = calculate_score(user_cards)  # Recalculate the final user score after all cards
    computer_score = calculate_score(computer_cards)  # Recalculate the final computer score

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


# Main loop for replaying the game
while True:
    play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    if play_again == 'y':
        print("\n" * 20)  # Clears the screen
        play_game()
    elif play_again == 'n':
        print("Thanks for playing!")
        break
    else:
        print("Invalid input, please type 'y' to play or 'n' to quit.")
