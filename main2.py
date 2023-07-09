import random

# Card Class
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = self._get_card_value()

    def _get_card_value(self):
        if self.rank in ["J", "Q", "K"]:
            return 10
        elif self.rank == "A":
            return 11
        else:
            return int(self.rank)

    def __str__(self):
        return f"{self.rank}{self.suit}"


# Deck Class
class Deck:
    def __init__(self):
        self.cards = self._create_deck()

    def _create_deck(self):
        suits = ["♠", "♣", "♦", "♥"]
        ranks = [str(i) for i in range(2, 11)] + ["J", "Q", "K", "A"]
        deck = [Card(rank, suit) for suit in suits for rank in ranks]
        random.shuffle(deck)
        return deck

    def deal_card(self):
        return self.cards.pop()

    def reshuffle(self):
        self.cards = self._create_deck()
        random.shuffle(self.cards)


# Player Class
class Player:
    def __init__(self, name, initial_money):
        self.name = name
        self.hand = []
        self.money = initial_money
        self.bet = 0

    def receive_card(self, card):
        self.hand.append(card)

    def calculate_hand_value(self):
        value = sum(card.value for card in self.hand)
        num_aces = sum(card.rank == "A" for card in self.hand)
        while value > 21 and num_aces > 0:
            value -= 10
            num_aces -= 1
        return value

    def place_bet(self, amount):
        if amount <= self.money:
            self.bet = amount
            self.money -= amount
        else:
            print("Insufficient funds!")

    def win(self, amount):
        self.money += amount

    def __str__(self):
        return f"{self.name} (Money: {self.money})"


# Dealer Class
class Dealer:
    def __init__(self):
        self.hand = []

    def receive_card(self, card):
        self.hand.append(card)

    def calculate_hand_value(self):
        value = sum(card.value for card in self.hand)
        num_aces = sum(card.rank == "A" for card in self.hand)
        while value > 21 and num_aces > 0:
            value -= 10
            num_aces -= 1
        return value

    def __str__(self):
        return "Dealer"


# Game Class
class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player("Player", 100)
        self.dealer = Dealer()
        self.rounds_played = 0
        self.reshuffle_threshold = 5

    def check_reshuffle(self):
        if self.rounds_played >= self.reshuffle_threshold or len(self.deck.cards) < 10:
            self.deck.reshuffle()
            self.rounds_played = 0
            print("Deck reshuffled!")

    def start_round(self):
        self.player.hand = []
        self.dealer.hand = []
        self.player.place_bet(int(input("Welcome to Black Jack.  Enter your $bet amount: ")))
        self.check_reshuffle()

        for _ in range(2):
            self.player.receive_card(self.deck.deal_card())
            self.dealer.receive_card(self.deck.deal_card())

        self.display_table()
        self.play_player_turn()

    def play_player_turn(self):
        while True:
            action = input("Choose an action: [h]it, [s]tand: ").lower()
            if action == "h":
                self.player.receive_card(self.deck.deal_card())
                self.display_table()
                if self.player.calculate_hand_value() > 21:
                    self.end_round()
                    break
            elif action == "s":
                self.play_dealer_turn()
                break

    def play_dealer_turn(self):
        while self.dealer.calculate_hand_value() < 17:
            self.dealer.receive_card(self.deck.deal_card())
            self.check_reshuffle()
        self.end_round()

    def end_round(self):
        player_value = self.player.calculate_hand_value()
        dealer_value = self.dealer.calculate_hand_value()
        self.rounds_played += 1

        if player_value > 21:
            print("Player busts! Dealer wins.")
        elif dealer_value > 21:
            print("Dealer busts! Player wins.")
            self.player.win(self.player.bet * 2)
        elif player_value > dealer_value:
            print("Player wins!")
            self.player.win(self.player.bet * 2)
        elif dealer_value > player_value:
            print("Dealer wins.")
        else:
            print("It's a tie.")

        print(f"Player's Hand: {', '.join(str(card) for card in self.player.hand)}")
        print(f"Dealer's Hand: {', '.join(str(card) for card in self.dealer.hand)}")
        print(f"Player's Money: {self.player.money}")

    def display_table(self):
        print("Player's Hand:", ", ".join(str(card) for card in self.player.hand))
        print("Dealer's Hand:", ", ".join(str(card) for card in self.dealer.hand[:-1]) + ", Hidden Card")
        print("")



game = Game()
game.start_round()
