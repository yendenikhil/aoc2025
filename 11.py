lines = open('11.in').read().splitlines()
G = {}
for line in lines:
    left, right = line.split(': ')
    for e in right.split(' '):
        G[left] = right.split(' ')
memo = {}
def count(curr, dac, fft):
    #print(curr, dac, fft)
    if curr == 'out':
        if dac and fft: return 1 
        else: return 0
    if curr == 'dac': dac = True
    if curr == 'fft': fft = True
    if (curr, dac, fft) in memo: return memo[(curr, dac, fft)]
    ans =  sum(count(n, dac, fft) for n in G[curr])
    memo[(curr, dac, fft)] = ans
    return ans

print(count('you', True, True))
print(count('svr', False, False))

