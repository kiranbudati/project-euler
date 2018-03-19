import time
start = time.time()

def collatz(n):
    arr = []
    if len(arr) == 0:
        arr.append(n)
        if n % 2 == 0:
            a = n/2
            arr.append(a)
        else:
            b = (3*n) + 1
            arr.append(b)

        for i in range(len(arr)):
            while arr[-1]!=1:
                if arr[-1] % 2 == 0:
                    c = arr[-1]/2
                    arr.append(c)
                else:
                    d = (3*arr[-1]) + 1
                    arr.append(d)
    return arr

my_list = []
for i in range(1,1000000):
    my_list.append([len(collatz(i)),i])
sor_ar = sorted(my_list)
print sor_ar[-1]
print('Time:', 1000*(time.time() - start))
