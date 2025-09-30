temperature_celsius = float(input("temperature_celsius: "))
temperature_fahrenheit = temperature_celsius * 9 / 5 + 32

if temperature_celsius < 15:
    print("Cold Temperature")
elif temperature_celsius >= 15 and temperature_celsius < 30:
    print ("Moderate Temperature")
else:
    print("Hot Temperature")
print(f"temperature_fahrenheit is : {temperature_fahrenheit}")
