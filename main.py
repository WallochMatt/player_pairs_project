# for player in players:#works on scratch pad before functions were made
#     open_hand = set()
#     if [card for card in player_hand if card in open_hand or open_hand.add(card)]:
#         print("MATCH")
#^this is list comprehension, I can't mess with this yet

#pure functions only, everything must be inside a function, do not use global at all

#function: stores 52 cards in a list, try to for loop 4 times

#shuffle function? would random py function suffice? 

# funtion to detect paris in player hands and determines winner  

#function that deals hands? tor multiple players?

import random

def run_game():
    player_count = counts_players()
    deck = makes_deck()
    player_hands = deals(deck) #it needs access to the players and deck from those respective functions
    checks_results(player_count, player_hands)

#assigns players
def counts_players():
    amount_of_players = 2#int(input("How many Players? (10 Player limit)")) #going to make a list of players, and I might be able to create a dictionary that way too
    players = []
    for player in range(amount_of_players): #i changed this from index to player, just in case it breaks
        players.append(player)
    return players

# #creates full deck
def makes_deck():
    card_types = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    deck = []
    for card in card_types * 4:                
        deck.append(card) #now i cn shuffle with random
    return deck

#deals and "shuffles", #the display portion of this will have to be its own function
def deals(deck):
    player_hand = []
    for index in range(5):#?
        card_in_hand = random.choice(deck)
        deck.remove(card_in_hand)
        player_hand.append(card_in_hand)
    return player_hand #may need to move out a scope
       
def hud(players, card_in_hand):
    for player in players:#range(amount_of_players):
        print(f" Player {str(player + 1)}:")
        print(card_in_hand)
        #print(f"{deck} remains") shows card loss progression

#check for winner/results
# it is checking all hands, rather than just a single player

def checks_results(players, player_hand):
    for player in players:
        for index in player_hand:
            if player_hand.count(index) > 1:
                print("M")

run_game()