from functools import reduce
from fractions import gcd
# def lcm
def lcm(a,b):
    return a*b//gcd(a,b)

a = reduce(lcm,range(1,20+1))
print(a)