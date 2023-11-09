import sys


def get_z(s):
    z = [0] * len(s)
    l, r = 0, 1
    for i in range(1, len(s)):
        if r > i:
            z[i] = min(z[i - l], r - i)
        while z[i] + i < len(s) and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i]
    return z


s = sys.stdin.readline().strip()
p = sys.stdin.readline().strip()
k = int(sys.stdin.readline().strip())
z1 = get_z(p + "$" + s)
z2 = get_z(p[::-1] + "$" + s[::-1])
r = []
for i in range(len(s) - len(p) + 1):
    if len(p) - (z1[len(p) + i + 1] + z2[len(s) - i + 1]) <= k:
        r.append(i + 1)
sys.stdout.write(f'{len(r)}\n')
sys.stdout.write(' '.join(map(str, r)))
