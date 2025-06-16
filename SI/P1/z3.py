'''
First we take the cards and colors of the deck the player uses, then for each we calculate the probability of getting each hand.
Next, based on the rules of the game, we calculate the probability of winning with each hand.
We calculate the probability of winning by multiplying the probability of getting a hand by the probability of the opponent getting a hand that is worse.
We also calculate the probability of getting higher hand than opponent to resolve the draws in hands.
'''
from itertools import product, combinations

class Player:
    def __init__(self, cards, suits):
        self.cards = cards
        self.suits = suits
        self.pair_prob = 0
        self.two_pairs_prob = 0
        self.three_of_kind_prob = 0
        self.straight_prob = 0
        self.flush_prob = 0
        self.full_prob = 0
        self.four_of_kind_prob = 0
        self.straight_flush_prob = 0
        self.royal_flush_prob = 0
        self.higher_hand_prob = 0
        self.hand_combinations = list(combinations(product(self.cards, self.suits), 5))
        self.calculate_probabilities()
        self.all_probabilities = [self.royal_flush_prob, self.straight_flush_prob, self.four_of_kind_prob, self.full_prob,
                                  self.flush_prob, self.straight_prob, self.three_of_kind_prob, self.two_pairs_prob,
                                  self.pair_prob, self.higher_hand_prob]
    
    def is_royal_flush(self, comb):
        values = [x[0] for x in comb]
        suits = [x[1] for x in comb]
        if set(values) == set([10, 11, 12, 13, 1]) and len(set(suits)) == 1:
            return True
        return False
    
    def is_straight_flush(self, comb):
        values = [x[0] for x in comb]
        suits = [x[1] for x in comb]
        if len(set(suits)) == 1 and max(values) - min(values) == 4: #because only moment when we numbers not in order is in royal flush
            return True
        return False
    
    def is_four_of_kind(self, comb):
        values = [x[0] for x in comb]
        for value in values:
            if values.count(value) == 4:
                return True
        return False
    
    def is_full(self, comb):
        values = [x[0] for x in comb]
        count = [values.count(x) for x in set(values)]
        if 3 in count and 2 in count:
            return True
        return False
    
    def is_flush(self, comb):
        suits = [x[1] for x in comb]
        if len(set(suits)) == 1:
            return True
        return False
    
    def is_straight(self, comb):
        values = [x[0] for x in comb]
        if (max(values) - min(values) == 4 and len(set(values)) == 5) or set(values)==set([10,11,12,13,1]):
            return True
        return False

    def is_three_of_kind(self, comb):
        values = [x[0] for x in comb]
        for value in values:
            if values.count(value) == 3:
                return True
        return False

    def is_two_pairs(self, comb):
        values = [x[0] for x in comb]
        count = [values.count(x) for x in set(values)]
        if count.count(2) == 2:
            return True
        return False
    
    def is_one_pair(self, comb):
        values = [x[0] for x in comb]
        for value in values:
            if values.count(value) == 2:
                return True
        return False

    def calculate_probabilities(self):
        for comb in self.hand_combinations:
            if self.is_royal_flush(comb):
                self.royal_flush_prob += 1
            elif self.is_straight_flush(comb):
                self.straight_flush_prob += 1
            elif self.is_four_of_kind(comb):
                self.four_of_kind_prob += 1
            elif self.is_full(comb):
                self.full_prob += 1
            elif self.is_flush(comb):
                self.flush_prob += 1
            elif self.is_straight(comb):
                self.straight_prob += 1
            elif self.is_three_of_kind(comb):
                self.three_of_kind_prob += 1
            elif self.is_two_pairs(comb):
                self.two_pairs_prob += 1
            elif self.is_one_pair(comb):
                self.pair_prob += 1
            else:
                self.higher_hand_prob += 1
        self.royal_flush_prob /= len(self.hand_combinations) 
        self.straight_flush_prob /= len(self.hand_combinations) 
        self.four_of_kind_prob /= len(self.hand_combinations) 
        self.full_prob /= len(self.hand_combinations) 
        self.flush_prob /= len(self.hand_combinations) 
        self.straight_prob /= len(self.hand_combinations) 
        self.three_of_kind_prob /= len(self.hand_combinations) 
        self.two_pairs_prob /= len(self.hand_combinations) 
        self.pair_prob /= len(self.hand_combinations) 
        self.higher_hand_prob /= len(self.hand_combinations) 

    def print_probs(self):
        print("Royal flush probability:", self.royal_flush_prob)
        print("Straight flush probability:", self.straight_flush_prob)
        print("Four of a kind probability:", self.four_of_kind_prob)
        print("Full house probability:", self.full_prob)
        print("Flush probability:", self.flush_prob)
        print("Straight probability:", self.straight_prob)
        print("Three of a kind probability:", self.three_of_kind_prob)
        print("Two pairs probability:", self.two_pairs_prob)
        print("One pair probability:", self.pair_prob)
        print("Higher hand probability:", self.higher_hand_prob)
        print("Sum of all probabilities:", sum(self.all_probabilities))

def player_chance_win(player1, player2):
    win_chance = 0
    higher_card_win_prob = 0
    for card in player1.cards:
        higher_card_win_prob += 1/len(player1.cards) * sum(1 for c in player2.cards if (c<card and c!=1) or card==1)/len(player2.cards)

    # print("Higher card win probability:", player1.all_probabilities[-1] * higher_card_win_prob * player2.all_probabilities[-1])

    for i in range(len(player1.all_probabilities)-1):
        win_chance += player1.all_probabilities[i] * (sum(player2.all_probabilities[i+1:]) + player2.all_probabilities[i]*higher_card_win_prob)
        # prawd na niewylosowanie kart wiekszych niz karty gracza 1
        
    win_chance += player1.all_probabilities[-1] * higher_card_win_prob * player2.all_probabilities[-1]
    return win_chance


fig = [1, 11, 12, 13]
blot = [2, 3, 4, 5, 6, 7, 8, 9, 10]
suits = [1, 2, 3, 4]

figurarz = Player(fig, suits)
blotkarz = Player(blot, suits)

print("Blotkarz win chance: {:.10f}".format(player_chance_win(blotkarz, figurarz)))
print("Figurarz win chance: {:.10f}".format(player_chance_win(figurarz, blotkarz)))
print()

def options():
    highest_win_chance = 0
    highest_win_chance_deck = []

    for i in range(1, 5):
        for j in range(2, 11):
            cards = list(h for h in range(2, j+1))
            colors = list(h for h in range(1, i+1))
            if len(cards) * len(colors) >= 5:
                custom_blotkarz = Player(cards, colors)
                win = player_chance_win(custom_blotkarz, figurarz) * 100
                if win>=highest_win_chance:
                    highest_win_chance = win
                    highest_win_chance_deck = [cards, colors]
                print("Blotkarz with cards from 2 to", j, f"and {i} number of colors:")
                print(f"Win chance = {win}%")
                print()

    print()
    print("Highest win chance:", str(highest_win_chance) + "%")
    print("Deck:", highest_win_chance_deck)
    print()
# normal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# normal_player = Player(normal, suits)
# normal_player.print_probs()
