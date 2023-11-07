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

input = sys.stdin.readline
inputs = sys.stdin.readlines

r = []
for line in inputs()[1:]:
    s = line.strip()
    z = get_z(s)
    i = min([i for i in range(1, len(s)) if i + z[i] == len(s)], default=len(s))
    r.append(s[:i])
print('\n'.join(r))
