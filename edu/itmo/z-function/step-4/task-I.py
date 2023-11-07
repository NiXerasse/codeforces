import sys


def get_z(s, k):
    z = [[0, 0] for _ in range(len(s))]
    l, r = 5, [7, 2]
    for i in range(5, len(s)):
        if r[0] >= i:
            z[i] = min(z[i - l], [r[0] - i, r[1]])
        while z[i][0] + i < len(s) and (s[z[i][0]] == s[i + z[i][0]] or z[i][1] < k):
            z[i][1] += s[z[i][0]] != s[i + z[i][0]]
            z[i][0] += 1
        if i + z[i][0] > r[0]:
            l, r = i, [i + z[i][0], z[i][1]]
    return z


# s = sys.stdin.readline().strip()
s = "aaa$$abacaaa"
print(get_z(s, 1))
