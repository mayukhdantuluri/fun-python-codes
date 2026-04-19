print("Welcome to the temperature converter.")
print("Here, you can convert temperatures between Celsius/Centigrade, Fahrenheit, and Kelvin.")

start_unit = input("Enter the unit you want to convert from (First letter or whole word): ").strip().lower()
if start_unit in ['c', 'celsius', 'centigrade']:
    end_unit = input("Enter the unit you want to convert to (Fahrenheit or Kelvin): ").strip().lower()
    if end_unit in ['c', 'celsius', 'centigrade']:
        print("Both start & end unit cannot be the same. Restart the program.")
    elif end_unit in ['f', 'fahrenheit']:
        celsius_temp = float(input("Enter the temperature in Celsius: "))
        fahrenheit_temp = (celsius_temp * 9/5) + 32
        print(f"{celsius_temp}° C = {fahrenheit_temp}° F")
    elif end_unit in ['k', 'kelvin']:
        celsius_temp = float(input("Enter the temperature in Celsius: "))
        kelvin_temp = celsius_temp + 273.15
        print(f"{celsius_temp}° C = {kelvin_temp} K")
    else:
        print("Invalid end unit. Restart the program.")
elif start_unit in ['f', 'fahrenheit']:
    end_unit = input("Enter the unit you want to convert to (Celsius or Kelvin): ").strip().lower()
    if end_unit in ['f', 'fahrenheit']:
        print("Both start & end unit cannot be the same. Restart the program.")
    elif end_unit in ['c', 'celsius', 'centigrade']:
        fahrenheit_temp = float(input("Enter the temperature in Fahrenheit: "))
        celsius_temp = (fahrenheit_temp - 32) * 5/9
        print(f"{fahrenheit_temp}° F = {celsius_temp}° C")
    elif end_unit in ['k', 'kelvin']:
        fahrenheit_temp = float(input("Enter the temperature in Fahrenheit: "))
        kelvin_temp = (fahrenheit_temp - 32) * 5/9 + 273.15
        print(f"{fahrenheit_temp}° F = {kelvin_temp} K")
    else:
        print("Invalid end unit. Restart the program.")
elif start_unit in ['k', 'kelvin']:
    end_unit = input("Enter the unit you want to convert to (Celsius or Fahrenheit): ").strip().lower()
    if end_unit in ['k', 'kelvin']:
        print("Both start & end unit cannot be the same. Restart the program.")
    elif end_unit in ['c', 'celsius', 'centigrade']:
        kelvin_temp = float(input("Enter the temperature in Kelvin: "))
        celsius_temp = kelvin_temp - 273.15
        print(f"{kelvin_temp} K = {celsius_temp}° C")
    elif end_unit in ['f', 'fahrenheit']:
        kelvin_temp = float(input("Enter the temperature in Kelvin: "))
        fahrenheit_temp = (kelvin_temp - 273.15) * 9/5 + 32
        print(f"{kelvin_temp} K = {fahrenheit_temp}° F")
    else:
        print("Invalid end unit. Restart the program.")
else:
    print("Invalid start unit. Restart the program.")