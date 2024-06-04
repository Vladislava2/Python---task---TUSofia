#class py_solution:
    #def int_to_Roman(self, num):
        #val = [
            #1000, 900, 500, 400,
            #100, 90, 50, 40,
            #10, 9, 5, 4,
            #1
            #]
        #syb = [
            #"M", "CM", "D", "CD",
            #"C", "XC", "L", "XL",
            #"X", "IX", "V", "IV",
            #"I"
            #]
        #roman_num = ''
        #i = 0
        #while  num > 0:
            #for _ in range(num // val[i]):
                #roman_num += syb[i]
                #num -= val[i]
            #i += 1
        #return roman_num


#print(py_solution().int_to_Roman(1))
#print(py_solution().int_to_Roman(2476))





def intToRoman(num): 
# Storing roman values of digits from 0-9 
# when placed at different places 
    m = ["", "M", "MM", "MMM"]

    c = ["", "C", "CC", "CCC", "CD", "D", 
         "DC", "DCC", "DCCC", "CM "] 

    x = ["", "X", "XX", "XXX", "XL", "L", 
         "LX", "LXX", "LXXX", "XC"] 

    i = ["", "I", "II", "III", "IV", "V", 
         "VI", "VII", "VIII", "IX"] 

# Converting to roman 

    thousands = m[num // 1000] 

    hundreds = c[(num % 1000) // 100] 

    tens = x[(num % 100) // 10] 

    ones = i[num % 10] 

    ans = (thousands + hundreds +
           tens + ones) 
    return ans

# Driver code
 
if __name__ == "__main__": 
    number = 10
    print(intToRoman(number)) 

