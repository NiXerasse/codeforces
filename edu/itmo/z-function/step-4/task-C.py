import sys

def get_z(s):
    z = [0] * len(s)
    l, r = 0, 1
    for i in range(1, len(s)):
        if r >= i:
            z[i] = min(z[i - l], r - i)
        while z[i] + i < len(s) and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i]
    return z

lines = sys.stdin.readlines()[1:]
r = []
for line in lines:
    s = line.strip()
    z = get_z(s)
    c = [1] * len(s)
    for zi in z:
        if zi:
            c[zi-1] += 1
    d = 0
    for i in range(len(s) - 1 - 1, -1, -1):
        c[i] += d
        if c[i] > d + 1:
            d = c[i] - 1
    r.append(' '.join(map(str, c)))
print('\n'.join(r))
