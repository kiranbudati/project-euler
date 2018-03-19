squares = []

for i in range(1,101):
    squares.append(i*i)
sum_sq = sum(squares) 
print(sum_sq)

sum_num = sum(range(1,101))
sum_num_sq = sum_num*sum_num
print(sum_num_sq)

print(sum_num_sq - sum_sq)