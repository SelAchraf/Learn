# Task 1
Name = "Achraf",
print(Name)
print(type(Name))
print("=" * 50)

# Task 2
friends = ("Osama", "Ahmed", "Sayed")
friends = list(friends) 
friends[0] = "Elzero"
friends = tuple(friends)
print(friends)
print(type(friends))
print(f"{len(friends)} elements")
print("=" * 50)

# Task 3
nums = (1, 2, 3)
letters = ("A", "B", "C")
concatenation = nums + letters
print(concatenation)
print(len(concatenation))
print("=" * 50)

# Task 4
my_tuple = (1, 2, 3, 4)
a, b, _, c = my_tuple
print(a)
print(b)
print(c)