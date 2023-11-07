for _ in range(int(input())):
    s, t = input(), input()
    count, i_start = 0, 0
    for i in range(len(s)):
        if s[i:i+len(t)] == t:
            E = i + len(t) - 1
            count += (E - i_start) * (E - i_start + 1) // 2 - (E - i - 1) * (E - i) // 2
            i_start = i + 1
    count += (len(s) - i_start) * (len(s) - i_start + 1) // 2
    print(count)
