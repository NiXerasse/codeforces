for _ in range(int(input())):
    t = input()
    p = input()
    r, count = [], 0
    for i in range(len(t) - len(p) + 1):
        if all(c1 == c2 or c1 == '?' for c1, c2 in zip(p, t[i:])):
            count += 1
            r.append(i)
    print(count)
    print(*r)
