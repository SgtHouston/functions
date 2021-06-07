try:
    degrees_in_fahrenheit = float(input("What is the temperature in Fahrenheit?: "))

    def F2C_Converter():
            
        degrees_in_celcius = (degrees_in_fahrenheit - 32) * 5/9
            
        return degrees_in_celcius

    print(F2C_Converter(),"C")

except ValueError:
    print("This is not a number.")