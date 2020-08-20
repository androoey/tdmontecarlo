import random

#asking for input
print("How many blues to win?")
blues_needed = int(input())
print("How many reds to win?")
reds_needed = int(input())
print("How many blues in deck?")
blues_in_deck = int(input())
print("How many reds in deck?")
reds_in_deck = int(input())

#generating deck
deck = (["R"] * reds_in_deck) + (["B"] * blues_in_deck)
num_sims = 100000
blues_drawn = 0
reds_drawn = 0
red_wins = 0



for x in range(num_sims):
    random.shuffle(deck)
    for card in deck:
        if reds_drawn >= reds_needed or blues_drawn >= blues_needed:
            break
        if card == "R":
            reds_drawn += 1
            #print("Reds:%d" %reds_drawn)
        else:
            blues_drawn += 1
            #print("Blues:%d" % blues_drawn)
    if reds_drawn >= 2:
        red_wins += 1
    blues_drawn = 0
    reds_drawn = 0

ratio = 1 - (red_wins/num_sims)
print("Probability of lib td win is:" + str(ratio))

