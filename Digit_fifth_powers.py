# def digfifth(n):
#     num = [1634,8208,9474]

#     count = 0
#     my_lis = []

#     for i in range(len(num)):
#         num_c = 0
#         for j in map(int,str(num[i])):
#             nm = 0
#             nm = j ** n
#             num_c += nm
#         my_lis.append(num_c)
#     print my_lis 
#     return sum(my_lis)
#             # num_c += j ** n
#             # print num_c
#         # count += num_c
#         # count
#     # return count 
#     # count = 0
#     # for i in map(int,str(num1)):
#     #     print i ** n
#     #     count += i ** n
#     # return count

# print(digfifth(5))

summ = 0
digit_sum = 0
i = 0
while i < 1000000:
    digit_sum = 0 # should be set in each step
    j = list(str(i))
    for x in j:
       digit = int(x) ** 5
       digit_sum += digit
    if digit_sum == i:
       summ += i
       print(i)
    i += 1
print(summ)