import sys


def count_sort(p, c):
    cnt, pos = [0] * n, [0] * n
    for ci in c:
        cnt[ci] += 1
    for i in range(1, n):
        pos[i] = pos[i - 1] + cnt[i - 1]
    p_new = [0] * n
    for pi in p:
        p_new[pos[c[pi]]] = pi
        pos[c[pi]] += 1
    c_new = [0] * n
    for i in range(1, n):
        prev, cur = (c[(p_new[i - 1] + (1 << k)) % n], c[p_new[i - 1]]), (c[(p_new[i] + (1 << k)) % n], c[p_new[i]])
        c_new[p_new[i]] = c_new[p_new[i - 1]] + (prev != cur)
    return p_new, c_new

s = sys.stdin.readline().strip() + '$'
n = len(s)
p, c, k = [i for _, i in sorted((c, j) for j, c in enumerate(s))], [0] * n, 0
for i in range(1, n):
    c[p[i]] = c[p[i - 1]] + (s[p[i]] != s[p[i - 1]])

while 1 << k < n:
    p = [(pi - (1 << k)) % n for pi in p]
    p, c = count_sort(p, c)
    k += 1

sys.stdout.write(' '.join(map(str, p)))
