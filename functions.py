# функция за дължина на аргумент :len()
a = ['foo', 'bar', 'baz', 'qux']
len(a)
#4

функция any (): "True", "False";
any([False, False, False])
False
any([False, True, False])
True

def <function_name>([<parameters>]):
    <statement(s)>

<function_name>([arguments])


позиционни аргументи
def f(qty, item, price):
    print(f'{qty} {item} cost ${price:.2f}')

f(6, 'banana', 1.74)
#f(6, 'banana', 1.74)
#f(6, 'bananas')
#f(6, 'bananas', 1.74, 'kumquats')

аргументи ключови думи
<name>=<value>
def f(qty=6, item='bananas', price=1.74)

параметри по подразбиране
<name>=<value>
def f(qty=6, item='bananas', price=1.74):
    print(f'{qty} {item} cost ${price:.2f}')

f(4, 'apples', 2.24)
#4 apples cost $2.24
f(4, 'apples')
#4 apples cost $1.74

f(4)
#4 bananas cost $1.74
f()
#6 bananas cost $2.29



def f():
    print('foo')
    print('bar')
    return

f()
foo

def f(x):
    if x < 0:
        return
    if x > 0:
        return
    print(x) #функцията ще се изпълни ако всичко е изпълнено

def f():
    if error_cond1:
        return
    if error_cond2:
        return
    if error_cond3:
        return

<normal processing>

def f():
    return 'foo'

s = f()
s
foo'





































