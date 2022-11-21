import math

n = float(input("Enter amount of sides: "))
length = float(input("Enter length of sides: "))

area = (n * length ** 2) / (4 * math.tan(math.pi / n))

print(f"Area: {area}")
