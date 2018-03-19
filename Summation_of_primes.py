# numbers = list(range(2, 2000000))
# for prime in numbers:
#     for x in numbers:
#         if x % prime == 0 and prime != x:
#             numbers.remove(x)
# print(sum(numbers))

marked = [0] * 2000000
value = 3
incm = 2
while value < 2000000:
    if marked[value] == 0:
        incm += value
        i = value
        while i < 2000000:
            marked[i] = 1
            i += value 
    value += 2
print incm