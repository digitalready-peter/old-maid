import random

def wait_for_player():
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass


def make_deck():
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') # remove a queen as the game requires
    return deck

def shuffle_deck(deck):
    random.shuffle(deck)

def deal_cards(deck):
     dealer=[]
     other=[]
     
     for i in range(0,len(deck),2):
        dealer.append(deck[i])
     for j in range (1,len(deck),2):
        other.append(deck[j])

     return (dealer, other)
 


def remove_pairs(l):
    

    no_pairs=[]

    
    pairs=[]
    counter = 0
    a=sorted(l)
    if a[0][0]==a[1][0] and len(a)==2:
        no_pairs=[]
        return no_pairs
    for i in range(len(a)-3):
        if a[i][0]==a[i+1][0] and  a[i][0]==a[i+2][0] and a[i][0]==a[i+3][0]:
              pairs.append(a[i])
              pairs.append(a[i+1])
              pairs.append(a[i+2])
              pairs.append(a[i+3])
        elif a[i][0]==a[i+1][0] and  a[i][0]!=a[i+2][0]:
              pairs.append(a[i])
              pairs.append(a[i+1])
        if a[-3][0]==a[-2][0]:
            pairs.append(a[-3])
            pairs.append(a[-2])  
        elif a[-2][0]==a[-1][0]:
            pairs.append(a[-1])
            pairs.append(a[-2])
    
        
    pairs=sorted(pairs)
    no_pairs=list((set(l)-set(pairs)))
    random.shuffle(no_pairs)
    return no_pairs

def print_deck(deck):
    
    print(' '.join(deck))

    
def get_valid_input(n):
     '''
     (int)->int
     Returns an integer given by the user that is at least 1 and at most n.
     Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
     
     Precondition: n>=1
     '''
     
     
     x=int(input("Give me an integer between 1 and "+str(n)+':'))
     while x>n or x<1:
        x=int(input("Invalid number. Please enter integer between 1 and "+str(n)+':'))
     
     return x