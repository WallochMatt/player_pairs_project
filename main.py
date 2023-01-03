
import random

def run_game():
    round= 0 
    number_of_rounds = select_rounds() #You can hard code the rounds too! 3
    player_count = counts_players()
    while round < number_of_rounds:

        deck = {
            "Hearts": ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"],
            "Spades": ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"],
            "Diamonds": ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"],
            "Clubs": ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"],
        }
    
        updated_player_list = assign_hands(player_count, deck) #may need to uncap, but it works so far
        round += declare_winner(updated_player_list)
        input("Press enter for next round, ties are not counted")


def counts_players():
    # amount_of_players = 4
    amount_of_players = int(input("How many players? (10 Player limit. Recommend: 4)")) 
    players = []
    for player in range(amount_of_players):
        players.append(player)
    return players


def deals(deck):
    player_hand = []
    display_hand = ""
    for index in range(5):#?
    
        rand_suit = random.choice(list(deck))
        draw = random.choice(deck[rand_suit])
        display_hand += f"{draw} of {rand_suit} \n"

        player_hand.append(draw)
        deck[rand_suit].remove(draw)

    return {
        "game_hand" : player_hand,
        "shown_hand" : display_hand
    }


def assign_hands(player_count, deck):
    for player_index in range(len(player_count)):
        print(f" {get_player_id(player_index)}")
        hand = deals(deck)

        game_hand = hand.get("game_hand")
        shown_hand = hand.get("shown_hand")
        print(shown_hand)

        list_of_pairs = find_pairs(game_hand)
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

"""
updated_player_list [] - holds the count of pairs a player has (dictated by the player's index position)
highest_pair_count int - the highest point pair, either 0, 1, or 2

They together, in the if statement, check if the highest point-pair is repeated, if so, then theres a tie
Ties return 0, which do not increase the round, where the return is captured on line 19
Wins return 1, which increase the round by 1 where the return is captured on line 19

"""
def declare_winner(updated_player_list):
    highest_pair_count = max(updated_player_list)

    if updated_player_list.count(highest_pair_count) > 1:
        print("Tie")
        return 0
        
    else:
        current_player = 0
        for pair_count in updated_player_list:
            current_player += 1
            if pair_count == highest_pair_count:
                print(f"Player {current_player} won")
        return 1


def get_player_id(index):
    return f"\n Player {str(index + 1)}:"

def select_rounds():
    number_of_rounds = int(input("Select number of rounds: "))
    return number_of_rounds



run_game()

