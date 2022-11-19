SQUARE_FEET_IN_ACRE = 43560 # creating constant

# Entering length and width in feets

length = float(input("Enter length (feets): "))
width = float(input("Enter width (feets): "))

# Getting area in acres

area = (length * width) / SQUARE_FEET_IN_ACRE

print(f"Square area in acres is equal to: {area} acres")
