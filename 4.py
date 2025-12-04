lines = open('4.in').read().splitlines()
G = []
for line in lines:
    G.append([x for x in line])
lenr = len(G[0])
lenc = len(G)
NN = [[-1, -1], [-1, 0], [-1,1],
      [1, -1], [1, 0], [1,1],
      [0, -1],[0,1],]
p1 = set()
counter = -1
# set to false for part 1
part2 = True
while len(p1) > counter:
    counter = len(p1)
    for r in range(lenr):
        for c in range(lenc):
            if G[r][c] == '@':
                rolls = []
                for dr, dc in NN:
                    nr = r + dr
                    nc = c + dc
                    if nr >= 0 and nr < lenr and nc >= 0 and nc < lenc and G[nr][nc] == '@':
                        rolls.append((nr, nc))
                if len(rolls) < 4:
                    p1.add((r,c))
                    if part2:
                        G[r][c] = '.'
    if part2 == False:
        break

print(len(p1))
