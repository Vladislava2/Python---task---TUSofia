#n = float(input("Въведи число: "))
#if n >= 5.50:
    #print("Excellent!")
#elif n < 5.50:
    #print("Not excellent!")

#n = int(input("Въведи число:"))
#if n % 2 == 0:
 #   print("Tова число е четно!")
#else:
 #   print("Това число не е четно!")

#a = int(input("Въведи число: "))
#b = int(input("Въведи число: "))
#if a > b:
    #print(a)
#elif a < b:
    #print(b)

#n = int(input("Въведи цяло число: "))
#if n == 1:
    #print("ЕДНО")
#elif n == 2:
    #print("ДВЕ")
#elif n == 3:
    #print("ТРИ")
#elif n == 4:
    #print("ЧЕТИРИ")
#elif n == 5:
    #print("ПЕТ")
#elif n == 6:
    #print("ШЕСТ")
#elif n == 7:
    #print("СЕДЕМ")
#elif n == 8:
    #print("ОСЕМ")
#elif n == 9:
    #print("ДЕВЕТ")
#else:
    #print("Числото е твърдо голямо!")

#n = int(input("Въведи число: "))
#bonusScore = 0.0
#if n <= 100:
    #bonusScore = 5
#elif n > 100 and n < 1000:
    #bonusScore = n * 0.2
#else:
    #bonusScore = n * 0.1
#if n % 2 == 0:
    #bonusScore = bonusScore + 1
#if n % 10 == 5:   # Може и n % 5 == 0, но тогава ще се добавя към всички делящи се на 5 (завършващи на 0 и 5)
    #bonusScore = bonusScore + 2 
#print (bonusScore)
#print (n + bonusScore)

first = int(input("Въведи цяло число: "))
second = int(input("Въведи цяло число: "))
third = int(input("Въведи цяло число: "))

sum = first + second + third

minutes = sum // 60
seconds = sum % 60
 
if seconds < 10:
    print(str(minutes) + ":0" + str(seconds))
else:
    print(str(minutes) + ":" + str(seconds))








