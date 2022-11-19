import math

# Getting user input

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Functions

sm = float(num1 + num2)
sub = float(num1 - num2)
mult = float(num1 * num2)
div = float(num1 / num2)
rem = num1 % num2
log = math.log10(num1)
power = float(num1 ** num2)

print(f"{sm}, {sub}, {mult}, {div}, {rem}, {log}, {power}")
