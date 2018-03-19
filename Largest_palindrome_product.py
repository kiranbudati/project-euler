# def Largest_palindrome_product(n):
    
#     m = n
#     a = 0
#     while m!=0:
#         a = m % 10 + a * 10
#         m = m / 10
#     if(n == a):
#         print("palindrome")
#     else:
#         print("not palindrome")

# Largest_palindrome_product(202)
max_num = 0
for i in range(100,999):
    for j in range(100,999):
        mult = i * j
        if str(mult) == str(mult)[::-1]:
            if mult > max_num:
                max_num = mult
print(max_num)