
# importing modules
import itertools, random

# make a deck of cards
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

# shuffle the cards
random.shuffle(deck)

# draw five cards
print("You got:")
for i in range(5):
   print(deck[i][0], "of", deck[i][1])





   def new_deck():
        deck = []
        for suit in Card.SUITS:
            for value in Card.VALUES:
                deck.append(Card(value, suit))
        random.shuffle(deck)
        return 
   




def next_turn(current_turn): 
    print('Current Turn: "' + current_turn)
    if current_turn == "user":
        return "comp_1"
    elif current_turn == "comp_1":
        return "comp_2"
    elif current_turn == "comp_2":
        return "comp_3" 
    elif current_turn == "comp_3":
        return "user"
    else:
        raise Exception("Fatal Error")

