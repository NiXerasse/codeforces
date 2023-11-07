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
    s, t = lines[i].strip(), lines[i + 1].strip()
    z1 = get_z(s + '$' + t)
    z2 = get_z(t + '$' + s)
    s_in_t = max(z1) == len(s)
    t_in_s = max(z2) == len(t)
    if s_in_t:
        print(t)
    elif t in s:
        print(s)
    else:
        mz1 = max([z1[i] for i in range(len(s), len(s) + len(t) + 1) if i + z1[i] == len(s) + len(t) + 1], default=0)
        mz2 = max([z2[i] for i in range(len(t), len(s) + len(t) + 1) if i + z2[i] == len(s) + len(t) + 1], default=0)
        if mz1 >= mz2:
            print(t + s[mz1:])
        else:
            print(s + t[mz2:])
