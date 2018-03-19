def factnum(n):
    count = 1
    for i in range(n,0,-1):        
        count = count * i
    
    cou_sum = sum(map(int,str(count)))
    print cou_sum
    return count
print(factnum(100))