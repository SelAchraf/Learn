import datetime
# Task 1
Date = datetime.datetime(2021, 6, 25).date()
Now = datetime.datetime.now().date()
print(f"Days From {Date} To {Now} Is => {(Now - Date).days}")
print("=" * 50)

# Task 2
print(datetime.datetime.now().date())
print(datetime.datetime.now().date().strftime("%b %-m, %Y"))
print(datetime.datetime.now().date().strftime("%-m - %b - %Y"))
print(datetime.datetime.now().date().strftime("%-m / %b / %y"))
print(datetime.datetime.now().date().strftime("%-m / %B / %Y"))
print(datetime.datetime.now().date().strftime("%a, %-m  %B  %Y"))