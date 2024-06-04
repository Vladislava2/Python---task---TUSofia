a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
action = str(input("Choose action: summation, subtraction, multiplication, division:"))

def summation (a,b):
    print(a+b)

def subtraction (a,b):
    print(a-b)

def multiplication (a,b):
    print(a*b)

def division (a,b):
    print(a/b)

if action == "summation":
    print(a+b)

if action == "subtraction":
    print(a-b)

if action == "multiplication":
    print(a*b)

if action == "division":
    print(a/b)
