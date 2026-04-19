from datetime import datetime
import time

while True:
    try:
        name = input("Enter your name: ")
        time.sleep(0.75)
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        break
    except ValueError as e:
        print(e)

def select_date_of_birth():
    while True:
        try:
            date_string = input("Enter your date of birth (Format: YYYY-MM-DD): ")
            date_object = datetime.strptime(date_string, '%Y-%m-%d')
            time.sleep(0.75)
            if date_object > datetime.now():
                print("Date of birth cannot be in the future. Please enter a valid date.")
                continue
            return date_object
        except ValueError:
            print("Invalid date or wrong format. Enter a valid date in YYYY-MM-DD format.")
            time.sleep(0.75)

dob = select_date_of_birth()
today = datetime.now()
age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

time.sleep(1.25)
print(f"Date of Birth: {dob.strftime('%Y-%m-%d')}")
time.sleep(0.5)
if dob.day == today.day and dob.month == today.month:
    print(f"Happy Birthday, {name}! You are now {age} years old.")
else:
    print(f"{name}, you are {age} years old.")