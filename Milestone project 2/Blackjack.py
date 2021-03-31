# GAME BLACKJACK

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:

    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):
        return f'Card {self.rank} of {self.suit}'

class Player:

    def __init__(self,name):
        self.name = name
        self.player_cards = []
        self.bank_roll = 1000

    def take_one(self,new_card):
        self.player_cards.append(new_card)

    def place_bet(self):
        bet = input(f'Bankroll is {self.bank_roll}, place a bet: ')
        self.bank_roll = self.bank_roll - int(bet)
        print(f'Your bankroll is {self.bank_roll}')

    def __str__(self):
        return f'You have cards {self.player_cards}'

class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                new_card = Card (rank, suit)
                self.all_cards.append(new_card)

    def __str__(self):
        print_deck = ''
        for card in self.all_cards:
            print_deck += card.__str__() + '\n'
        return print_deck

    def shuffle(self):
        return random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Hand:

    def __init__(self):
        self.card = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.card.append(card)

        self.value = 0
        for one_card in self.card:
            self.value += one_card.value

        return self.value

    def adjust_for_ace(self):

        if 'Ace' in self.card and self.value > 21:
            pass

class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        return self.total + self.bet

    def lose_bet(self):
        return self.total - self.bet

# FUNCTIONS

def take_bet():

    chips.bet = int(input('Place a bet: '))

    try:
        chips.bet = int(input('Place a bet: '))

    except:

        print('Put number')

    else:
        print('ok')


take_bet()




my_deck = Deck()
my_deck.shuffle()
my_hand = Hand()

my_hand.add_card(my_deck.deal_one())
print(my_hand.value)
my_hand.add_card(my_deck.deal_one())
print(my_hand.value)
my_hand.add_card(my_deck.deal_one())


print(my_hand.card[0],my_hand.card[1],my_hand.card[2])
print(my_hand.value)







