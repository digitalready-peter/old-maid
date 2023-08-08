import random

#Create deck, shuffle 

 
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

def deal_cards(deck):
     '''Returns two lists representing two decks that are obtained
     after the dealer deals the cards from the given deck.
     The first list represents dealer's i.e. computer's deck
     and the second represents the other player's i.e user's list.
     '''
     dealer=[]
     other=[]
     

     # 
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

def remove_pairs(l):

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















