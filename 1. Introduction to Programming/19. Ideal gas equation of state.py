R = 8.314

cels = float(input("Enter temperature: "))
pressure = float(input("Enter pressure: "))
vol = float(input("Enter vol: "))

cels_to_kel = cels + 273.15

moles = (R * cels_to_kel) / (pressure * vol)

print(f"Result: {moles} moles")
