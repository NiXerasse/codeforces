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


s = sys.stdin.readline().strip()
z = get_z(s + s[:-1])
before = 0
for i in range(1, len(s)):
    if s[(i + z[i]) % len(s)] < s[z[i] % len(s)]:
        before += 1
print(before + 1)
