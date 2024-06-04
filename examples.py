#n = int(input("Въведи число: "))

#sum = 0
#for n in range (0, n+1):
    #sum = sum + n

#print("Сумата на първите", n , "e: ", sum)

#multiplication = 1
#for n in range (1, n+1):
    #multiplication = multiplication * n 

#print("Произведението на първите", n , "e: ", multiplication)

#-------------------------------------------------------------------------------------

#a = float(input("Въведи реално число: "))
#n = int(input("Въведи число: "))
#grading = 1
#grading = a ** n 

#print("a на степен n = ", grading)

#-------------------------------------------------------------------------------------

pip install tabulate
from tabulate import tabulate
table = [["First name","Last name","Age"], ["John", "Smith", 12], ["Mary", "Jane", 25]]
print(tabulate(table))


    