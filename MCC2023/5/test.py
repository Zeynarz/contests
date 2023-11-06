n,k = tuple([int(a) for a in input().split()])
rects = [] # (height,width)

for i in range(n):
    dimensions = tuple([int(a) for a in input().split()])
    rects.append(dimensions)

diffs = []

for i in range(n-1):
    diff = abs(rects[i][0]-rects[i+1][0])
    diffs.append(diff)

    print(diff,rects[i][0],rects[i+1][0])

print(max(diffs))
