# Creating constant for annual

ANNUAL = 0.04

# Getting user input

value = int(input("Enter your value: "))

# Creating variables for first, second and third years

first_year = value * ANNUAL + value
second_year = value * 0.08 + value
third_year = value * 0.12 + value

print(f"Your value after first year: {first_year}\nYour value after second year: {second_year}\nYour value after third year: {third_year}")
