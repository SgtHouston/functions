try:
    
    def Is_It_Even(num):
        if num % 2 == 0:
            print("Yes, " + str(num) + " is an even number.")
            return True
            
        else:
            print("No, " + str(num) + " is not an even number.")
            return False
            
    
    num = (float(input("What number would you like to check?: ")))

    print(Is_It_Even(num))
    
            
except ValueError:
    print("This is not a number.")