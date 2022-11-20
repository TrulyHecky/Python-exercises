import math

latitude1 = math.radians(float(input("Enter a first latitude: ")))
longitude1 = math.radians(float(input("Enter a first longitude: ")))
latitude2 = math.radians(float(input("Enter a second latitude: ")))
longitude2 = math.radians(float(input("Enter a second longitude: ")))

distance = 6371.01 * math.acos(math.sin(latitude1) * math.sin(latitude2) + math.cos(latitude1) * math.cos(latitude2) * math.cos(longitude1 - longitude2))

print(distance)
