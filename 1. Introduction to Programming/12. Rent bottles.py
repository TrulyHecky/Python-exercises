# Creating constants for one liter bottle and more than one liter

ONE_LITER_BOTTLE = 0.10
MORE_THAN_ONE = 0.25

# Getting input from user

one_liter_bottle = int(input("Enter amount of one liter bottles: "))
more_than_one = int(input("Enter amount of more than one liter bottles: "))

# Creating sum variable for each type of bottles

sum_bottles = float((one_liter_bottle * ONE_LITER_BOTTLE) + (more_than_one * MORE_THAN_ONE))

print(f"Amount that can be earned: ${sum_bottles}")
