INCH = 2.54
FEET = 12 * INCH

in_inch = int(input("Enter your height in inch: "))
in_feet = int(input("Enter your height in feet: "))

inch_in_cm = in_inch * INCH
feet_in_cm = in_feet * FEET

print(f"Inch in cm: {inch_in_cm}\nFeet in cm: {feet_in_cm}")
