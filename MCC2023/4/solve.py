n,k = tuple([int(a) for a in input().split()])
arr = [int(a) for a in input().split()]

def binSearch(arr,num):
    # returns the largest index, where arr[index] <= num
    si,li = 0,len(arr)-1

    while si != li:
        midpoint = ((si+li)//2) + 1

        if arr[midpoint][0] <= num:
            si = midpoint

        else:
            li = midpoint - 1

    return si 

# remove duplicates and sort arr
arr = list(set(arr))
arr.sort()

# find the existing runs
# the (A1,A1),(A1+A2,A2),... things
runs = []
runsChain = [0]
gapsChain = [(0,0)]

prevNum = arr[0]
currentRun = 1
for current in arr[1:]:
    if prevNum+1 == current:
        # the run goes on
        currentRun += 1
    else:
        # the run dies
        runs.append(currentRun)
        runsChain.append(currentRun + runsChain[-1])
        currentRun = 1

        # find the gaps
        gap = current - prevNum - 1
        gapsChain.append((gap + gapsChain[-1][0],gap))

    prevNum = current

runs.append(currentRun) # add the last run
runsChain.append(currentRun + runsChain[-1])

# test out all combinations of filling up the gaps
ans = 0
start = 1 # start index of runsChain, start 2 indicates A1+A2
gapsFilled = binSearch(gapsChain,k)
end = gapsFilled # end index of gapsChain

runsN = len(runsChain)
gapsN = len(gapsChain)

# until the last run has been used
while True: 
    linkedRuns = runsChain[start+gapsFilled] - runsChain[start-1] + k

    if linkedRuns > ans:
        print(arr[start:start+gapsFilled+1])
        ans = linkedRuns

    if (start+gapsFilled) == (runsN-1):
        # last run is alr used
        break


    # setup for next run link 
    if gapsFilled == 0:
        wildcardsAvail = k
    else:
        # k - how many wildcards I have used alr
        wildcardsAvail = k - (gapsChain[end][0] - gapsChain[start+1][0])
        gapsFilled -= 1

    start += 1
    
    # when the start exceeds the end, cause by no gaps being filled
    if start > end:
        end = start

    # fill in more gaps if can
    while (end+1) < gapsN and gapsChain[end+1][1] <= wildcardsAvail:
        wildcardsAvail -= gapsChain[end+1][1]
        gapsFilled += 1
        end += 1

print(ans)
