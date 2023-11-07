substrings_are_equal = lambda s, x1, x2, y1, y2: all(s[x1 + d] == s[y1 + d] for d in range(x2 - x1))
for _ in range(int(input())):
    s = input()
    count = 0
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s) + 1):
            count += (substrings_are_equal(s, i, j, 0, j - i) +
                      substrings_are_equal(s, i, j, len(s) - (j - i), len(s))) == 1
    print(count)
