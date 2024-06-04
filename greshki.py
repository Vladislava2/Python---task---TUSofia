#SyntaxError: invalid syntax
while True print("Hello world")
  File "<stdin>", line 1
    while True print("Hello world")

#SyntaxError: invalid syntax

#изключения:
#1: ZeroDivisionError
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero

#2: NameError
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name "spam" is not defined

#3: TypeError
>>> "2" + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError:





try:
        print(x)
except:
       print("An exception occurred")
#SyntaxError: expected an indented block

#try, except, finally
try:
        print(x)
except:
        print("An exception ocurred")

#try блок/except блокове
try:
        print(x)
except NameError:
        print("Variable x is not defined")
except:
        print("Something else went wrong")

#ключова дума else
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

#ключова дума finally
try:
       print(x)
except:
       print("Something went wrong")
finally:
       print("The 'try except' is finished")

#затваряне на обектите и освобождане на ресурсите
try:
  f = open("demofile.txt")
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()

#въвеждане на цяло число като вход от страна на потребителя:
while True:
  try:
          x = int(input("Please enter a number:"))
          break
    except ValueError:
         print("Oops! That was no valid number. Try again...")

#
except (RuntimeError, TypeError, NameError):
    pass

#ситуация на изключение при функции
def this_fails():
    x = 1/0
try:
    this_fails()
except ZeroDivisionError as err:
    print("Handling run-time error:", err)
  #Handling run-time error: division by  zero

#ключова дума raise
x = -1
if x < 0:
raise Exception("Sorry, no numbers below zero")

#грешка TypeError, ако типът на x не е int
x = "Hello"
if not type(x) is int:
raise TypeError("Only integers are allowed")

#грешка, върната от интерпретатора при генериране на ситуация HiThere:
raise NameError("HiThere")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: HiThere




raise ValueError

raise ValueError()





































  





        







