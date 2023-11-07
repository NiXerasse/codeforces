for _ in range(int(input())):
    s = input()
    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            count += (s[i : j] == s[: j - i]) + (s[i : j] == s[-(j - i):]) == 1
    print(count)
