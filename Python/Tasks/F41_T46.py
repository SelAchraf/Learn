# Task 1
first_num = int(input("Enter the first number: ").strip())
Second_num = int(input("Enter the second number: ").strip())
operation = input("Enter the operation: ").strip()
if operation == "+":
    print(first_num + Second_num)
elif operation == "-":
    print(first_num - Second_num)
elif operation == "*":
    print(first_num * Second_num)
elif operation == "/":
    print(first_num / Second_num)
else:
    print(first_num % Second_num)
print("=" * 50)

# Task 2
age = 17
print("App Is Suitable For You" if age >16 else "App Is Not Suitable For You")
print("=" * 50)

# Task 3
age = int(input("Enter your age: ").strip())
if age > 10 and age < 100 :
    print(f"Your Age In Months Is {age * 12} Months")
    print(f"Your Age In Days Is {age * 12 * 30} Days")
    print(f"Your Age In Hours Is {age * 12 * 30 * 24} Hours")
    print(f"Your Age In Minutes Is {age * 12 * 30 * 24 * 60} Minutes")
    print(f"Your Age In Seconds Is {age * 12 * 30 * 24 * 60 * 60} Seconds")
else :
    print("Your age is out of range")
print("=" * 50)

# Task 4
country = input("Input Your Country: ").strip().capitalize()
countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30
if country in countries : 
    print(f"Your Country Eligible For Discount And The Price After Discount Is ${price - discount}")
else : 
    print(f"Your Country Not Eligible For Discount And The Price Is ${price}")   