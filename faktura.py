from datetime import datetime

name = input("Въведете името си: ")

lists = '''
OIL             123     5lv/bottle
BISCUITS        124     3lv/package
SUGAR           125     1.50/kg
SALT            126     1lv/kg
CANDY           127     25lv/kg
'''
#declaration
price = 0
pricelist = []
totalprice = 0
Finalfinalprice = 0
ilist = []
qlist = []
plist = []

#rates for items 
items = {"OIL":5, 
"BISCUITS":3,
"SUGAR":1.50,
"SALT":1, 
"CANDY":25}

option = int(input("За списък с продукти, натиснете 1: "))
if option == 1:
    print(lists)
for i in range(len(items)):
    inp1 = int(input("За закупуване, натиснете 1 или 2 за напускане: "))
    if inp1 == 2:
        break 
    if inp1 == 1:
        item = input("Въведете избраният продукт: ")
        quantity = int(input("Въведете вашето количество: "))
        if item in items.keys():
            price = quantity * (items[item])
            pricelist.append((item, quantity, items, price))
            totalprice += price 
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst = (totalprice * 5)/100
            finalamount = gst + totalprice 
        else:
            print("Грешка! Въведеният артикул не е наличен!")
    else: 
        print("Грешка! Въведохте грешен номер!")
    inp = input("Желаете ли фактура? Въведете yes or no: ") 
    if inp == 'yes':
        pass
        if finalamount != 0:
            print(25*"=", "VLADY'S SUPERMARKET", 25*"=")
            print(28*" ","wannaparthy")
            print("Name: ", name, 30*" ", "Date: ", datetime.now())
            print(75*" - ")
            print("sno",8*" ", 'items', 8*" ", 'Quantity', 3*" ", 'price')
            for i in range(len(pricelist)):
                print(i, 8*' ', 5*' ', ilist[i], 3*' ', qlist[i], 8*" ", plist[i])
            print(75*" - ")
            print(50*" ", 'TotalAmount: ', totalprice)
            print("gst amount",40*" ", gst)
            print(75*" - ")
            print(50*" ", 'finalAmount:', finalamount)
            print(75*" - ")
            print(20*" ", "Заповядайте отново!")
            print(75*" - ")


