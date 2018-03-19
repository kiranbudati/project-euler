def even_feb(limit):
    a,b = 0,1

    while a < limit:
        if not a %2:
            yield a

        a,b = b,a+b

print sum((even_feb(4000000)))
