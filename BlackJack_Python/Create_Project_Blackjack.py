#Aidan Lamkin
#CSCI 101 Section G
#Create Project Blackjack
#References: file input/ouput lecture videos for 102
#Time: 300 min

import random

def introduction():
    print("Welcome to my player versus computer blackjack game! The goal of the game is")
    print("to get your hand of cards as close to 21 as possible without exceeding 21.")

def print_line():
    print("-------------------------------------------------------------------------------")
    
def fill_deck(deck_of_cards):
    with open("DeckOfCards.txt", "r") as cards:
        for row in cards:
            line = row.rstrip()
            deck_of_cards.append(line)

def clear_deck(deck):
    deck.clear()

def copy_deck(deck1, deck2):
    for i in range(len(deck1)):
        deck2.append(deck1[i])

def play_again():
    user_input = ""
    acceptable_answers = ['Play', 'play', 'Quit', 'quit']
    while user_input not in acceptable_answers:
        print("Would you like to play a round or quit:")
        user_input = input("Play/Quit> ")
        if user_input in acceptable_answers:
            return user_input

def place_bet(chips):
    current_bet = -1
    while current_bet < 0 or current_bet > chips:
        print("How many chips would you like to bet?")
        current_bet = int(input("Bet> "))
    return current_bet

def hit(player_deck, table_deck):
    index = random.randint(0, len(table_deck) - 1)
    random_card = table_deck[index]
    player_deck.append(random_card)
    table_deck.pop(index)
    print(f"You were dealt a {random_card}")
    
def assign_card_value(player_deck, value_player_deck):
    card = player_deck[-1]
    c = card[0]
    value = 0
    if card == '10':
        value = 10
    elif c.isdigit() == True:
        value = int(c)
    elif c == 'A':
        value = 1
    else:
        value = 10
    value_player_deck.append(value)

def get_hand_sum(value_deck):
    hand_sum = 0
    for i in range(len(value_deck)):
        hand_sum += value_deck[i]

    return hand_sum

def print_hand_sum(value_deck):
    print(f"Your hand total is {get_hand_sum(value_deck)}")
    
def check_for_bust(value_deck):
    if get_hand_sum(value_deck) <= 21:
        return False
    else:
        return True

def check_ace(value_deck):
    user_input = ""
    for i in range(len(value_deck)):
        if value_deck[i] == 1:
            while(user_input != 1 and user_input != 11):
                print("Would you like your Ace to be worth 1 or 11?")
                user_input = int(input("ACE> "))
            if user_input == 1:
                continue
            elif user_input == 11:
                value_deck[i] = 11

def dealer_setup(dealer_deck, dealer_value_deck, table_deck):
    for i in range(2):
        index = random.randint(0, len(table_deck) - 1)
        random_card = table_deck[index]
        dealer_deck.append(random_card)
        table_deck.pop(index)
        assign_card_value(dealer_deck, dealer_value_deck)
    for i in range(len(dealer_value_deck)):
        if dealer_value_deck[i] == 1:
            dealer_value_deck[i] = 11

    print(f"The dealer is showing a {dealer_deck[-1]}")

def dealer_hit(dealer_deck, dealer_value_deck, table_deck):
    print(f"The dealer's first card is a {dealer_deck[0]}")
    print(f"The dealer's hand total is {get_hand_sum(dealer_value_deck)}")
    print_line()
    while get_hand_sum(dealer_value_deck) < 17:
        index = random.randint(0, len(table_deck) - 1)
        random_card = table_deck[index]
        dealer_deck.append(random_card)
        table_deck.pop(index)
        assign_card_value(dealer_deck, dealer_value_deck)
        print(f"The dealer drew a {dealer_deck[-1]}")
        print(f"The dealer's hand total is {get_hand_sum(dealer_value_deck)}")
        print_line()
        if get_hand_sum(dealer_value_deck) > 21:
            for i in range(len(dealer_value_deck)):
                if dealer_value_deck[i] == 11:
                    dealer_value_deck[i] = 1
                if get_hand_sum(dealer_value_deck) > 21:
                    print("The dealer busted!")
                    return

def ace_logic(value_deck):
    for i in range(len(value_deck)):
        if value_deck[i] == 1 and get_hand_sum(value_deck) + 10 == 21:
            value_deck[i] = 11
            return 1

