t = int(input())
for _ in range(t):
    s = input()
    max_l = 1
    for l in range(2, len(s) + 1):
        if all(s[p] == s[l - 1 - p] for p in range(l//2)):
            max_l = max(l, max_l)
    print(max_l)
