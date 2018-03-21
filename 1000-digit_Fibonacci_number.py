f=[1,1]
def feb(n):
    for i in f:
        if len(str(i)) !=n:
        # if len(str(i))
            s=len(f)
            f.append(f[s-1]+f[s-2])
    return f

def remLow(fa):
    for j in range(len(fa)):
        if len(str(fa[j])) == 1000:
            print fa[j],j+1
my_f = feb(1000)
remLow(my_f)