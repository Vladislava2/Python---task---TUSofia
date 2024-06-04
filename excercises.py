# Задача 1

def get_odd_numbers(numbers):
    odd_numbers = []
    
    for number in numbers:
        if number % 2 == 1:
            odd_numbers.append(number)
    return odd_numbers

    
numbers = [1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
print(get_odd_numbers(numbers))

def get_even_numbers(numbers):
    even_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

print(get_even_numbers(numbers))

# Задача 3

#def define_average(first_arg, *rest_arg):
    #average = (first_arg + sum(rest_arg)) / (1 + len(rest_arg))
#print(define_average(define_average))
#define_average(1,2,3,4,5,6,7,8,9,10)

# Задача 4

def generator(months):
    generator_one = []
print(generator(months))
months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]    
