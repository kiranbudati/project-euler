def dist(start,end):
    temp_list = []
    my_list = []

    for i in range(start,end+1):
        for j in range(start,end+1):
            temp_list.append(i**j)
    for k in temp_list:
        if k not in my_list:
            my_list.append(k)

    return len(my_list)
print(dist(2,100))