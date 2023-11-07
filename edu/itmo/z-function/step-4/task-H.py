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
r, count = '', 0
for c in s[::-1]:
    r = c + r
    z = get_z(r)
    max_p = max(z) + 1
    count += (max_p + len(r)) * (len(r) - max_p + 1) // 2
print(count)
