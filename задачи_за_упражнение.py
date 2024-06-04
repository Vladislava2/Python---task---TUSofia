# 1-ва задача
for i in range(1,1000):
    if i % 10 == 7:
        print(str(i))

# 2-ра задача
#n = int(input())
#sum_nums = 0

#for i in range(1, n):
    #current_num = int(input())
    #sum_nums = sum_nums + current_num
    
#print("sum =" + str(sum_nums))

# 3-та задача
num = 5
for i in range (1,11):
    print(num, "x", i, "=", num*i)

# 4-та задача
for x in range(-10,0):
    print(x)

# 5-та задача
lower = 25
upper = 50
print("Prime numbers between", lower, "and", upper, "are:")
for num in range(25,51):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:     
            print(num)

# 6-та задача
#rows = input("Enter a number:")
#rows = int(rows)
    #for i in range (0, rows):
        #for j in range (0, i+1):
        #print("*", end="")
        #print("\r")
    #for i in range (rows, 0, -1):
        #for j in range (0, i-1):
        #print("*", end="")
        #print("\r")

# 7-ма задача
s=[7,6,5,4,2]
print(s[::-1])

# 8-ма задача








