import random

deck = [2,3,4,5,6,7,8,9,10,11,12,13,14] * 4
player_hand = []
dealer_hand = []
count = 0

def deal(deck, player_hand, dealer_hand):
    random.shuffle(deck)
    for i in range(2):
        player_card = deck.pop()
        if player_card == 11: player_card = 'J'
        if player_card == 12: player_card = 'Q'
        if player_card == 13: player_card = 'K'
        if player_card == 14: player_card = 'A'
        player_hand.append(player_card)
        dealer_card = deck.pop()
        if dealer_card == 11: dealer_card = 'J'
        if dealer_card == 12: dealer_card = 'Q'
        if dealer_card == 13: dealer_card = 'K'
        if dealer_card == 14: dealer_card = 'A'
        dealer_hand.append(dealer_card)
    return(deck, player_hand, dealer_hand)
#
# deal(deck, player_hand, dealer_hand)
# print(deck,player_hand,dealer_hand)

def score(hand):
    total = 0
    for i in hand:
        if i == 'J' or i == 'Q' or i == 'K':
            total += 10
        elif i == 'A':
            if total <= 10:
                total += 11
            else:
                total += 1
        else:
            total = total + i
    if total > 21:
        print("Bust!")
        play_again()
    return total
#
def black_jack(hand):
    if hand == 21:
        print('BLACKJACK. You loose')
        play_again()

def play_again():
    if len(deck) <= 8:
        print("Not enough deck in the shoe. See ya later")
        end()
    else:
        print("there are {} cards left in the shoe.".format(len(deck)))
        again = input("Type Y to play again\n>").lower()
        player_hand = []
        dealer_hand = []
        if again == "y":
            play(deck, player_hand, dealer_hand)
        else:
            print('thanks for playing!')
            exit()
def result(player_hand, dealer_hand):
    print('Player\'s hand: {}\n Dealer\'s hand: {}\n '.format(player_hand,dealer_hand))
    if player_hand == dealer_hand:
        print("Push")
    elif player_hand == 21:
        print("BLACKJACK")
    elif score(player_hand) < score(dealer_hand):
        print("Player Looses!")
    elif score(player_hand) > score(dealer_hand):
        print("Player Wins!")

def hit(player_hand):
    while True:
        a = input('Do want a card? (Y/N)\n>').lower()
        if a == 'y':
            player_card = deck.pop()
            if player_card == 11: player_card = 'J'
            if player_card == 12: player_card = 'Q'
            if player_card == 13: player_card = 'K'
            if player_card == 14: player_card = 'A'
            player_hand.append(player_card)
            print("You got a {}".format(player_card))
            print("Your total is {}".format(score(player_hand)))
        elif a == 'n':
            break
        else:
            print("I didn't understand that answer")

def dealer_hit(dealer_hand):
    while score(dealer_hand) < 16:
        dealer_card = deck.pop()
        dealer_hand.append(dealer_card)

def the_count(player_hand,dealer_hand, count):
    all_cards = []
    for i in player_hand:
        all_cards.append(i)
    for i in dealer_hand:
        all_cards.append(i)
    for i in all_cards:
        if i == 10 or i == 'J' or i == 'Q' or i == 'K' or i == 'A':
            count = count - 1
        elif i < 6:
            count = count + 1
    print("The count is {}".format(count))
    return count

def play(deck, player_hand, dealer_hand):
    global count
    print("There are currently {} cards in the shoe".format(len(deck)))
    deal(deck, player_hand, dealer_hand)
    print("You show {}. Dealer Shows {}".format(player_hand,dealer_hand[0]))
    score(dealer_hand)
    black_jack(dealer_hand)
    score(player_hand)
    black_jack(player_hand)
    hit(player_hand)
    score(player_hand)
    dealer_hit(dealer_hand)
    result(player_hand,dealer_hand)
    count = the_count(player_hand,dealer_hand, count)
    play_again()

play(deck, player_hand, dealer_hand)
