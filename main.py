
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
    amount_of_players = 4
    #amount_of_players = int(input("How many Players? (10 Player limit)")) #going to make a list of players, and I might be able to create a dictionary that way too
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

            
def declare_winner(updated_player_list):
    highest_pair_count = max(updated_player_list)

    if updated_player_list.count(highest_pair_count) > 1:
        print("Tie")
        
    else:
        current_player = 0
        for pair_count in updated_player_list:
            current_player += 1
            if pair_count == highest_pair_count:
                print(f"Player {current_player} won")



def get_player_id(index):
    return f"\n Player {str(index + 1)}:"

def select_rounds():
    number_of_rounds = int(input("Select number of rounds: "))
    return number_of_rounds



run_game()

