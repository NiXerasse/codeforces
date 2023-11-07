a = [chr(x) for x in [*range(65, 91), *range(97, 123)]]
def check(s, z):
    for i in range(1, len(s)):
        count = 0
        while i + count < len(s) and s[i + count] == s[count]:
            count += 1
        if z[i] != count:
            return False
    return True


def gen(z):
    s, c = [None] * len(z), 0
    s[0] = a[c]
    if z[0] != 0:
        return '!'
    for i in range(1, len(z)):
        if z[i]:
            for j in range(z[i]):
                if i + j >= len(s):
                    return '!'
                if s[i+j] is None:
                    s[i+j] = s[j]
                elif s[i+j] != s[j]:
                    return '!'
        elif s[i] is None:
            c = c + 1
            s[i] = a[c]
        elif s[i] == s[0]:
            return '!'

    return ''.join(s)

for _ in range(int(input())):
    n = int(input())
    *z, = map(int, input().split())
    s = gen(z)
    print(s if check(s, z) else '!')
