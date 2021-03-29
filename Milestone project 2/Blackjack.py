# GAME BLACKJACK

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Card:

    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):
        return f'Card {self.rank} of {self.suit} has a value {self.value}'

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

    def shuffle(self):
        return random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

# GAME LOGIC
print('Welcome to Blackjack, first place a bet and then we can start.\n'
      '==============')

my_deck = Deck()
my_deck.shuffle()

player_jack = Player ('Jack')
player_pc = Player ('PC')
player_jack.place_bet()


player_jack.take_one(my_deck.deal_one())
player_jack.take_one(my_deck.deal_one())

print(player_jack.player_cards[0], '\n',player_jack.player_cards[1])

print('Value of the cards is ', player_jack.player_cards[0].value + player_jack.player_cards[1].value )








