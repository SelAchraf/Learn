# Task 1
values = (0, 1, 2)
if any(values):
    my_var = 0      #my_var = 0
my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]
if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):
    print("Good")
else:
    print("Bad")
print("=" * 50)
# Good

# Task 2 ##############################################

# Task 3 ##############################################

# Task 4
def my_all(input):
    for i in input:
        if not i:
            return False
    return True
print(my_all([1, 2, 3]))
print(my_all([1, 2, 3, []]))
print("-" * 15)

def my_any(input):
    for i in input:
        if i:
            return True
    return False
print(my_any([0, 1, [], False])) 
print(my_any([(), 0, False])) 
print("-" * 15)

def my_min(input):
    min = input[0]
    for i in input:
        if min > i:
            min = i
    return min
print(my_min([10, 100, -20, -150, 50]))
print("-" * 15)

def my_max(input):
    max = input[0]
    for i in input: 
        if max < i:
            max = i
    return max
print(my_max([10, 100, -20, -100, 50, 700]))