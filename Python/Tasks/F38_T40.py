# Task 1
name = input("Plrase enter your name: ")
print(f"Hello {name.strip().capitalize()}, Happy to see you")
print("=" * 50)

# Task 2
age = int(input("Please enter your age: "))
print(type(age))
if(age < 16):
    print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")
else:
    print(f"Hello Your Age Is {age}, All Articles Is Suitable For You")
print("=" * 50)

# Task 3
first_name = input("Enter your first_name: ")
second_name = input("Enter your second_name: ")
print(f"Hello {first_name.strip().capitalize()} {second_name.strip().capitalize():.1s}.")
print("=" * 50)

# Task 4
email = input("Enter your email: ").strip().lower()
print(f"The email lower is: {email}")
print(f"Your Name Is: {email[:email.index("@")].capitalize()}")
print(f"Your Service Provider Is: {email[email.index("@")+1:email.index(".")]}")
print(f"Your Level Domain Is: {email[email.index(".")+1:]}")
