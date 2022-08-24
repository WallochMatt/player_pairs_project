
import random

def run_game():
    round= 0 
    number_of_rounds = select_rounds()
    player_count = counts_players()
    while round < number_of_rounds:

        full_deck = makes_deck()
    
        updated_player_list = assign_hands(player_count, full_deck) #may need to uncap, but it works so far
        
        declare_winner(updated_player_list)
        round += 1
        input("Press enter for next round")

def counts_players():
    #amount_of_players = 4
    amount_of_players = int(input("How many Players? (10 Player limit)")) #going to make a list of players, and I might be able to create a dictionary that way too
    players = []
    for player in range(amount_of_players):
        players.append(player)
    return players
    # amount_of_players = 2#int(input("How many Players? (10 Player limit)")) #going to make a list of players, and I might be able to create a dictionary that way too
    # players = [] * amount_of_players#empty spaces?
    # return players


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
    for player_index in range(len(player_count)):
        print(f" {get_player_id(player_index)}")
        hand = deals(full_deck)
        print(hand)
        list_of_pairs = find_pairs(hand)
        num_of_pairs = len(list_of_pairs)
        player_count[player_index] = num_of_pairs
      
    return player_count


def find_pairs(hand):
    copies = set()
    for card_index in hand:
        if hand.count(card_index) > 1:
            copies.add(card_index)
   
    print(f"{len(copies)} pairs!")
    return copies

            
def declare_winner(player_count):
    #I have chosen to leave this in a comment mess for the sake of feedback 
    largest_pairing = 0
    tie_call = 0
    for current_player_index in range(len(player_count)):
        if (player_count[current_player_index] == player_count[largest_pairing]):# and (player_count[current_player_index] != player_count[largest_pairing]):
             print(f"{get_player_id(largest_pairing)} tied!!")
             tie_call += 1
        

        # if(player_count[current_player_index] > player_count[largest_pairing]):
        #     largest_pairing = current_player_index

        # for current_player_index in range(len(player_count)):
        #     if current_player_index != (len(player_count) - 1):

        #         if current_player_index == player_count[current_player_index + 1]:
        #             print(f"TIE with {get_player_id(current_player_index)}")
        #             break
        #         else:
        #             pass
        if(player_count[current_player_index] > player_count[largest_pairing]) and tie_call == 0:
            largest_pairing = current_player_index

    print(f"{get_player_id(largest_pairing)} won with {player_count[largest_pairing]} pairs!!!")


def get_player_id(index):
    return f"\n Player {str(index + 1)}:"

def select_rounds():
    number_of_rounds = int(input("Select number of rounds: "))
    return number_of_rounds



run_game()

