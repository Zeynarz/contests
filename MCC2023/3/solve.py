n,m = tuple([int(i) for i in input().split()])

# get all the cardSums
cards = []
for i in range(n):
    card = [int(a) for a in input().split()]
    cards.append(card)

cardSums = []  # a + b, c + d
sums = []   # a + b + c + d
for index,card in enumerate(cards):
    AB = card[0] + card[1]
    CD = card[2] + card[3]

    cardSums.append((AB,CD,index))
    sums.append((AB+CD,index))


# choose only using ABs
cardSums.sort(key=lambda x: x[0])
chosenCards = cardSums[n-m:]

ans = 0
highestCD = 0
alrUsedIs = []
for AB,CD,i in chosenCards:
    ans += AB
    alrUsedIs.append(i)

    if CD > highestCD:
        highestCD = CD

ans += highestCD
    
# see if got anyone can dethrone the head
sums.sort(key=lambda x: x[0])
for s,i in sums[-1::-1]:
    if i in alrUsedIs:
        continue

    else:
        # got the largest sum that we can use
        ansCopy = ans - chosenCards[0][0] - highestCD + s 
        if ansCopy > ans:
            ans = ansCopy
        break

print(ans)

