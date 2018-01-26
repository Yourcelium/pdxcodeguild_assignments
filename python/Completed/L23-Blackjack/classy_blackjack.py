    from random import shuffle

'''

    This is Blackjack

'''

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '{} of {}'.format(self.rank, self.suit)

    def __repr__(self):
        return self.__str__()


class Deck:
    def __init__(self, shoe=0):
        self.deck = self.create_deck()
        self.shoe = self.create_shoe(shoe)
        self.count = 0

    def create_deck(self):
        temp_deck = []
        for i in range(2, 15):
            temp_deck.append(Card('Hearts', i))
        for i in range(2, 15):
            temp_deck.append(Card('Spades', i))
        for i in range(2, 15):
            temp_deck.append(Card('Clubs', i))
        for i in range(2, 15):
            temp_deck.append(Card('Diamonds', i))
        for i in temp_deck:
            if i.rank == 11:
                i.rank = 'J'
            if i.rank == 12:
                i.rank = 'Q'
            if i.rank == 13:
                i.rank = 'K'
            if i.rank == 14:
                i.rank = 'A'
        return temp_deck

    def __str__(self):
        return '{}'.format(self.deck)

    def __repr__(self):
        return self.__str__()

    def create_shoe(self, num_of_shoes):
        shoe = []
        for i in range(num_of_shoes):
            shuffle(self.deck)
            for p in self.deck:
                shoe.append(p)
        return shoe


class Hand:
    def __init__(self, name):
        self.hand = []
        self.name = name

    def __str__(self):
        return '{}'.format(self.name)

    def __repr__(self):
        return self.__str__()

    def look(self):
        print(self.hand)

    def clear(self):
        self.hand = []

    def get_card(self, deck):
        crd = deck.pop()
        self.hand.append(crd)
        # if crd.rank == 10 or crd.rank == 'J' or crd.rank == 'Q' or crd.rank == 'K' or crd.rank == 'A':
        #     deck.count = deck.count + 1
        # elif crd.rank > 6 and crd.rank < 9:
        #     deck.count = deck.count + 1

    def score(self):
        total = 0
        for i in self.hand:
            if i.rank == 'J' or i.rank == 'Q' or i.rank == 'K':
                total += 10
            elif i.rank == 'A':
                if total <= 10:
                    total += 11
                else:
                    total += 1
            else:
                total = total + int(i.rank)
        return total

    def hit(self, deck):
        while True:
            hit = input('{} Turn: To hit type 1, to stay type anything else\n>>'.format(self.name))
            if hit == '1':
                self.hand.append(deck.pop())
                print('{} show\'s a {}'.format(self.name, self.hand))
                if self.score() == 21:
                    print('21! Nice')
                    break
                elif self.score() > 21:
                    print('Bust')
                    break
                else:
                    print('You are now showing {}'.format(self.hand))
            else:
                break

    def dealer_hit(self, deck):
        while self.score() < 17:
            self.hand.append(deck.pop())
        print('Dealer shows {}'.format(self.hand))

    def check_split(self):



class Blackjack:
    def __init__(self, num_of_shoe):
        self.deck = Deck().create_shoe(num_of_shoe)
        self.count = 0

    def get_count(self, players):
        for player in players:
            cards = player.hand
            for crd in cards:
                if crd.rank == 10 or crd.rank == 'J' or crd.rank == 'Q' or crd.rank == 'K' or crd.rank == 'A':
                    self.count = self.count - 1
                elif crd.rank < 7:
                    self.count = self.count + 1
        print('The count is now {}'.format(self.count))

    def game(self):
        dealer = Hand('Dealer')
        burn_card = Hand('Burn Pile')
        burn_card.get_card(self.deck)
        how_many_players = int(input('How many players would you like at the table?\n>'))
        players = []
        for i in range(how_many_players):
            players.append(Hand(input('Player Name\n>')))
        for player in players:
            player.get_card(self.deck)
            print('{} shows {}'.format(player.name, player.hand))
        dealer.get_card(self.deck)
        print('Dealer shows {}'.format(dealer.hand))
        for player in players:
            player.get_card(self.deck)
            print('{} shows {}'.format(player.name, player.hand))
        dealer.get_card(self.deck)
        for player in players:
            player.hit(self.deck)
        dealer.dealer_hit(self.deck)
        for player in players:
            if player.score() > dealer.score():
                print('{} wins!'.format(player))
            elif player.score() == dealer.score():
                print('Push')
            elif dealer.score() > player.score():
                print('Dealer Wins')
        self.get_count(players)

    def again(self):
        q = input('To pay again type 1, to exit type 2\n>')
        if q == '1':
            self.game()
        elif q == '2':
            exit()
        else:
            q = input('I didn\'t understand that command\n To pay again type 1, to exit type 2\n>')


if __name__ == '__main__':
    game1 = Blackjack(2)
    game1.game()
