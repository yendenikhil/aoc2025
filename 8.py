import math
# set this to true for part 1
isPart1 = True
lines = open('8.in')
C = []
for line in lines:
    C.append([ int(x) for x in line.strip().split(',')])
total = len(C)

CC = []
for i, c1 in enumerate(C[:-1]):
    for j, c2 in enumerate(C[i+1:]):
        d = pow(c1[0] - c2[0], 2) + pow(c1[1] - c2[1], 2) + pow(c1[2] - c2[2], 2)
        CC.append([d, tuple(c1), tuple(c2)])
# so we start with lowest distance
CC.sort(key= lambda x: x[0])
if isPart1:
    CC = CC[:1000]

V = [] # this will contain the list of sets, each set will be connected junction boxes

# for each pair j1 and j2, there can be only 2 entries found in V one which has j1 and other has j2
for d, j1, j2 in CC:
    found = []
    # find already parsed circuits with either j1 or j2
    for i, e in enumerate(V):
        if j1 in e or j2 in e:
            found.append(i)
    found.sort(reverse=True)
    # now add j1 and j2 and add the found circuits (max 2) to make one big circuit
    connect = set([j1, j2])
    for i in found:
        connect.update(V[i])
        del V[i] # remove found circuits
    if len(connect) == total:
        print('part2:', j1[0]*j2[0])
        break
    V.append(connect)
if isPart1:
    V.sort(key= lambda x: len(x), reverse=True)
    print(math.prod([len(e) for e in V[0:3]]))


