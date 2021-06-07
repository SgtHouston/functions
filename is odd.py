def Is_It_Odd(num):
    if num % 2 != 0:
        print("Yes, " + str(num) + " is an odd number.")
        return True
            
    else:
        print("No, " + str(num) + " is not an odd number.")
        return False
            

try:
    num = (float(input("What number would you like to check?: ")))
    print(Is_It_Odd(num))

except ValueError:
    print("This is not a number.")