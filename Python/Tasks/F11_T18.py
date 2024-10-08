# Task 1 ##############################



# Task 2 ##############################

# Task 3
name = 'Elzero'
print("Second Letter Is " + "\"" + name[1] + "\"")
print("Third Letter Is " + "\"" + name[2] + "\"")
print("Last Letter Is " + "\"" + name[-1] + "\"")
print("=" * 50)

# Task 4
name = 'Elzero'
print("\"" + name[1:4] + "\"")
print("\"" + name[0:5:2] + "\"")
print("\"" + name[-2::-2] + "\"")
print("=" * 50)

# Task 5
name = "#@#@Elzero#@#@"
print(name.strip("#@"))
print("=" * 50)

# Task 6
num = "9"
print(num.zfill(4))
print("=" * 50)

# Task 7
name_one = "Osama"
name_two = "Osama_Elzero"
print(name_one.rjust(20,"@"))
print(name_two.rjust(20,"@"))
print("=" * 50)

# Task 8
name_one = "OSamA"
name_two = "osaMA"
print(name_one.swapcase())
print(name_two.swapcase())
print("=" * 50)

# Task 9
msg = "I Love Python And Although Love Elzero Web School"
print(msg.count("Love"))
print("=" * 50)

# Task 10
name = "Elzero"
print(name.find("z"))
print("=" * 50)

# Task 11
msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3", "Love", 1))
print("=" * 50)

# Task 12
msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3", "Love"))
print("=" * 50)

# Task 13
name = "Osama"
age = 38
country = "Egypt"
print(f"My Name Is {name}, And My Age Is {age}, And My Country Is {country}")   # methode 1
print("My Name Is {}, And My Age Is {}, And My Country Is {}" .format(name, age, country))  # methode 2