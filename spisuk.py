import random
s=[1,3,5,7]
print(s[1])

s[1]=11
print(s)

s=list()
s1=list ("Python")
print (s1)

s=["P","Y","T","H","O","N",3]
print(s)

s=[]
s.append(5)
s.append(10)
s.append(20)
print(s)

s=[2,4,6,8]
s[0]=7
print(s[0])




s=[1,2,3,4,5,6]
print(s[::-1])
print(s[:-1])
print(s[1:])
print (s[0:2])
print(s[-1:])

s=[1,2,3,4,5,6]
s1=[9,8]
s2=s+s1
print(s2)

s=[[1,2,3,4,5], ["a","b","c"], [10,20]]
print(s[0][3])
print(s[2][0])

#s=[1,2,3,4,5,6]
#for i in s
#print (i, end="")


#s=[1,2,3,4,5,6]
#for i in range (len(s))
#print(s[i],end="")

s=[2,4,6,8]
print(4 in s)

s=[2,4,6,8,2]
print(s.count(2))#2
#print(s.index(3))#ValueError:3 is not in list
print(min(s))#би трябвало да изведе 2
print(max(s))#би трябвало да изведе 8

#Да се отброят

#append() (+=) insert()  pop()  remove()  del()

#insert [<индекс>, <обект>]

s=[2,4,6,8,2]
s.append (22)
print(s)

s+=[44,88]
print(s)

s.insert(0, 90)
print(s)

s.pop(0)
print(s)

s.remove(2)
print(s)

del s[4]
 

#Разбъркване на елементи

#shuffle()

s=[2,4,6,8,2]
random.shuffle(s)
print(s)
print(random.choice(s))
s.reverse()
print(s)

#sort()
#sort[<key=None>,<reverse=False>]

key=str.lower

s=[45,10,55,5,35]
s.sort()
print(s)

s.sort(reverse=True)
print(s)

s1=["s","T","a","E","f"]
s1.sort(key=str.lower)
s1.sort()
print(s1)

k=(7,5,3)
print(k)

#tuple=()

tup=tuple([10,20,30])
print(tup)

tup1=tuple("python")
print(tup1)
tup2=tuple()

k = (7,5,3,6,1)
print(k[0])
print(k[2:3])
print(7 in k)
print(k * 3)
tup = k + (2,4)
print (tup)

tup = (7,5,3,6,1)
print(tup.index(1))
print(tup.index(5))

for i in tup:
    print(i, end=' ')

d = dict
d1 = dict(name='ivan', last_name='petrov')
d3 = dict([('name','polina'), ('l_name', 'koleva')])
print(d3)
print(d1)

d = {}
d['name'] = 'petyr'
d['l_name'] = 'kolev'
d = {'name':'ivan', 'l_name':'ivanov'}
print(d)

d = {'name':'ivan', 'l_name':'ivanov'}
d['name']
print(d['fname'])

b = 'fname' in d
print(b)

len(d)
print(len(d))

d['s_name'] = 'petrov'
print(d)

del d['s_name']
print(d)

keys = list(d.keys())
keys.sort()
for key in keys:
    print("{0} => {1})".format(key, d[key]), end=' ')

s = set([1,2,3,1])
print(s)
s2 = set("hello")

s2 = set("hello")
for i in s2:
    print(i,end=' ')
    
print(len(s2))

s = set([1,2,3])
s1 = set([4,2,6])
s3 = s | s1
print(s3)

s = set([1,2,3,4])
s1 = set([2,4,6])
s3 = s1 - s
print(s3)

s = set([1,2,3,4])
s1 = set([2,4,6])
s4 = s & s1
print(s4)

bit A    bit B   XOR
0          0      0
0          1      1
1          0      1
1          1      0

s = set([1,2,3,4])
s1 = set([2,4,6])
s5 = s ^ s1
print(s5)

3 in s
 ==
 s1 <= s

add(< елемент>)
remove(<елемент > )
discard( < елемент> )
pop()
clear()
s1 = set([2,4,6])
s1.add(8)
s1.remove(2)
print(s1)
s1.remove(2)







































