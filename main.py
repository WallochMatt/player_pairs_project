#pure functions only, everything must be inside a function, do not use global at all

#function: stores 52 cards in a list, try to for loop 4 times

#shuffle function? would random py function suffice? 

# funtion to detect paris in player hands and determines winner  

#function that deals hands? tor multiple players?

import random
#assigns players
amount_of_players = int(input("How many Players? (10 Player limit)")) #going to make a list of players, and I might be able to create a dictionary that way too
players = []
for player in range(amount_of_players): #i changed this from index to player, just in case it breaks
    players.append(player)
print(players)

# #creates full deck
card_types = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
deck = []
for card in card_types * 4:                
    deck.append(card) #now i cn shuffle with random

# #print(deck)

#deals and "shuffles", #the display portion of this will have to be its own function
for player in players:#range(amount_of_players):
    print(f" Player {str(player + 1)}:")
    player_hand = []
    for index in range(5):
        card_in_hand = random.choice(deck)
        deck.remove(card_in_hand)
        player_hand.append(card_in_hand)
    print(player_hand)
        #print(card_in_hand)
        #print(f"{deck} remains") shows card loss progression

#check for winner/results

#it is checking all hands, rather than just a single player
# for x in player_hand:
#     if :
#      print("Pair")
