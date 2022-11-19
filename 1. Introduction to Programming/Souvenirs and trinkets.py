# Creating constants for total sum

SOUVENIR = 75
TRINKET = 112

# Getting user input

souv = int(input("Enter amount of souvenirs: "))
trin = int(input("Enter amount of trinkets: "))

sm = (souv * SOUVENIR) + (trin * TRINKET)

print(f"Total weight: {sm} grams")
