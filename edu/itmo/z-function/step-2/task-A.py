s = input()
z = [0] * len(s)
for i in range(1, len(s)):
    count = 0
    while i + z[i] < len(s) and s[i + z[i]] == s[z[i]]:
        z[i] += 1
print(*z)
