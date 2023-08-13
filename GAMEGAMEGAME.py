import random
import time

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') # remove a queen as the game requires
    return deck

def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)

#####################################

def deal_cards(deck):

    dealer = []
    player1 = []
    player2 = []
    player3 = []
    
    variable = 0
    for card in deck:
        if variable == 0:
            dealer.append(card)
            variable = 1
        elif variable == 1:
            player1.append(card)
            variable = 2
        elif variable == 2:
            player2.append(card)
            variable = 3
        elif variable == 3:
            player3.append(card)
            variable = 0
            
    return (dealer, player1, player2, player3)

def remove_pairs(l):
    '''
     (list of str)->list of str

     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled

     Precondition: elements of l are cards represented as strings described above

     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    no_pairs=[]
    
    if len(l) < 2:
        return l
    l.sort()
    l.append([''])    
    item = 1
    while item < len(l):
        if l[item-1][:-1] != l[item][:-1]:
            no_pairs.append(l[item-1])
            item += 1
        else:
            item += 2

    random.shuffle(no_pairs)
    return no_pairs

def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''

    print('')
    print(' '.join(deck))
    print('')
    
def get_valid_input(n):
     '''
     (int)->int
     Returns an integer given by the user that is at least 1 and at most n.
     Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
     
     Precondition: n>=1
     '''
     x = int(input('Give me an integer between 1 and'+' '+str(n)+': '))
     if n >= x >= 1:
         return x
     else:
         while True:
             x = int(input('Invalid number. Please enter integer between 1 and'+' '+str(n)+': '))
             if n >= x >= 1:
                 return x
             else:
                 continue



def play_game():
    deck=make_deck()
    shuffle_deck(deck)
    tmp=deal_cards(deck)
    num_players = 3
    dealer=tmp[0]
    human=tmp[1]
    Bot1=tmp[2]
    Bot2=tmp[3]

    print("Let's play some old maid eh?")
    time.sleep(2)
    print("")
    print('It might be your first time so let me give you a quick rundown.')
    time.sleep(2)
    print('This is your deck:')
    print_deck(human)
    time.sleep(2)
    print("I cannot see your deck so do not worry.")
    time.sleep(1)
    print("First, you must discard all card in your hand, but since we don't really have hands, the cards will automatically discard themselves. How neat is that?")
    print("Also, we'll just play till whoever runs out of cards first. (God help me I can't figure this out)")

    dealer=remove_pairs(dealer)
    human=remove_pairs(human)
    Bot1=remove_pairs(Bot1)
    Bot2=remove_pairs(Bot2)
    
    turn = 0
    time.sleep(2)
    print("By the way, I've invited some of my friends to play as well, hope you don't mind.")
    wait_for_player()
    while 3 >= turn >= 0:
        if len(human) == 0:
            print("")
            print("It seems that you've bested us this time.")
            print("Congrats.")
            print("THE HUMAN WINS")
            break
        elif len(dealer) == 0:
            print("")
            print("Well, good game to you sir.")
            print("DEALER WINS")
            break
        elif len(Bot1) == 0:
            print("")
            print("IM LIKE THAT.")
            print("BOT 1 WINS")
            break
        elif len(Bot2) == 0:
            print("")
            print("Haha, I still don't really get this.")
            print("BOT 2 WINS")
            break
        else:
            if turn == 0:
                print('')
                print("Your deck is:")
                print_deck(human)
                print("Who would you like to take from?")
                chosen_player = get_valid_input(num_players)
                print(f"You chose player {chosen_player}")
                if chosen_player == 1:
                    n = len(dealer)
                    print("Dealer: Alright, pick one of my cards.")
                    result = get_valid_input(n)

                    if result == 1:
                        print('You asked for my 1st card.')
                    elif result == 2:
                        print('You asked for my 2nd card.')
                    elif result == 3:
                        print('You asked for my 3rd card.')
                    else:
                        print('You asked for my',str(result)+'th card.')

                    print('Here it is. It is',dealer[int(result)-1])
                    print('')
                    print('With',dealer[int(result)-1],'added, your current deck of cards is:')
                    human.append(dealer[int(result)-1])
                    dealer.remove(dealer[int(result)-1])
                    print_deck(human)
                    print('And after discarding pairs and shuffling, your deck is:')
                    human=remove_pairs(human)
                    print_deck(human)
                    turn = 1
                    wait_for_player()
                elif chosen_player == 2:
                    n = len(Bot1)
                    print("Bot 1: Alright, pick one of my cards.")
                    result = get_valid_input(n)

                    if result == 1:
                        print('You asked for my 1st card.')
                    elif result == 2:
                        print('You asked for my 2nd card.')
                    elif result == 3:
                        print('You asked for my 3rd card.')
                    else:
                        print('You asked for my',str(result)+'th card.')

                    print('Here it is. It is',Bot1[int(result)-1])
                    print('')
                    print('With',Bot1[int(result)-1],'added, your current deck of cards is:')
                    human.append(Bot1[int(result)-1])
                    Bot1.remove(Bot1[int(result)-1])
                    print_deck(human)
                    print('And after discarding pairs and shuffling, your deck is:')
                    human=remove_pairs(human)
                    print_deck(human)
                    turn = 1
                    wait_for_player()
                elif chosen_player == 3:
                    n = len(Bot2)
                    print("Bot 2: Alright, pick one of my cards.")
                    result = get_valid_input(n)

                    if result == 1:
                        print('You asked for my 1st card.')
                    elif result == 2:
                        print('You asked for my 2nd card.')
                    elif result == 3:
                        print('You asked for my 3rd card.')
                    else:
                        print('You asked for my',str(result)+'th card.')

                    print('Here it is. It is',Bot2[int(result)-1])
                    print('')
                    print('With',Bot2[int(result)-1],'added, your current deck of cards is:')
                    human.append(Bot2[int(result)-1])
                    Bot2.remove(Bot2[int(result)-1])
                    print_deck(human)
                    print('And after discarding pairs and shuffling, your deck is:')
                    human=remove_pairs(human)
                    print_deck(human)
                    turn = 1
                    wait_for_player()
            elif turn == 1:
                 print('')
                 print('Dealer: My turn.')
                 print('')
                 chosen_player = random.choice(["Human", "Bot1", "Bot2"])
                
                
                 n = len(chosen_player) if chosen_player == "Human" else len(Bot1) if chosen_player == "Bot1" else len(Bot2)
                 result = random.randint(1, n)

                 if chosen_player == "Human":
                    print(f"I took your {result}{'st' if result == 1 else 'nd' if result == 2 else 'rd' if result == 3 else 'th'} card.")
                    dealer.append(human[result - 1])
                    human.pop(result - 1)
                    dealer = remove_pairs(dealer)
                    turn = 2
                    wait_for_player()
                 elif chosen_player == "Bot1":
                    print(f"I took {'Bot1'}'s {result}{'st' if result == 1 else 'nd' if result == 2 else 'rd' if result == 3 else 'th'} card.")
                    dealer.append(Bot1[result - 1])
                    Bot1.pop(result - 1)
                    dealer = remove_pairs(dealer)
                    turn = 2
                    wait_for_player()
                 elif chosen_player == "Bot2":
                    print(f"I took {'Bot 2'}'s {result}{'st' if result == 1 else 'nd' if result == 2 else 'rd' if result == 3 else 'th'} card.")
                    dealer.append(Bot2[result - 1])
                    Bot2.pop(result - 1)
                    dealer = remove_pairs(dealer)
                    turn = 2
                    wait_for_player()
            elif turn == 2:
                 print('')
                 print('Bot 1: My turn.')
                 print('')
                 chosen_player = random.choice(["Human", "Dealer", "Bot2"])
                
                
                 n = len(chosen_player) if chosen_player == "Human" else len(Bot1) if chosen_player == "Bot1" else len(Bot2)
                 result = random.randint(1, n)

                 if chosen_player == "Human":
                    print(f"I took your {result}{'st' if result == 1 else 'nd' if result == 2 else 'rd' if result == 3 else 'th'} card.")
                    dealer.append(human[result - 1])
                    human.pop(result - 1)
                    dealer = remove_pairs(dealer)
                    turn = 3
                    wait_for_player()
                 elif chosen_player == "Dealer":
                    print(f"I took {'The Dealer'}'s {result}{'st' if result == 1 else 'nd' if result == 2 else 'rd' if result == 3 else 'th'} card.")
                    Bot1.append(dealer[result - 1])
                    dealer.pop(result - 1)
                    Bot1 = remove_pairs(Bot1)
                    turn = 3
                    wait_for_player()
                 elif chosen_player == "Bot2":
                    print(f"I took {'Bot 2'}'s {result}{'st' if result == 1 else 'nd' if result == 2 else 'rd' if result == 3 else 'th'} card.")
                    Bot1.append(Bot2[result - 1])
                    Bot2.pop(result - 1)
                    Bot1 = remove_pairs(Bot1)
                    turn = 3
                    wait_for_player()
            elif turn == 3:
                 print('')
                 print('Bot 2: My turn.')
                 print('')
                 chosen_player = random.choice(["Human", "Dealer", "Bot1"])
                
                
                 n = len(chosen_player) if chosen_player == "Human" else len(Bot1) if chosen_player == "Bot1" else len(Bot2)
                 result = random.randint(1, n)

                 if chosen_player == "Human":
                    print(f"I took your {result}{'st' if result == 1 else 'nd' if result == 2 else 'rd' if result == 3 else 'th'} card.")
                    Bot2.append(human[result - 1])
                    human.pop(result - 1)
                    Bot2 = remove_pairs(Bot2)
                    turn = 0
                    wait_for_player()
                 elif chosen_player == "Dealer":
                    print(f"I took {'The Dealer'}'s {result}{'st' if result == 1 else 'nd' if result == 2 else 'rd' if result == 3 else 'th'} card.")
                    Bot2.append(dealer[result - 1])
                    dealer.pop(result - 1)
                    Bot2 = remove_pairs(Bot2)
                    turn = 0
                    wait_for_player()
                 elif chosen_player == "Bot1":
                    print(f"I took {'Bot 1'}'s {result}{'st' if result == 1 else 'nd' if result == 2 else 'rd' if result == 3 else 'th'} card.")
                    Bot2.append(Bot1[result - 1])
                    Bot1.pop(result - 1)
                    Bot2 = remove_pairs(Bot2)
                    turn = 0
                    wait_for_player()           

if __name__ == "__main__":
    play_game()
    