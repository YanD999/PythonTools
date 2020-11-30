unit = input("What unit do you want to convert from? F/C ")
temp = input("What is the temperature to convert? ")

def isCelsius():
    return unit == 'c' or unit == 'C' or unit == 'celsius' or unit == 'Celsius'

def isFahrenheit():
    return unit == 'f' or unit == 'F' or unit == 'fahrenheit' or unit == 'Fahrenheit'

if unit == ' ' or unit == '' or temp == ' ' or temp == '' or (isCelsius() == False and isFahrenheit() == False):
    print("You didn't gave correct values")
    exit()
else:
    if isCelsius(): # to fahrenheit
        fahrenheit = (float(temp) * 9/5) + 32
        print(temp + "°C corresponds to " + str(fahrenheit) + " degrees Fahrenheit")
    elif isFahrenheit(): # to celsius
        celsius = (float(temp) - 32) * 5/9
        print(temp + "°F corresponds to " + str(celsius) + " degrees Celsius")
    else:
        print("Invalid unit") # should never be called
