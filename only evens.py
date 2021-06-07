#  Write a function that accepts a list of numbers as an argument.  
# Return a new List that includes the only the even numbers.

def only_evens(list_of_num):
    evens = []
    for num in list_of_num:
        if num % 2 == 0:
            evens.append(num)
    return evens

   
list_of_num = [8, 29, 33, 45, 44, 100, 3004, 202, -1, -8]

print(only_evens(list_of_num))

