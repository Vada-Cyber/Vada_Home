import math

constant = 32.45 # 20*log10(4*pi/c) where c is speed of light in vacuum
tx_antenna_gain = float(input("tx_antenna_gain: ")) # dBi
rx_antenna_gain = float(input("rx_antenna_gain: "))  # dBi
distance_m = float(input("Enter distance in meters: "))
frequency_mhz = float(input("Enter frequency in megahertz: "))
distance_km = distance_m / 1000

distance_term = 20 * math.log10(distance_km)
frequency_term = 20 * math.log10(frequency_mhz)
total_fspl = constant + distance_term + frequency_term - tx_antenna_gain - rx_antenna_gain
print(f"Distance in meters: {distance_m} m")
print(f"Distance_term: {distance_term} dB")
print(f"Frequency: {frequency_term} dB")
print(f"tx_antenna_gain: {tx_antenna_gain} dBi")
print(f"rx_antenna_gain: {rx_antenna_gain} dBi")

print(f"Free Space Path Loss is: {total_fspl} dB")

