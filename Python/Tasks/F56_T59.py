# Task 1
def calculate(num1, num2, operation="Add"):
    if operation.lower() == "a" or operation.lower() == "add":
        print(num1 + num2)
    elif operation.lower() == "s" or operation.lower() == "subtract":
        print(num1 - num2)
    elif operation.lower() == "m" or operation.lower() == "multiply":
        print(num1 * num2)
    else:
        print("operation invalid")
calculate(1,2,"add")
print("=" * 50)

# Task 2
def addition(*nums):
    Total = 0
    for num in nums :
        if num == 10 :
            continue
        elif num == 5 :
            Total -= num
        else:
            Total += num
    print(Total)
addition(10,5)
print("=" * 50)

# Task 3
def show_skills(name, *skills):
    if skills:
        print(f"Hello {name} Your Skills Is")
        for skill in skills :
            print(f"- {skill}")
    else:
        print(f"Hello {name} You Have No Skills To Show")
show_skills("Osama", "HTML", "CSS", "JS", "Python")
show_skills("Ahmed")
print("=" * 50)

# Task 4
def say_hello(name = None, age = None, country = None):
    if name and age and country: 
        print(f"Hello {name} Your Age Is {age} And You Live In {country}")
    else:
        print(f"Hello Unknown Your Age Is Unknown And You Live In Unknown")
say_hello("Osama", 38, "Egypt")  
say_hello()
