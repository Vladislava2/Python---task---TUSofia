import math
n = int(input("Enter a number:"))
def palindrom(n):
    if n == n[::-1]:
        return 1
    else:
        return 0

