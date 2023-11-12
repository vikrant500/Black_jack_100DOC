import random
from art_black_jack import logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)

    return card


def calculate_score(dealt_cards):
    if sum(dealt_cards) == 21 and len(dealt_cards) == 2:
        return 0  # 0 means blackjack in the code

    if 11 in dealt_cards and sum(dealt_cards) > 21:
        dealt_cards.remove(11)
        dealt_cards.append(1)

    return sum(dealt_cards)


def compare(user_score, computer_score):
    # Bug fix. If you and the computer are both over 21 , you lose.
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose"

    if user_score == computer_score:
        return "Draw "
    elif computer_score == 0:
        return "Lose, opponent has Blackjack "
    elif user_score == 0:
        return "Win with a Blackjack "
    elif user_score > 21:
        return "You went over. You lose "
    elif computer_score > 21:
        return "Opponent went over. You win "
    elif user_score > computer_score:
        return "You win "
    else:
        return "You lose "


def play_game():
    user_cards = []
    computer_cards = []
    your_turn_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # your turn

    while not your_turn_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            your_turn_over = True

        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")

            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                your_turn_over = True

    # computer's turn

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print(logo)
    play_game()