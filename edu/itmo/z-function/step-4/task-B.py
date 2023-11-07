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
for i in range(0, len(lines), 2):
    s, t = lines[i].strip(), lines[i+1].strip()
    z = get_z(t + '$' + s + s)
    p = len(t) + 1
    while z[p] != len(t) and p < len(s) + len(t) + 1:
        p += 1
    if p < len(s) + len(t) + 1:
        r.append(p - len(t) - 1)
    else:
        r.append(-1)
sys.stdout.write('\n'.join(map(str, r)))
