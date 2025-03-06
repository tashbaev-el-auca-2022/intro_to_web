from datetime import datetime, timedelta
import time

# Lab1
now = datetime.now()
formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_now)

# Lab2
nooruz_date = datetime(now.year, 3, 21)
if now > nooruz_date:
    nooruz_date = datetime(now.year + 1, 3, 21)
time_left = nooruz_date - now
print(time_left)

# Lab3
def countdown(seconds):
    end_time = datetime.now() + timedelta(seconds=seconds)
    while True:
        remaining = end_time - datetime.now()
        total_seconds = int(remaining.total_seconds())
        if total_seconds <= 0:
            print("0")
            break
        print(f"Time remaining: {total_seconds} seconds", end="\r")
        time.sleep(1)
    print("Done")

# Lab3
def month_calendar(year, month):
    current_date = datetime(year, month, 1)
    start_weekday = current_date.weekday()
    if month == 12:
        next_month = datetime(year + 1, 1)
    else:
        next_month = datetime(year, month + 1, 1)
    last_date = next_month - timedelta(days=1)
    
    print("Mon Tue Wed Thu Fri Sat Sun")
    print("    " * start_weekday, end="")
    
    while current_date <= last_date:
        print(f"{current_date.day:3}", end=" ")
        if current_date.weekday() == 6:
            print()
        current_date += timedelta(days=1)
    print()

month_calendar(2025, 4)
