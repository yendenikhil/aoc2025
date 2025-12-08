first, *lines = open('7.in')

B = [0] * len(first)
B[first.index('S')] = 1
p1 = 0
for line in lines:
    for i, c in enumerate(line):
        if c == '^':
            if B[i] > 0:
                p1 += 1
            B[i-1] += B[i]
            B[i+1] += B[i]
            B[i] = 0

print(p1)
print(sum(B))
