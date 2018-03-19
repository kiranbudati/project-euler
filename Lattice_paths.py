results = {}

def routes(a, b):
    if (a, b) in results:
        return results[a, b]
    elif a > b:
        r = routes(b, a)
    elif a == 0:
        r = 1
    else:
        r = routes(a - 1, b) + routes(a, b - 1)
    results[a, b] = r
    return r

print (routes(20,20))