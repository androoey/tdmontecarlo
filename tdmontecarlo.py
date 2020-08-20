import random

#generating deck
deck = (["R"] * 7) + (["B"] * 5)
num_sims = 100000
blues_drawn = 0
reds_drawn = 0
red_wins = 0

for x in range(num_sims):
    random.shuffle(deck)
    for card in deck:
        if reds_drawn >= 2 or blues_drawn >= 4:
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

ratio = red_wins/num_sims
print(ratio)

