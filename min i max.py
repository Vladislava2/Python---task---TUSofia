num_of_numbers=int(input("Please, Enter:"))
min=None
max=None
for K in range(num_of_numbers):
    num=int(input("Enter a number:"))
    if max is None:
        max=num
    elif max<num:
            max=num
    if min is None:
        min=num
    elif min>num:
        min=num
print("Maximum is",max)
print("Minimum is",min)
    
               
