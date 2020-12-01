unit = input("What unit do you want to convert from? K/F/C ")
temp = input("What is the temperature to convert? ")

def isCelsius():
    return unit == 'c' or unit == 'C' or unit == 'celsius' or unit == 'Celsius'

def isFahrenheit():
    return unit == 'f' or unit == 'F' or unit == 'fahrenheit' or unit == 'Fahrenheit'

def isKelvin():
    return unit == 'k' or unit == 'K' or unit == 'kelvin' or unit == 'Kelvin'

if unit == ' ' or unit == '' or temp == ' ' or temp == '' or (isCelsius() == False and isFahrenheit() == False and isKelvin() == False):
    print("You didn't gave correct values")
    exit()
else:
    if isCelsius(): # to fahrenheit and kelvin
        fahrenheit = (float(temp) * 9/5) + 32
        kelvin = float(temp) + 273.15
        print(temp + "°C corresponds to " + str(fahrenheit) + " degrees Fahrenheit")
        print(temp + "°C corresponds to " + str(kelvin) + " degrees Kelvin")
    elif isFahrenheit(): # to celsius and kelvin
        celsius = round((float(temp) - 32) * 5/9, 2)
        kelvinf = round(celsius + 273.15, 2)
        print(temp + "°F corresponds to " + str(celsius) + " degrees Celsius")
        print(temp + "°F corresponds to " + str(kelvinf) + " degrees Kelvin")
    elif isKelvin(): # to celsius and fahrenheit
        celsiusk = float(temp) - 273.15
        fahrenheitk = (float(celsiusk) * 9/5) + 32
        print(temp + "°K corresponds to " + str(celsiusk) + " degrees Celsius")
        print(temp + "°K corresponds to " + str(fahrenheitk) + " degrees Fahrenheit")
    else:
        print("Invalid unit") # should never be called
