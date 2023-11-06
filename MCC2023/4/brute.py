# to help me find answers and see what's wrong with my solution
n,k = tuple([int(a) for a in input().split()])
arr = [int(a) for a in input().split()]

# remove duplicates and sort arr
arr = list(set(arr))
arr.sort()

# find the existing runs
runs = []
gaps = []
prevNum = arr[0]
currentRun = 1
for current in arr[1:]:
    if prevNum+1 == current:
        # the run goes on
        currentRun += 1
    else:
        # the run dies
        runs.append(currentRun)
        currentRun = 1
        gaps.append(current-prevNum-1)

    prevNum = current

runs.append(currentRun) # add the last run

# try out every run
ans = 0
for i in range(len(runs)):
    tempK = k
    gapsFilled = 0
    for gap in gaps[i:]:
        if tempK >= gap:
            tempK -= gap
            gapsFilled += 1
        else:
            break
    
    currentRun = sum(runs[i:i+gapsFilled+1]) + k 
    if currentRun > ans:
        ans = currentRun

print(ans)
