print("Euler 4")
low = 100
high = 999
i = high * high
stop = low * low
done = 0

while i > stop:
    s = str(i)
    l = len(s)-1
    if s[0] == s[l] and s[1] == s[l-1] and s[2] == s[l-2]:
        for j in range(high, low, -1):
            if i%j == 0 and i/j>low and i/j<=high:
                print(i, j, i/j)
                done = 1
                break
    if done: break
    i -= 1
