with open('large_sum_txt.txt',"r") as ap:
    arr = []

    for i in ap:
        arr.append(i)

farr = []

for i in arr:
    farr.append(int(i))

aSum = sum(farr)

print str(aSum)[:10 ]