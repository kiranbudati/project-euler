letters = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,
"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26,}

fname = "names.txt"

with open(fname) as na:
    for i in na:
        x = [x.strip() for x in eval(i)]

sort_name =[]
pos = []
print(len(x))
for j in range(len(x)):
    sort_name.append(''.join(sorted(x[j])))
    count = 0
    for ch in sort_name[j]:
        count += letters[ch]
    pos.append(count)
f_c = 0
for k in range(1,len(pos)):
    f_c += k * (pos[k-1])
print f_c
    # print (j * count)
# name = "KIRAN"
# name = ''.join(sorted(name))
# print name
# for ch in name:
#     print(letters[ch])
