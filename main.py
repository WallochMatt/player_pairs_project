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
#Note: I could make a while loop in the run game function to start the next game, keep track of score and end game..
def run_game():
    number_of_players = counts_players()
    full_deck = makes_deck()
    
    pairs = assign_hands(number_of_players, full_deck) #may need to uncap, but it works so far
    
    
    winner(number_of_players, pairs)

def counts_players():
    amount_of_players = 2#int(input("How many Players? (10 Player limit)")) #going to make a list of players, and I might be able to create a dictionary that way too
    players = []
    for player in range(amount_of_players):
        players.append(player)
    return players

def makes_deck():
    card_types = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    deck = []
    for card in card_types * 4:                
        deck.append(card)
    return deck

def deals(deck):
    player_hand = []
    for index in range(5):#?
        card_in_hand = random.choice(deck)
        deck.remove(card_in_hand)
        player_hand.append(card_in_hand)
    return player_hand


def assign_hands(number_of_players, full_deck):
    for player_at_index in range(len(number_of_players)):
        print(f" Player {str(player_at_index + 1)}:") #"HUD" function made obsolete
        hand = deals(full_deck) 
        print(hand)
        number_of_pairs = copy_list(hand)  #i know the player set copies alreadt
    return number_of_pairs

def copy_list(hand):
    copies = set()
    for card in hand:
        if hand.count(card) > 1:
            copies.add(card)

    print(f"{len(copies)} Pairs")
    return copies

def winner(number_of_players, pairs):
    for player in range(len(number_of_players)):
        if player != len(number_of_players):

            for pair in pairs:
                if pair == 

            

            






run_game()
