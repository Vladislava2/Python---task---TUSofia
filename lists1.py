from typing import List


num_list = []
n = int(input("Enter the Starting of the range: "))
k = int(input("Enter the Ending of the range: "))
for i in range(n,k+1):
    num_list.append(i)
print("Original Number List: ", num_list)
even_list=[]
odd_list=[]
for i in range(len(num_list)):
    if(num_list[i] % 2 == 0):
        even_list.append(num_list[i])
    else:
        odd_list.append(num_list[i])
print("Even Numbers List: ", even_list)
print("Odd Numbers List: ", odd_list)


#def get_even_numbers(numbers):
    #even_numbers = []
    #for number in numbers:
        #if number % 2 == 0:
            #even_numbers.append(number)
    #return even_numbers
#def get_odd_numbers(numbers):
    #odd_numbers = []
    #for number in numbers:
        #if number % 2 == 1:
            #odd_numbers.append(number)
    #return odd_numbers

#numbers = [1,2,3,4,5,6,7,8,9,10]
#print(get_even_numbers(numbers))
#print(get_odd_numbers(numbers))