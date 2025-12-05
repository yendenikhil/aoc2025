blocks = open('5.in').read().strip().split('\n\n')
R = [] 
for curr in blocks[0].split('\n'):
    a, b = curr.split('-')
    R.append([int(a), int(b)])

# check overlapping ranges
R.sort(key= lambda x: x[0])
RR = []
curra, currb = R[0]
for a, b in R[1:]:
    if a <= currb: 
        currb = max(currb, b)
    else:
        RR.append([curra, currb])
        curra, currb = a, b
RR.append([curra, currb])

# solve
p1 = 0
for currid in blocks[1].split('\n'):
    for a, b in RR:
        if a <= int(currid) <= b:
            p1 += 1
            break
    
print(p1)
p2 = 0
for a, b in RR:
    p2 += b - a + 1
print(p2)
