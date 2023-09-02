import random

# Vytvoření balíčku karet
suits = ['Srdce', 'Káry', 'Piky', 'Kříže']
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9']
deck = [(value, suit) for suit in suits for value in values]

# Odstranění všech desítek a obrázkových karet (J, Q, K)
deck = [card for card in deck if card[0] != '10' and card[0] not in ['J', 'Q', 'K']]

# Funkce pro výpočet bodů pro tři karty
def calculate_score(cards):
    values_dict = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    total_score = sum([values_dict[card[0]] for card in cards])
    return total_score % 10

# Funkce pro porovnání karet podle pravidel
def compare_cards(cards1, cards2):
    score1 = calculate_score(cards1)
    score2 = calculate_score(cards2)

    if score1 != score2:
        return score1 - score2

    # Stejné skóre, porovnání nejvyšších karet
    max_card1 = max(cards1, key=lambda card: (values.index(card[0]), suits.index(card[1])))
    max_card2 = max(cards2, key=lambda card: (values.index(card[0]), suits.index(card[1])))

    return (values.index(max_card1[0]), suits.index(max_card1[1])) - (values.index(max_card2[0]), suits.index(max_card2[1]))

# Funkce pro vytvoření a rozdání karet hráčům
def deal_cards(num_players):
    random.shuffle(deck)
    hands = [deck[i:i+3] for i in range(0, num_players * 3, 3)]
    return hands

# Hlavní funkce
def main():
    num_players = int(input("Zadejte počet hráčů (maximálně 6): "))
    if num_players < 2 or num_players > 6:
        print("Neplatný počet hráčů.")
        return

    hands = deal_cards(num_players)

    for i, hand in enumerate(hands):
        print(f"Hráč {i+1}: {[f'{card[0]} {card[1]}' for card in hand]}")

    winner = max(enumerate(hands), key=lambda x: (calculate_score(x[1]), max([(values.index(card[0]), suits.index(card[1])) for card in x[1]])))
    print(f"Hráč {winner[0] + 1} vyhrál se skóre {calculate_score(winner[1])}")

if __name__ == "__main__":
    main()
