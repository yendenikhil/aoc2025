D = []
with open('1.in', 'r') as file:
  for line in file:
      D.append([line[0], int(line[1:].strip())])

curr = 50
p1 = 0
p2 = 0
for [d, dist] in D:
    for _ in range(dist): 
        if d == 'L':
            curr -= 1
        else:
            curr += 1
        if curr == 0 or curr == 100:
            # print('>', d, dist, curr, p1, p2)
            p2 += 1
        if curr == -1:
            curr = 99
        elif curr == 100:
            curr = 0
    if curr == 0:
        p1 += 1
    #print(d, dist, curr, p1, p2)


print(p1)
print(p2)