def check_split(player_deck, player_value_deck, split_deck, split_value_deck, current_bet, total_chips):
    user_input = ""
    card1 = player_deck[0]
    card2 = player_deck[1]
    c1 = card1[0]
    c2 = card2[0]
    if c1 == c2:
        if current_bet * 2 > total_chips:
            print("You are unable to split because you don't have enough chips.")
            return
        while user_input != 'Yes' and user_input != 'yes' and user_input != 'No' and user_input != 'no':
            print("Would you like to split your hand in to two hands?")
            user_input = input("Yes/No> ")
        if user_input == 'Yes' or user_input == 'yes':
            split_deck.append(card2)
            player_deck.pop(1)
            split_deck.append(player_value_deck[1])
            player_value_deck.pop(1)
            return True
        elif user_input == "No" or user_input == "no":
            return False

full_deck = []
table_deck = []

fill_deck(full_deck)
player_hand = []
player_value = []
dealer_hand = []
dealer_value = []
player_split = []
player_value_split = []

user_move = ""
next_game = "play"

number_of_chips = 10
current_bet = 0
split_bet = 0
blackjack = 21

introduction()


while (next_game == 'play' or next_game == 'Play') and number_of_chips > 0:
    
    print_line()
    next_game = play_again()

    if next_game == 'play' or next_game == 'Play':
        print(f"You have {number_of_chips} chips")

        current_bet = place_bet(number_of_chips)
        print_line()
        while current_bet > number_of_chips:
            current_bet = place_bet(number_of_chips)
            print_line()

        copy_deck(full_deck,table_deck)

        hit(player_hand, table_deck)
        assign_card_value(player_hand, player_value)
        hit(player_hand, table_deck)
        assign_card_value(player_hand, player_value)
        print_line()

        if ace_logic(player_value) != 1:
            check_ace(player_value)

        print_hand_sum(player_value)
        print_line()

        split = check_split(player_hand, player_value, player_split, player_value_split, current_bet, number_of_chips)

        if split == True:
            split_bet = current_bet
            print_line()

        if get_hand_sum != blackjack:
            dealer_setup(dealer_hand, dealer_value, table_deck)

        bust_check = False
        bust_check_split = False

        user_move = "Blank"

        while (user_move != "Stay" and user_move != "stay") and bust_check == False and get_hand_sum(player_value) != blackjack:

            if user_move != 'Hit' or user_move != 'hit' or user_move != 'stay' or user_move != 'Stay' or user_move != 'Double down' or user_move != 'double down':
                user_move = input("Would you like to hit, double down, or stay?> ")
                print_line()

            if user_move == 'hit' or user_move == 'Hit':
                hit(player_hand, table_deck)
                assign_card_value(player_hand, player_value)
                if ace_logic(player_value) != 1:
                    check_ace(player_value)
                print_hand_sum(player_value)
                print_line()

                bust_check = check_for_bust(player_value)

            if user_move == 'Double down' or user_move == 'double down':
                if current_bet * 2 + split_bet > number_of_chips:
                    print("You can not double down because you don't have enough chips.")
                    print_line()
                else:
                    current_bet *= 2
                    hit(player_hand, table_deck)
                    assign_card_value(player_hand, player_value)
                    if ace_logic(player_value) != 1:
                        check_ace(player_value)
                    print_hand_sum(player_value)
                    print_line()

                    bust_check = check_for_bust(player_value)
                    break
            else:
                continue
            
            if get_hand_sum(player_value) == blackjack:
                break

        if bust_check == True:
            print("You busted!")
            if split == True:
                clear_deck(player_hand)
                clear_deck(player_value)
                number_of_chips -= current_bet
                print(f"You lost {current_bet} chips!")
                current_bet = 0
            else:
                clear_deck(player_hand)
                clear_deck(player_value)
                clear_deck(dealer_hand)
                clear_deck(dealer_value)
                clear_deck(table_deck)
                number_of_chips -= current_bet
                print(f"You lost {current_bet} chips!")
                continue

        if get_hand_sum(player_value) == blackjack:
            print("BLACKJACK!")
            if split == True:
                clear_deck(player_hand)
                clear_deck(player_value)
                number_of_chips += round(current_bet * 1.5)
                print(f"You gained {int(current_bet*1.5)} chips!")
                current_bet = 0
            else:
                clear_deck(player_hand)
                clear_deck(player_value)
                clear_deck(dealer_hand)
                clear_deck(dealer_value)
                clear_deck(table_deck)
                number_of_chips += round(current_bet * 1.5)
                print(f"You gained {int(current_bet*1.5)} chips!")
                continue

        user_move = "Blank"
                
        while (user_move != "Stay" and user_move != "stay") and bust_check_split == False and split == True:

            if user_move != 'Hit' or user_move != 'hit' or user_move != 'stay' or user_move != 'Stay' or user_move != 'Double down' or user_move != 'double down':
                user_move = input("Would you like to hit, double down, or stay?> ")
                print_line()

            if user_move == 'hit' or user_move == 'Hit':
                hit(player_split, table_deck)
                assign_card_value(player_split, player_value_split)
                if ace_logic(player_value) != 1:
                    check_ace(player_value)
                print_hand_sum(player_value_split)
                print_line()

                bust_check_split = check_for_bust(player_value_split)

            if user_move == 'Double down' or user_move == 'double down':
                if split_bet * 2 + current_bet > number_of_chips:
                    print("You can not double down because you don't have enough chips.")
                    print_line()
                else:
                    split_bet *= 2
                    hit(player_split, table_deck)
                    assign_card_value(player_split, player_value_split)
                    if ace_logic(player_value) != 1:
                        check_ace(player_value)
                    print_hand_sum(player_value_split)
                    print_line()

                    bust_check_split = check_for_bust(player_value_split)
                    break
            else:
                continue
            
            if get_hand_sum(player_value_split) == blackjack:
                break

        if bust_check_split == True:
            print("You busted!")
            clear_deck(player_split)
            clear_deck(player_split_value)
            number_of_chips -= split_bet
            print(f"You lost {split_bet} chips!")
            print_line()
            split_bet = 0

        if get_hand_sum(player_value_split) == blackjack:
            print("BLACKJACK!")
            clear_deck(player_split)
            clear_deck(player_split_value)
            number_of_chips += round(split_bet * 1.5)
            print(f"You gained {int(split_bet * 1.5)} chips!")
            print_line()
            split_bet = 0


        dealer_hit(dealer_hand, dealer_value, table_deck)

        if check_for_bust(dealer_value) == True:
            print("You won!")
            clear_deck(player_hand)
            clear_deck(player_value)
            clear_deck(dealer_hand)
            clear_deck(dealer_value)
            clear_deck(table_deck)

            if split == False:
                number_of_chips += current_bet
                print(f"You gained {current_bet} chips!")
            else:
                number_of_chips += current_bet + split_bet
                print(f"You gained {current_bet + split_bet} chips")
            continue

        if get_hand_sum(dealer_value) == blackjack:
            print("Dealer won!")
            clear_deck(player_hand)
            clear_deck(player_value)
            clear_deck(dealer_hand)
            clear_deck(dealer_value)
            clear_deck(table_deck)
            if split == False:
                number_of_chips -= current_bet
                print(f"You lost {current_bet} chips!")
            else:
                number_of_chips -= (current_bet + split_bet)
                print(f"You lost {current_bet + split_bet} chips")
                continue

        if get_hand_sum(player_value) > get_hand_sum(dealer_value) and get_hand_sum(player_value) < blackjack:
            print("You won!")
            number_of_chips += current_bet
            print(f"You gained {current_bet} chips!")
        elif get_hand_sum(player_value) < get_hand_sum(dealer_value) and get_hand_sum(dealer_value) < blackjack:
            print("Dealer won!")
            number_of_chips -= current_bet
            print(f"You lost {current_bet} chips!")
        elif get_hand_sum(player_value) == get_hand_sum(dealer_value):
            print("It's a push!")
            print("Your number of chips stays the same!")

        if split == True and bust_check_split == False and get_hand_sum(player_value_split) != blackjack:
            if get_hand_sum(player_value_split) > get_hand_sum(dealer_value) and get_hand_sum(player_value_split) < blackjack:
                print("Your split hand won!")
                number_of_chips += split_bet
                print(f"You gained {split_bet} chips!")
            elif get_hand_sum(player_value_split) < get_hand_sum(dealer_value) and get_hand_sum(dealer_value) < blackjack:
                print("Dealer won against your split hand!")
                number_of_chips -= split_bet
                print(f"You lost {split_bet} chips!")
            elif get_hand_sum(player_value_split) == get_hand_sum(dealer_value):
                print("It's a push against your split hand!")
                print("Your number of chips stays the same!")

        clear_deck(player_hand)
        clear_deck(player_value)
        clear_deck(player_split)
        clear_deck(player_value_split)
        clear_deck(dealer_hand)
        clear_deck(dealer_value)
        clear_deck(table_deck)

        current_bet = 0
        split_bet = 0


if number_of_chips == 0:
    print("Sorry, you're broke. Better luck next time!")
elif number_of_chips > 10:
    print(f"You gained {number_of_chips - 10} chips while at the table. Nice!")
elif number_of_chips < 10:
    print(f"You lost {10 - number_of_chips} chips while at the table. Try your luck another time!")
else:
    print("You broke even. Not bad")

print("Have a nice day!")

            
    

        

        
