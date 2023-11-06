n,k = tuple([int(a) for a in input().split()])
rects = [] # (height,width)

for i in range(n):
    dimensions = tuple([int(a) for a in input().split()])
    rects.append(dimensions)

def groupDimensions(grp):
    # given an arr of rectangles (a group)
    # return the h,w and area of the rectangle that covers it all
    h,dummy = max(grp,key=lambda x:x[0])
    w = 0
    for dummy,rectW in grp:
        w += rectW

    return h,w,h*w

# start off with just one group
groupings = [rects]

# we have to cut the groupings up k-1 times
while True:
    maxSaved1 = 0 # this is for double slices in ONE group
    cutId = None,None,None  # groupId, cutStart, cutEnd

    remainingCuts = k-len(groupings) 
    if remainingCuts == 0:
        # cutting is done
        break

    # for choosing to use either two slices in ONE group or two slices in TWO groups
    maxSaved2 = [] # highest slices in each group

    for groupId,group in enumerate(groupings):
        # go into each group and find the best place to cut
        if len(group) == 1:
            # no cutting can be done in this group
            maxSaved2.append((None,None))
            continue

        # find the group's height and width
        groupH,groupW,groupA = groupDimensions(group)

        gMaxSaved2 = 0 
        gCutId = 0,0

        # cut off at the middle
        for startId in range(0,len(group)): 
            for endId in range(startId,len(group)):
                # calculate how much area is saved, 
                # startId is the first rect in new group
                # endId is the last rect in new group

                if startId == 0 and endId == len(group)-1:
                    # cutting off into one part / maintaining the group
                    continue
                
                elif startId == 0 or endId == len(group)-1:
                    # we cut off into two parts only
                    if startId == 0:
                        left = group[:endId+1]
                        right = group[endId+1:]

                    elif endId == len(group)-1:
                        left = group[:startId]
                        right = group[startId:]

                    leftH,leftW,leftA = groupDimensions(left)
                    rightH,rightW,rightA = groupDimensions(right)

                    saved = groupA - (leftA+rightA)

                    if saved > gMaxSaved2:
                        gMaxSaved2 = saved
                        gCutId = startId,endId

                else:
                    # we cut off into three parts
                    if remainingCuts == 1: # only one cut remaining
                        print("FIXME")
                        exit()

                    left = group[:startId]
                    middle = group[startId:endId+1]
                    right = group[endId+1:]
                    
                    # calculate their respective areas
                    leftH,leftW,leftA = groupDimensions(left)
                    middleH,middleW,middleA = groupDimensions(middle)
                    rightH,rightW,rightA = groupDimensions(right)

                    saved = groupA - (leftA+middleA+rightA)

                    if saved > maxSaved1:
                        maxSaved1 = saved
                        cutId = groupId,startId,endId

                #print(len(group),group,startId,endId,saved)
            
        maxSaved2.append((gMaxSaved2,gCutId))

    # determining whether to use 1 slice or two slice
    # TODO DEBUG HERE IF GOT PROBLEM
    highSaved = [(0,0,0,0),(0,0,0,0)]
    for gid in range(len(maxSaved2)):
        saved,gCutId = maxSaved2[gid]

        if saved == None:
            continue

        minSaved = min(highSaved,key=lambda x:x[0])
        minVal = minSaved[0]
        if saved > minVal:
            highSaved.remove(minSaved)

            startId,endId = gCutId
            highSaved.append((saved,gid,startId,endId))


    if (highSaved[0][0] + highSaved[1][0]) < maxSaved1:
        # cutting twice in one group is better than cutting twice in two different groups 
        print("SAME GRP SLICE")
        print(cutId)
        gi,si,ei = cutId 
        split = [groupings[gi][:si]] + [groupings[gi][si:ei+1]] + [groupings[gi][ei+1:]]
        groupings = groupings[:gi] + split + groupings[gi+1:] 

    else:
        # cutting twice in two different groups is better than cutting twice in one group
        print("DIFF GRP SLICE")
        highSaved.sort(key=lambda x:x[1]) # the smaller gid is in front
        print(highSaved,cutId)

        dummy,gi1,si1,ei1 = highSaved[0]
        dummy,gi2,si2,ei2 = highSaved[1]

        if si1 == 0:
            split1 = [groupings[gi1][:ei1+1]] + [groupings[gi1][ei1+1:]]
        else:
            split1 = [groupings[gi1][:si1]] + [groupings[gi1][si1:]]

        if si2 == 0:
            split2 = [groupings[gi2][:ei2+1]] + [groupings[gi2][ei2+1:]]
        else:
            split2 = [groupings[gi2][:si2]] + [groupings[gi2][si2:]]

        groupings = groupings[:gi1] + split1 + groupings[gi1+1:gi2] + split2 + groupings[gi2+1:] 

    print([len(group) for group in groupings])
    print("XXX"*30)


# calculate the area of all the groupings
totalA = 0
for group in groupings:
    print(len(group),end=", ")
    h,w,a = groupDimensions(group)
    totalA += a

print()
print(totalA)
