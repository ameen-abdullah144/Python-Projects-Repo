#BLACK JACK

import random 

suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {
    'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 
    'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11
}
playing = True

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit
    
class Deck:

    def __init__(self):
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp=''
        for card in self.deck:
            deck_comp+='\n'+card.__str__()
        return 'This Deck has: '+deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card= self.deck.pop()
        return single_card
    
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0  # Track aces

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


    def __str__(self):
        hand_comp = ''
        for card in self.cards:
            hand_comp += '\n ' + card.__str__()
        return f'Hand contains: {hand_comp}\nHand value: {self.value}'


class Chips:
    def __init__(self):
        self.total = 500
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except ValueError:
            print('Sorry, please provide an integer.')
        else:
            if chips.bet > chips.total:
                print(f"Insufficient chips! You have: {chips.total}")
            else:
                break

def hit(deck,hand):

    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing
    while True:
        x = input('Hit or Stand? Enter h or s: ')
        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player stands. Dealer's turn.")
            playing = False
        else:
            print("Sorry, I didn't understand that. Please enter 'h' or 's'.")
            continue
        break

def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print(' ', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ') #this is the replacement of for loop, alse called astresic loop
    print(f"Dealer's Hand value: {dealer.value}")
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print(f"Player's Hand value: {player.value}")

def player_busts(chips):
    print("Player busts!")
    chips.lose_bet()


def player_wins(chips):
    print("Player wins!")
    chips.win_bet()


def dealer_busts(chips):
    print("Dealer busts! Player wins!")
    chips.win_bet()


def dealer_wins(chips):
    print("Dealer wins!")
    chips.lose_bet()


def push():
    print("Dealer and Player tie! It's a push.")

# Main Game Loop
while True:
    print('WELCOME TO BLACKJACK!')

    # Create and shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up the player's chips
    player_chips = Chips()

    # Prompt the player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    while playing:
        # Prompt for player to hit or stand
        hit_or_stand(deck, player_hand)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        # If player's hand exceeds 21, player busts
        if player_hand.value > 21:
            player_busts(player_chips)
            break

    

    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        # Show all cards
        show_all(player_hand, dealer_hand)

        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_chips)
        else:
            push()
            push()

    print(f"\nPlayer's total chips are at: {player_chips.total}")

    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n': ")
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thanks for playing!")
        break
            