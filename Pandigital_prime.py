1
def isPandigital(a):
    count = 10*[0]
    while a != 0:
        if count[a%10] == 1: return False
        count[a%10] += 1
        a /= 10
    return True
 
def genPandigitals():
    pandigitals = []
    for a in xrange(100, 1000):
        if not isPandigital(a): continue
        for b in xrange(max(1000 - a, a), 1000):
            if isPandigital((a*1000 + b)*10000 + a + b):
                pandigitals.append([a, b, a+b])
    return pandigitals
 
p = genPandigitals()
print "Smallest triple:", p[0]
print "All the triples:\n", p
