def even_numbers(mylist):
    evennumbers = []
    for numbers in mylist:
        if numbers % 2 == 0:
           evennumbers.append(numbers)
    return evennumbers

print(even_numbers([1,2,3,4,5,6,7,8,9,10,12,13,15]))

