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

def check(s, p):
    if len(p) != len(s):
        return 'No'
    x = p + s
    z = get_z(p + s)
    b = max([z[i] for i in range(len(s), len(x)) if i + z[i] == len(x)], default=0)
    mid = x[b:len(x)-b]
    if mid == mid[::-1]:
        return f'Yes\n{len(s) - b}'
    else:
        return 'No'

s, p = sys.stdin.readline().strip(), sys.stdin.readline().strip()
print(check(s, p))
