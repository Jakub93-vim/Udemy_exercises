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
        return f'Card {self.rank} of {self.suit}'


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

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):

        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
       self.total -= self.bet

# FUNCTIONS

def take_bet(chips):

    while True:
        try:
            chips.bet = int(input('Place a bet: '))

        except:

            print('Write only a number')

        else:
            print('Bet accepted')
            break

def hit(deck, hand):

    hand.add_card(deck.deal_one())
    hand.adjust_for_ace()



def hit_or_stand(deck, hand):

    global playing
    playing = True

    while True:


        player_choice = input('Do you want to hit or stand ? (H/S)')

        if player_choice == 'H':
            hit(deck, hand)
            print(f'Your cards have value {hand.value}')

        elif player_choice == 'S':
            print('Player stands, dealer will play')
            playing = False

        else:
            print('Answer H or S please')
            continue
        break

def show_some(player, dealer):
    print("\nDealer's cards: ")
    print(" <card hidden>")
    print(dealer.card[1])
    print("\nPlayer's cards: ")
    print(*player.card, sep= '\n')


def show_all(player, dealer):
    print(f"\nDealer's cards, value is {dealer.value} ")
    print(*dealer.card, sep='\n')
    print(f"\nPlayer's cards, value is {player.value} ")
    print(*player.card, sep='\n')

def player_busts(player, dealer, chips):

    print(f'Player busts, value of his cards is {player.value}\n '
          f'dealer had {dealer.value} and chips of player are {chips.total}')

def player_wins(player):

    pass

player_chips = Chips()
take_bet(player_chips)
print(player_chips.total)
player_chips.lose_bet()

print(player_chips.total)




my_deck = Deck()
my_deck.shuffle()
player = Hand()
dealer = Hand()
dealer.add_card(my_deck.deal_one())
dealer.add_card(my_deck.deal_one())

player.add_card(my_deck.deal_one())
player.add_card(my_deck.deal_one())

show_some(player,dealer)

show_all(player,dealer)

hit_or_stand(my_deck,player)

player_busts(player,dealer,player_chips)







