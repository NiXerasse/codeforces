def z(k, i):
    if i % 2 or i == 0:
        return 0
    M = 2**(k-1)
    if i == M:
        return M - 1
    if i > M:
        return z(k - 1, i - M)
    else:
        return z(k - 1, i)

for _ in range(int(input())):
    k, j = map(int, input().split())
    print(z(k, j))
    