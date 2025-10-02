temperature_celsius = float(input("temperature_celsius: "))
temperature_fahrenheit = temperature_celsius * 9 / 5 + 32

if temperature_celsius >-15 and temperature_celsius <0:
    print("Extremely_Cold_Temperature")
elif temperature_celsius >=-15 and temperature_celsius < 0:
    print ("Very_Cold_Temperature")
elif temperature_celsius >0 and temperature_celsius < 15:
    print ("Cold_Temperatur")
elif temperature_celsius >= 15 and temperature_celsius < 22:
    print ("Moderate Temperature")
elif temperature_celsius >= 22 and temperature_celsius < 32:
    print("Hot_Temperature")
elif temperature_celsius >=32 and temperature_celsius < 45:
    print ("Very_Hot_Temperature")
else:
    print("Extremely_Hot_Temperature, Tunr_the_Iron_Off")
print(f"temperature_fahrenheit is : {temperature_fahrenheit}°F")
print(f"{temperature_celsius}°C  is : {temperature_fahrenheit}°F")

