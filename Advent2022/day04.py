handIn = open('input04.txt')

lines = (handIn.read()).split('\n')
assign = [l.split(',') for l in lines]

pairs = 0
pairs2 = 0

for f, s in assign:
    f = list(map(int, f.split('-')))
    s = list(map(int, s.split('-')))

    if (f[0] >= s[0] and f[1] <= s[1]) or (s[0] >= f[0] and s[1] <= f[1]):
        pairs += 1

    if (f[0] >= s[0] and f[1] <= s[1]) or (s[0] >= f[0] and s[1] <= f[1]) or (f[0] >= s[0] and f[0] <= s[1]) or (f[1] >= s[0] and f[1] <= s[1]):
        pairs2 += 1

print(pairs)
print(pairs2)