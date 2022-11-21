days = int(input("Enter days: "))
hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

days_to_sec = days * 86400
hours_to_sec = hours * 3600
mins_to_sec = minutes * 60

answer = days_to_sec + hours_to_sec + mins_to_sec + seconds

print(f"Answer is: {answer} seconds")
