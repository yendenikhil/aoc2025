import math
blocks = open('12.in').read().strip().split('\n\n')
p1 = 0
for line in blocks[-1].split('\n'):
    left, right = line.split(': ')
    area = math.prod(map(lambda x: x// 3, map(int, left.split('x'))))
    num = sum(map(int, right.split(' ')))
    if area >= num: p1 += 1
print(p1)
