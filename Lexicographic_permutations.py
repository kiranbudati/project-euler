from itertools import permutations 
n = 3
my_list = []

for item in permutations(range(n), 5): 
    my_list.append(item)

print my_list