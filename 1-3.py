def ep1(max):
    i = 3
    total = 0
    while i < max:
        if i % 3 == 0 or i % 5 == 0:
            total += i
        i += 1
    return total

def ep2(max):
    prev = 1
    f = 2
    total = 0
    while f + prev < max:
        if f % 2 == 0: total += f
        pf = f
        f = f + prev
        prev = pf
    if f < max: total += f
    return total

def ReduceN(n, prime):
    success = 1
    while success:
        success = 0
        if n % prime == 0:
            success = 1
            n /= prime
    return n

def NextPrime(primes):
    i = primes[-1] + 1
    tryagain = 0
    while 1:
        for p in primes:
            if i % p == 0:
                tryagain = 1
                break
        if tryagain:
            i += 1
            tryagain = 0
        else:
            return i

def ep3(n):
    primes = [2]
    topgun = 1
    newp = 1

    while newp <= n:
        for p in primes:
            r = ReduceN(n, p)
            if r < n: topgun = p
            n = r

        newp = NextPrime(primes)
        primes.append(newp)

    return topgun

print "ep1:", ep1(1000)
print "ep2:", ep2(4*1000*1000)
print "ep3:", ep3(600851475143)
