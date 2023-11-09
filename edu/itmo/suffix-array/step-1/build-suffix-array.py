import sys


def get_sa(s):
    eq, p = [None] * len(s), sorted((ord(c), i) for i, c in enumerate(s))

    def get_eq():
        cl = 1
        for i in range(len(p)):
            if i and p[i][0] != p[i - 1][0]:
                cl += 1
            eq[p[i][1]] = cl
        return cl

    cl, k = get_eq(), 1
    while cl < len(eq):
        p = sorted(((eq[i], eq[(i + 2**(k-1)) % len(s)]), i) for i in range(len(s)))
        cl, k = get_eq(), k + 1
    return [pi[1] for pi in p]


s = sys.stdin.readline().strip() + '$'
sa = get_sa(s)
sys.stdout.write(' '.join(map(str, sa)))
