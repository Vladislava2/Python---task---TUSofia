Създаване на модул и съхраняване под името mymodule.py 
def greeteng(name):
    print("Hello, " + name)

Извикване на модула:
import mymodule
mymodule.greeting("Jonathan")

#Hello, Jonathan

from modname import name1[, name2[, ... nameN]]

from fibo import fib, fib2
fib(500)

#0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

from modname import *

from fibo import *
fib(500)

0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

reload()
reload(module_name)

Създаване на модули с използване на променливи от тип масив, обекти, речници и променливи.
Нека 
