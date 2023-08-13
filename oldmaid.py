import random

def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [(rank, suit) for rank in ranks for suit in suits]
    deck.append(('Old Maid', 'Joker'))
    return deck

def shuffle_deck(deck):
    random.shuffle(deck)

def deal_cards(deck, players):
    num_players = len(players)
    cards_per_player = len(deck) // num_players
    for i in range(num_players):
        players[i].extend(deck[i * cards_per_player : (i + 1) * cards_per_player])

def remove_pairs(player):
    pairs = []
    for card in player:
        if card[0] != 'Old Maid':
            rank = card[0]
            if player.count((rank, card[1])) == 2:
                pairs.append((rank, card[1]))
    for pair in pairs:
        player.remove(pair)

def play_old_maid():
    print("Welcome to Old Maid card game!\n")
    num_players = int(input("Enter the number of players (2 or more): "))

    if num_players < 2:
        print("At least 2 players are required to play the game.")
        return

    deck = create_deck()
    shuffle_deck(deck)
    players = [[] for _ in range(num_players)]

    deal_cards(deck, players)

    while True:
        for i in range(num_players):
            print(f"\nPlayer {i+1}'s turn:")
            print("Your hand:", players[i])

            # Check if the player has any cards left
            if len(players[i]) == 0:
                print(f"Player {i+1} has no more cards. They are out of the game!")
                continue

            # Remove pairs from the player's hand
            remove_pairs(players[i])

            # Check if the player has won
            if len(players[i]) == 1 and players[i][0][0] == 'Old Maid':
                print(f"Player {i+1} wins!")
                return

            # Ask the next player to choose a card from the next player
            next_player = (i + 1) % num_players
            card_index = int(input(f"Choose a card index (0-{len(players[next_player])-1}): "))
            card = players[next_player].pop(card_index)
            players[i].append(c2ard)

if __name__ == "__main__":
    play_old_maid()
