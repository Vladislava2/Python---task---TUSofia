n = int(input("Enter a number:"))
sum_nums = 0
multiplication_nums = 1
for i in range(1, n+1):
    #sum_nums+=i
    if n>10:
        multiplication_nums*=i
    elif n<10:
        sum_nums+=i
print(sum_nums)
print(multiplication_nums)

