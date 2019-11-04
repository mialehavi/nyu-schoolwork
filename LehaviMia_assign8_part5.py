#Mia Lehavi
#Section 03
#Assignment 8, Part 5: Blackjack (extra credit)

import random

cards  = ['10 of Hearts', '9 of Hearts', '8 of Hearts', '7 of Hearts', '6 of Hearts', '5 of Hearts', '4 of Hearts', '3 of Hearts', '2 of Hearts', 'Ace of Hearts', 'King of Hearts', 'Queen of Hearts', 'Jack of Hearts', '10 of Diamonds', '9 of Diamonds', '8 of Diamonds', '7 of Diamonds', '6 of Diamonds', '5 of Diamonds', '4 of Diamonds', '3 of Diamonds', '2 of Diamonds', 'Ace of Diamonds', 'King of Diamonds', 'Queen of Diamonds', 'Jack of Diamonds', '10 of Clubs', '9 of Clubs', '8 of Clubs', '7 of Clubs', '6 of Clubs', '5 of Clubs', '4 of Clubs', '3 of Clubs', '2 of Clubs', 'Ace of Clubs', 'King of Clubs', 'Queen of Clubs', 'Jack of Clubs', '10 of Spades', '9 of Spades', '8 of Spades', '7 of Spades', '6 of Spades', '5 of Spades', '4 of Spades', '3 of Spades', '2 of Spades', 'Ace of Spades', 'King of Spades', 'Queen of Spades', 'Jack of Spades']

values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10]


#accumulators to count # of wins for player and computer
player_win = 0
computer_win = 0

player_cards = []
player_worth = 0



#deal two cards at random to player
c1 = random.choice(cards)
c2 = random.choice(cards)

#store these cards and associated values in separate lists
player_cards.append(c1)
player_cards.append(c2)
posc1 = cards.index(c1)
posc2 = cards.index(c2)
player_worth += values[posc1]
player_worth += values[posc2]

# remove the two cards from deck once they have been dealt so they cannot be dealt a second time.
cards.remove(c1)
cards.remove(c2)

while True:
    # report player's hand & value of their hand
    print("Player Hand:",player_cards, "is worth", player_worth)
                
    #ask the player if they want to "hit" or "stand"
    choice = str.lower(input("(h)it or (s)tand? "))

    #"hit": deal them another card (and remove it from the main deck)
    if choice == "h":
        draw = random.choice(cards)
        print("You drew", draw)
        pos = cards.index(draw)
        cards.remove(draw)
        player_cards.append(draw)
        player_worth += values[pos]

        #if hand is worth 21 points they win the game
        if player_worth == 21:
            print("You got 21! Blackjack!")
            print("You win!")
            player_win += 1
            break
        
        #if over 21 points they lose the game
        elif player_worth > 21:
            print("Bust!")
            print("Computer wins!")
            computer_win += 1
            break
        #less than 21 points - continue loop 
        else:
            continue
    #"stand": they will have less than 21 points
    elif choice == "s":
        #give the computer opportunity to beat the player's score
        #deal two cards to the computer
        comp_cards = []
        comp_worth = 0
        comp1 = random.choice(cards)
        comp2 = random.choice(cards)
        comp_cards.append(comp1)
        comp_cards.append(comp2)
        c_posc1 = cards.index(comp1)
        c_posc2 = cards.index(comp2)
        comp_worth += values[c_posc1]
        comp_worth += values[c_posc2]

        while True:
            
            #report the computer's hand and point value
            print("Computer Hand:",comp_cards, "is worth", comp_worth)
            draw = random.choice(cards)
            print("You drew", draw)
            pos2 = cards.index(draw)
            cards.remove(draw)
            comp_cards.append(draw)
            comp_worth += values[pos2]
            if comp_worth < 21:
                # comp stops hitting if computer earns more points than the player
                if comp_worth > player_worth:
                    print("Computer wins!")
                    break
                else:
                    continue
            # comp stops hitting computer gets 21 points (blackjack)
            elif comp_worth == 21:
                print("Computer got 21! Blackjack!")
                print("Computer wins!")
                break
            # comp stops hitting if computer goes "bust" 
            else:
                print("Bust!")
                print("Player wins!")
                break
        break
        

#Write in a system that allows the user to maintain a "bank" of money
#Allow them to keep playing as long as their bank is above $0
#Each hand that they choose to play should cost a small amount of money (say, $5) and if they win they will double their money
#if they lose their initial bet is forfeited. This feature is not shown in the output below.
                   
