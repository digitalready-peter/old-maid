#ruthson
import random

#8====D
class  Card():
    def new_deck():
        deck = []
        for suit in Card.SUITS:
            for value in Card.VALUES:
                deck.append(Card(value, suit))
        random.shuffle(deck)
        return deck
    
    VALUES = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    SUITS = ["Clubs", "Spades", "Diamonds", "Hearts"]

def __init__(self, value, suit):
    self.value = value
    self.suit = suit 

def __repr__(self):
        # ♣ ♦ ♥ ♠
        if self.suit == "Clubs":
            symbol = "♣"
        elif self.suit == "Spades":
            symbol = "♠"
        elif self.suit == "Diamonds":
            symbol = "♦"
        elif self.suit == "Hearts":
            symbol = "♥"
        else:
            raise Exception("Invalid Suit")

        if self.value == 11:
            val = "J"
        elif self.value == 12:
            val = "Q"
        elif self.value == 13:
            val = "K"
        elif self.value == 1:
            val = "A"
        else: val = self.value

        return f"{symbol}{val}"



#whenver it is "users" current turn shuffle that users deck proceed
def next_turn(current_turn):
    print("Current Turn: " + current_turn)
    if current_turn == "user":
        return "comp_1"

        self.hand = hand 
    elif current_turn == "comp_1":
        return "comp_2"
    elif current_turn == "comp_2":
        return "comp_3"
    elif current_turn == "comp_3":
        return "user"
    else:
        raise Exception("Fatal Error")


class Player: 
     
    def __init__(self,hand):
            self.hand = hand 

#Peter
import random

#Create deck, shuffle 

class Card:
 SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
 VALUES = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
 
 def new_deck():
        deck = []

        for suit in Card.SUITS:
            for value in Card.VALUES:
                if not (value == 12 and suit == "Hearts"): # Exclude one card from deck (Queen of Hearts)
                    deck.append(Card(value, suit))
#For each suit: For each value: If this is NOT the Queen of Hearts: Add this card to the deck
        random.shuffle(deck)
        return deck

print("You got:")
for i in range(1):
   print(deck [i][0], "of", deck [i][1])

#Dictionary of named cards
cards = {11: "Jack", 12: "Queen", 13: "King", 1:"Ace"}

#Deal cards into hand
def deal_cards(deck):
    hands = [[], [], [], []]

    for i in range(len(deck)):
        hands[i % 4].append(deck[i])

    return hands

deck = new_deck()
hands = deal_cards(deck)

print("Player 1:", hands[0])
print("Better Bot:", hands[1]) 
print("Bott Frag:", hands[2])
print("stan:", hands[3])








