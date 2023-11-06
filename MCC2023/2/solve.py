from math import ceil
T = int(input())

def binSearch(arr,power):
    # search for index where 
    # p[index] < a, and p[index+1] >= a
    si = 0
    li = len(arr)-1

    while si != li:
        midpoint = ceil((si+li)/2)
        if arr[midpoint] < power:
            si = midpoint
        else:
            li = midpoint - 1

    return si
 
for z in range(T):
    n,a,b = tuple([int(i) for i in input().split()])
    p = [int(i) for i in input().split()] 

    p.sort()

    kills = 0
    index = 0
    while a < b and p:
        if a <= p[0]:
            # can't get any stronger
            break

        # could optimise this to only search from index-1 to n prob
        index = binSearch(p,a)
        
        a += p[index]
        p.pop(index)
        kills += 1

    if a >= b:
        print(kills)
    else:
        print(-1)
