def isPal(i):
    # works only on even size ints, suffices for this prob
    # being palindromic is not a property of a number, must use strings
    s = str(i)
    l = len(s)
    for v in range(int(l/2)):
        if s[v] == s[l-v-1]:
            v += 1
        else:
            return 0
    return 1

def main(size):
    low = 10 ** (size - 1)
    high = 10 ** size - 1
    i = high * high
    stop = low * low
    done = 0
    while i > stop:
        if isPal(i):
            for j in range(high, low, -1):
                if i%j == 0 and i/j>low and i/j<high:
                    print(i, "(", j, int(i/j), ")")
                    done = 1
                    break
        if done: break
        i -= 1

if __name__ == "__main__":
    print("Euler 4:")
    main(3)
