lines = open('6.in').read().splitlines()
G = []
OP = []
p1 = []
p2 = []
for i, line in enumerate(lines):
    arr = []
    for e in line.strip().split(' '):
        if e != '' and i != len(lines) - 1:
            arr.append(int(e))
        elif e != '':
            arr.append(e)
    if i != len(lines) - 1:
        G.append(arr)
    else:
        OP = arr
for e in OP:
    if e == '*':
        p1.append(1)
        p2.append(1)
    else:
        p1.append(0)
        p2.append(0)

for arr in G:
    for i, e in enumerate(arr):
        if OP[i] == '*':
            p1[i] *= e
        else:
            p1[i] += e

#print(p1)
print(sum(p1))

lenlines = max(len(e) for e in lines)
arr = []
GG = []
for i in range(lenlines):
    if lines[-1][i] != ' ' and i > 0:
        arr1 = []
        for e in arr:
            if len(e.strip()) > 0:
                arr1.append(int(e.strip()))
        GG.append(arr1)
        arr = []
    num = ''
    for r, line in enumerate(lines[:-1]):
        if i < len(line):
            num = num + line[i]
    arr.append(num)
arr1 = []
for e in arr:
    if len(e.strip()) > 0:
        arr1.append(int(e.strip()))
GG.append(arr1)

for i, o in enumerate(OP):
    if o == '*':
        for e in GG[i]:
            p2[i] *= e
    else:
        for e in GG[i]:
            p2[i] += e


print(sum(p2))


