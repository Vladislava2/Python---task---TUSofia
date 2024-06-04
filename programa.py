n = int(input("Въведете число: "))

if n == n[::-1]:
    print ("The number is palindrom!")
elif n != n[::-1]:
    print ("The number isn't palindrom!")
    