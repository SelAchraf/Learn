# Task 1
friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]
# methode 1
def remove_chars(friend):
    return friend[1:-1]
cleaned_list = map(remove_chars, friends_map)
for name in cleaned_list:
    print(name)
print("-" * 15)

# methode 2
for name in map((lambda friend:friend[1:-1]), friends_map):
    print(name)
print("=" * 50)

# Task 2
friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]
# methode 1
def get_names(friend):
    return friend[-1] == "m"    
names = filter(get_names, friends_filter)
for name in names:
    print(name)
print("-" * 15)

# methode 2
for name in filter((lambda friend: friend[-1] == "m"), friends_filter):
    print(name)
print("=" * 50)

# Task 3
from functools import reduce
nums = [2, 4, 6, 2]
# methode 1
def multiply(num1, num2):
    return num1 * num2
result = reduce(multiply, nums)
print(result)
print("-" * 15)

# methode 2 
result = reduce((lambda num1, num2: num1 * num2), nums)
print(result)
print("=" * 50)

# Task 4
skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")
for num, skill in enumerate(reversed(skills), 50):
    if type(skill) != int :
        print(f"{num} - {skill}") 