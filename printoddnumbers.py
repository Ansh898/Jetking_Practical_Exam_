def odd_numbers(mylist):
    oddnumbers = []
    for numbers in mylist:
        if numbers % 2 == 1:
           oddnumbers.append(numbers)
    return oddnumbers

print(odd_numbers([1,2,3,4,5,6,7,8,9,10,12,13,15]))

