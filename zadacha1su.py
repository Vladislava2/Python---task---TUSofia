figure = input("Фигура:")
а=int(input("Въведи число:"))
b=int(input("Въведи число:"))

def square (a):
    return a*a
def rectangle (a,b):
    return a*b
def triangle (a,b):
    return (a/2*b/2)

if figure == "square":
    print("S(квадрат)=" + str(square(a)))
elif figure == "rectangle":
    print("S(правоъгълник)=" + str(rectangle(a,b)))
elif figure == "triangle":
    print("S(триъгълник)=" + str(round(triangle(a,b),2)))
