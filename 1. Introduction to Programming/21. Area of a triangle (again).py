import math

s1 = float(input("Enter first side: "))
s2 = float(input("Enter second side: "))
s3 = float(input("Enter third side: "))

half_per = (s1 + s2 + s3) / 2

area = math.sqrt(half_per * (half_per - s1) * (half_per - s2) * (half_per - s3))

print(f"Area: {area}")
