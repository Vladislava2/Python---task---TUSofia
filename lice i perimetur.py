import math
a=int(input("Please, Enter the value a:"))
b=int(input("Please, Enter the value b:"))
h=int(input("Please, Enter the value h:"))
r=int(input("Please, Enter the value r:"))
#c=int(input("Please, Enter the value c:"))
ha=int(input("Please, Enter the value ha:"))
hb=int(input("Please, Enter the value hb:"))
hc=int(input("Please, Enter the value hc:"))
d1=int(input("Please, Enter the value d1:"))
d2=int(input("Please, Enter the value d2:"))
alpha=int(input("Please, Enter the value alpha:"))
n=int(input("Please, Enter the value n:"))
x=math.pi/n 
lice_na_trapec=((a+b)*h)/2
lice_okrujnost=3,14*r*r
perimetur_na_okrujnost=2*3,14*r
lice_na_pravougulnik=a*b
lice_na_ysporednik=a*ha
lice_na_prav_triug=(a*b)/2
obikolka_na_prav_triug=a+b+math.sqrt(a*a+b*b)
lice_na_romb=a*h
lice_na_izpk_chetiriug=(d1*d2*math.sin(alpha))/2
lice_na_prav_mnogoug=n*a*a*(math.cos(x)/math.sin(x))
print("The result is:",lice_na_trapec)
print("The result is:",lice_okrujnost)
print("The result is:",perimetur_na_okrujnost)
print("The result is:",lice_na_pravougulnik)
print("The result is:",lice_na_ysporednik)
print("The result is:",lice_na_prav_triug)
print("The result is:",obikolka_na_prav_triug)
print("The result is:",lice_na_romb)
print("The result is:",lice_na_izpk_chetiriug)
print("The result is:",lice_na_prav_mnogoug)
