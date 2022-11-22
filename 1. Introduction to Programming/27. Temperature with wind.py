temp = float(input("Enter temp: "))
wind = float(input("Enter wind speed: "))

wci = 13.12 + (0.6215 * temp) - (11.37 * wind  0.16) + (0.3965 * temp * wind  0.16)

print(f"WCI: {wci}")
