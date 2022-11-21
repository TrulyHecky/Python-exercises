WATER_HEAT_CAPACITY = 4.186
ELECTRICITY_PRICE = 8.9
J_TO_KWH = 2.777e–7

volume = float(input("Volume of water in milliliters: "))
d_temp = float(input("Temperature rise (in Celcius): "))

q = volume * d_temp * WATER_HEAT_CAPACITY

print(f"Needed energy: {q}")

kwh = q * J_TO_KWH
cost = kwh * ELECTRICITY_PRICE

print(f"Needed money: {cost}")
