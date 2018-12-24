def ep1 (max):
    i = 3
    total = 0
    while i < max:
        if i % 3 == 0 or i % 5 == 0:
            total += i
        i += 1
    return total

def ep2 (max):
    prev = 1
    f = 2
    total = 0
    while f + prev < max:
        if f % 2 == 0: total += f
        pf = f
        f = f + prev
        prev = pf
    return total

print "ep1:", ep1(10)
print "ep2:", ep2(4*1000*1000)
