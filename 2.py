import re
D = []
p1 = []
p2 = []
with open('2.in', 'r') as file:
  for line in file:
      for e in line.strip().split(','):
          D.append([ int(x) for x in e.split('-')])
for [a, b] in D:
    for x in range(a, b + 1):
        # print(x)
        res = bool(re.fullmatch(r"(.+)\1", str(x)))
        res2 = bool(re.fullmatch(r"(.+)\1+", str(x)))
        # print(res)
        if res:
            p1.append(x)
        if res2:
            p2.append(x)
print(sum(p1))
print(sum(p2))
