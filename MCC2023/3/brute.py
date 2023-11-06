from itertools import combinations

# to get answer for debugging
n,m = tuple([int(i) for i in input().split()])

# get all the cards
cards = []
for i in range(n):
    card = [int(a) for a in input().split()]
    cards.append(card)

maxNum = 0
bestI = 0
comboUsed = 0
for starI in range(n):
    starSum = sum(cards[starI])
    
    tmpCards = cards[:starI] + cards[starI+1:]
    sums = [card[0]+card[1] for card in tmpCards]
    
    combos = list(combinations(sums,m-1))

    for combo in combos:
        result = starSum + sum(combo)

        if result > maxNum:
            maxNum = result
            bestI = starI
            comboUsed = combo     

print("max result     : " + str(maxNum))
print("starCard used  : " + str(cards[bestI]))
print("combo used     : " + str(comboUsed))
print(cards)
