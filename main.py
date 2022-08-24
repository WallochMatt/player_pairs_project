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
    player_count = counts_players()
    full_deck = makes_deck()
    #hand = deals(full_deck) #this ran an additional instence
    test = assign_hands(player_count, full_deck) #may need to uncap, but it works so far
    pairs = copy_list() #made a dupe
    #result = checks_results(hand)
    winner(player_count, pairs)

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


def assign_hands(player_count, full_deck):
    for player in player_count:
        print(f" Player {str(player + 1)}:") #"HUD" function made obsolete
        hand = deals(full_deck)
        print(hand)
        pairs = copy_list(hand)
        #checks_results(hand)
    return pairs #needed? check here if i get none for pairs or zero, may need to delete


def copy_list(hand):
    copies = {0} #use length of the set - 1
    for index in hand:
        if hand.count(index) > 1:
            copies.add(index)
    copies.discard(0)
    #print(f" {len(copies)} matches")
    print(len(copies))
    return copies

def winner(players, copies):
    for player in players:
        if len(copies) == 0:
            print("izzero")
        else:
            print6
            
# def winner(players, copies):
#     for player in range(len(players)):
#         #for index in range(0, players):
#         if len(copies) == 0:
#             print("No pairs")
#             #if player != player[-1]:
#         if player.len(copies) > player[1].len(copies): #find away around this out of range
#             print(f" Player {str(player + 1)} wins")
#         elif len(copies) == len(copies[player + 1]):
#             print("Tie")
#     # for player in range(len(players)):
#     #     for index in range(player + 1, len(players)):
            






run_game()

# def copy_list(hand): #alt for check results
#     copies = [] # couldn't this be a set?
#     for index in hand:
#         if hand.count(index) > 1:
#             copies.append(index)
#             hand.remove(index)
#             #print(f" {len(copies)} matches")
#             #return copies