n,k = tuple([int(i) for i in input().split()])
arr = [int(i) for i in input().split()]

# straightforward approach
# this takes n*k iterations, task 7 only requires 696*696=484416 iterations,
# prob doable?

for i in range(n):
    for z in range(k):
        prevOdd = None 
        if prevOdd == None or prevOdd == False:
            # first iteration / dk if its currently even or odd
            if arr[i] % 2 == 0:
                prevOdd = False
                arr[i] //= 2
            else:
                prevOdd = True
                arr[i] = arr[i]*3 + 1

        elif prevOdd:
            # now its even
            prevOdd = False
            arr[i] //= 2

print(sum(arr))
