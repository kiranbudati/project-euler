from itertools import count

def divisor_count(n):
    """Count of the divisors of n"""
    return sum(1 for divisor in xrange(1, n + 1) if n % divisor == 0)

for n in count(1):
    tn = n * (n + 1) // 2
    # n and (n + 1) are relatively prime.  Therefore, if n is even,
    # the factors of tn can be derived from the factors of n/2 and
    # the factors of n+1. If n is odd, then the factors of tn can be
    # derived from the factors of n and the factors of ((n+1)/2).
    tn_divisor_count = (
        divisor_count(n // 2) * divisor_count(n + 1) if n % 2 == 0 else
        divisor_count(n) * divisor_count((n + 1) // 2)
    )
    if tn_divisor_count >= 500:
        print tn
        break