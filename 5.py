TODO:   getFactor needs to sort the list
The number 6 drops a second 3 in the list unnecessarily


def isPrime(lPrimes, n):
    for i in lPrimes:
        if n % i == 0:
            return 0
    return 1

def getFactors(lFacs, n):
    for i in lFacs:
        if n % i == 0 and n / i > 1:
            print(n)
            lFacs.append(int(n/i))
            return getFactors(lFacs, int(n/i))
    return lFacs

def main(iStop):
    print("Euler 5:")
    lPrimes = []
    lFacs = []
    for i in range(2, iStop):
        print("--", i)
        if isPrime(lPrimes, i):
            lPrimes.append(i)
            lFacs.append(i)
            print("added a prime", lFacs)
        else:
            lFacs = getFactors(lFacs, i)
            print ("added a fac", lFacs)

    print("primes", lPrimes)
    print("facs", lFacs)

if __name__ == "__main__":
    main(7)
