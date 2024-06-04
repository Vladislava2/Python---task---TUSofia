a = float(input("Въведи число: "))
b = float(input("Въведи число: "))
c = float(input("Въведи число: "))

S = 0.0

p = (a+b+c)*0.5

S = (p*(p-a)*(p-b)*(p-c))**0.5

if a > c - b and b > c - a and c > b - a: 
    print("Лицето е: " + str(S)) 
else:
    print("Не съществува!")




