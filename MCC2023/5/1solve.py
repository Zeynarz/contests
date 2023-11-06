import sys
n,k = tuple([int(a) for a in input().split()])
rects = [] # (height,width)

for i in range(n):
    dimensions = tuple([int(a) for a in input().split()])
    rects.append(dimensions)

# deal with the special cases first
if k == 1:
    # one blue rectangle to cover everything
    blueH = max(rects,key=lambda x: x[0])[0]
    blueW = 0
    for h,w in rects:
        blueW += w

    print(blueH*blueW)

elif k >= n:
    # no groupings or anything needs to be done, just calculate total volume
    pass

else:
    # 1 < k < n
    # have to divide the rectangles into k groups

    # group up the red rectangles with same heights as they waste no space
    group = []
    groupN = 0
    rects = [(0,0)] + rects # so that the first few could be grouped if there is grouping
    for index in range(n,-1,-1):
        # go from behind, so that manipulating the arr wont mess up the indexes
        rect = rects[index]
        h,w = rect
        if group:
            if h == group[0][0]:
                # able to be grouped together
                group.append(rect)
                groupN += 1
            else:
                # group ends
                if groupN > 1:
                    blueH = max(group,key=lambda x: x[0])[0]
                    blueW = 0
                    for h,w in group:
                        blueW += w

                    blueRect = (blueH,blueW)
                    
                    # replace the red rects
                    rects = rects[:index+1] + [blueRect] + rects[index+groupN+1:]

                # if no grouping happens, then we just leave the rectangles be
                # reset the group
                group = [rect]
                groupN = 1

                
        else:
            # first rectangle, thus initiate a group
            group = [rect]
            groupN = 1

    rects.pop(0)

    # ---------------------------------------------------------------------------------
    
    rectsN = len(rects)
    if rectsN > k:
        # not enough grouping
        g = rectsN - k # still need to do g groupings

        # group according to heights
        heights = []
        for i in range(rectsN):
            heights.append((rects[i][0],i))

        heights.sort(key=lambda x:x[0])

        startChg,offset = 0,0
        while g > 0:
            for i in range(len(heights)-1):
                # check to see if this height can combine with next height
                h1,i1 = heights[i]
                h2,i2 = heights[i+1]

                maxH = max(h1,h2)
                mergedW = rects[i1][1] + rects[i2][1]
                canGroup = True

                furtherI, closerI = max(i1,i2), min(i1,i2)
                for h,w in rects[closerI+1:furtherI]:
                    mergedW += w 
                    if h > maxH:
                        canGroup = False
                        break

                if canGroup:
                    # they can merge
                    # so merge and break out
                    mergedRect = (maxH,mergedW)
                    rects = rects[:closerI] + [mergedRect] + rects[furtherI+1:]

                    # heights will be altered too
                    heights = heights[:i] + [(maxH,closerI)] + heights[i+2:]
                    offset = furtherI-closerI
                    for j in range(len(heights)-1,-1,-1):
                        h,rectIndex = heights[j]
                        if rectIndex > furtherI:
                            # index needs to be altered
                            heights[j] = (h,rectIndex-offset)

                        elif closerI < rectIndex < furtherI:
                            # this rect is now gone
                            heights.pop(j)
                    
                    # groupings made
                    g -= offset

                    break

            


# print out the total volume
if k != 1:
    print(rects)
    blueA = 0
    for h,w in rects:
        blueA += h*w
    
    print(blueA)
