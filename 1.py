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

def ep3o(max):
    # build a list of primes
    primes = [2]
    i = 3   # to skip even numbers
    while i < max/2:  # past /2 won't be a factor
        notp = 0
        for j in primes:
            if i % j == 0:
                notp = 1
                break
        if notp == 0: primes.append(i)
        i += 2

    # find the largest prime factor of max
    for i in reversed(primes):
        if max % i == 0:
            return i

def ep3(max, primes, pfs):
    for p in primes:
        if max % p == 0:
            pfs.append(p)
            return ep3(max/p, primes, pfs)

    np = primes[-1] + 1
    while np <= max:
        notp = 0
        for x in primes:
            if np % x == 0:
                notp = 1
                break
        if notp:
            np += 1
        else:
            primes.append(np)
            if max % np == 0:
                pfs.append(np)
            return ep3(max, primes, pfs)

    return pfs[-1]

print "ep1:", ep1(1000)
print "ep2:", ep2(4*1000*1000)
#print "ep3:", ep3(901, primes=[2], pfs=[])
