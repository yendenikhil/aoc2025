lines = open('3.in').read().splitlines()
ans = 0
size = 12
# for part 1 uncomment size = 2
# size = 2
for line in lines:
    currline = line 
    digits = []
    for rem in range(size - 1, -1, -1):
        m = ''
        if rem == 0:
            m = max(c for c in currline[:])
        else:
            m = max(c for c in currline[:-1 * rem])
        digits.append(m)
        currline = currline[currline.index(m) + 1:]
    ans += int(''.join(digits))
        
print(ans)

