import math

ACS = 9.8
START_SPEED = 0

distance = float(input("Enter a distance: "))

free_fall = math.sqrt(START_SPEED ** 2 + 2 * ACS * distance)

print(f"Result: {free_fall}")
