import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:
    def __init__(self, suit, rank) -> None:
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self) -> str:
        return self.rank + " of " + self.suit

class Deck:
    def __init__(self) -> None:
        self.all_cards = []

        #Create exactly one cards for all suits
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle (self):
        #Shuffle all cards inside deck
        random.shuffle(self.all_cards)

    def draw_one (self):
        #Deal one card from top of the deck
        return self.all_cards.pop()

class Player:
    def __init__(self, name) -> None:
        self.name = name
        #Define the deck that the Player have
        self.all_cards = []

    def __str__(self) -> str:
        return f'Player name is {self.name} has {len(self.all_cards)} cards'

    def draw_card(self):
        #Draw only first card on top of the deck
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        #We could determine if we add single card (as single object) or multiple cards (as list object)
        
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

#Game Setup
#1: Create initial player
player_one = Player("One")
player_two = Player("Two")

#2: Create card deck
new_deck = Deck()
#3: Shuffle the deck
new_deck.shuffle()

#4: Split it into both player
for x in range(26):
    player_one.add_cards(new_deck.draw_one())
    player_two.add_cards(new_deck.draw_one())

#5: Game state
game_state = True

round_number = 0
while game_state:
    round_number += 1
    print(f"Round {round_number}")
    
    #6: Checking their hands
    if len(player_one.all_cards) == 0:
        print("Curently Player One out of cards! Player Two Wins!")
        game_state = False

    if len(player_two.all_cards) == 0:
        print("Curently Player Two out of cards! Player One Wins!")
        game_state = False

    #Start Round
    player_one_cards = []
    player_one_cards.append(player_one.draw_card())

    player_two_cards = []
    player_two_cards.append(player_two.draw_card())

    print(f"Player One Cards: {player_one_cards[-1]} vs. Player Two Cards: {player_two_cards[-1]}")

    #7: War Condition
    war_state = True

    while war_state:
        #First Condition: Player One Wins
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            war_state = False
        
        #Second Condition: Player Two Wins
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            war_state = False

        #War
        else:
            print("Entering War...")

            #8: Check the card both player have
            if len(player_one.all_cards) < 3:
                print("Player One unable to play war! Game Over! Player Two Wins!")
                game_state = False
                break

            elif len(player_two.all_cards) < 3:
                print("Player One unable to play war! Game Over! Player Two Wins!")
                game_state = False
                break

            #9: Stay at War because both player have enough card
            else:
                for num in range(3):
                    player_one_cards.append(player_one.draw_card())
                    player_two_cards.append(player_two.draw_card())

        