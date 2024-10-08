# Task 1
my_list = [1, 2, 3, 3, 4, 5, 1]
unique_list = list(set(my_list))
print(unique_list)
print(type(unique_list))
unique_list.remove(unique_list[-1])
print(unique_list)
print("=" * 50)

# Task 2
nums = {1, 2, 3}
letters = {"A", "B", "C"}
print(nums | letters)
print(nums.union(letters))
nums.update(letters)
print(nums)
print("=" * 50)

# Task 3
my_set = {1, 2, 3}
print(my_set)
my_set.clear()
print(my_set)
my_set.add("A")
my_set.add("B")
print(my_set)
my_set.discard("C")
print("=" * 50)

# Task 4
set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}
print(set_one.issubset(set_two))
print("=" * 50)

# Task 5
Dictionary = {
    "HTML" : "90%",
    "CSS" : "80%",
    "PYTHON" : "30%" 
}
print(f"{list(Dictionary.keys())[0]} Progress is {Dictionary[list(Dictionary.keys())[0]]}")
print(f"{list(Dictionary.keys())[1]} Progress is {Dictionary[list(Dictionary.keys())[1]]}")
print(f"{list(Dictionary.keys())[2]} Progress is {Dictionary[list(Dictionary.keys())[2]]}")