import sys
import itertools
n,k = tuple([int(a) for a in input().split()])
rects = [] # (height,width)

for i in range(n):
    dimensions = tuple([int(a) for a in input().split()])
    rects.append(dimensions)

def calcArea(combo):
    # calculate area of configuration combo
    combo = list(combo)
    
    area = 0
    rectPassed = 0
    for num in combo:
        group = rects[rectPassed:rectPassed+num]
        h,dummy = max(group,key=lambda x:x[0]) 
        w = 0
        for rh,rw in group:
            w += rw

        area += h*w

        rectPassed += num

    return area

"""
def sum_to_n(n, size, limit=None):
    if size == 1:
        yield [n]
        return
    if limit is None:
        limit = n
    start = (n + size - 1) // size
    stop = min(limit, n - size + 1) + 1
    for i in range(start, stop):
        for tail in sum_to_n(n - i, size - 1, i):
            yield [i] + tail

# this won't work for large ks
# its to be used to improve my solve.py
combos = [a for a in sum_to_n(n,k)] # combinations, not permutations yet
permutations = []

for combo in combos:
    permutations += list(itertools.permutations(combo))

ans = 99999999999999
ansCombo = None
for p in permutations:
    comboArea = calcArea(p)
    if comboArea < ans:
        ans = comboArea
        ansCombo = p

print(ans)
print(ansCombo)


# print out the rectangles
rectPassed = 0
for num in ansCombo:
    group = rects[rectPassed:rectPassed+num]
    h,dummy = max(group,key=lambda x:x[0]) 
    w = 0
    for rh,rw in group:
        w += rw

    print((h,w))
    rectPassed += num
"""

combo = [2, 2, 2, 1, 4, 2, 3, 8, 5, 4, 4, 1, 2, 2, 2, 4, 3, 2, 2, 1, 1, 3, 5, 3, 3, 2, 2, 4, 1, 1, 2, 1, 2, 2, 1, 2, 3, 1, 5, 5, 2, 1, 1, 1, 2, 1, 1, 1, 6, 1, 2, 3, 2, 1, 3, 1, 3, 3, 15, 1, 3, 10, 6, 3, 1, 3, 7, 1, 2]

minValue = 61969647

# lets just play around with this and see if we get lucky
comboCopy = list(combo)
for offset in range(1,10):
    for i in range(len(comboCopy)-1):
        if comboCopy[i] <= offset:
            continue
    
        comboCopy[i] -= offset
        comboCopy[i+1] += offset
    
        a = calcArea(comboCopy)
        if a < minValue:
            print(a)
            print("YOOOOO")
    
        comboCopy[i] += offset
        comboCopy[i+1] -= offset
        
