################################### Using While ###################################################
# Task 1
my_nums = [15, 81, 5, 17, 20, 21, 13]
my_nums.sort(reverse = True)
index = 0
sort = 1
while index < len(my_nums):
    if my_nums[index] % 5 == 0 :
        print(f"{sort} => {my_nums[index]}")  
        sort += 1
    index += 1
else:
    print("All Numbers Printed") 
print("=" * 50)

# Task 2
index = 1
while index <= 20:
    if index == 6 or index == 8 or index == 12:
        index +=1
    else:
        print(f"{str(index).zfill(2)}")
        index +=1
else:
    print("All Numbers Printed")
print("=" * 50)

# Task 3
my_ranks = {
    'Math': 'A',
    "Science": 'B',
    'Drawing': 'A',
    'Sports': 'C'
}
index = 0
Total = 0
List = list(my_ranks.keys())
while index < len(my_ranks):
    print(f"My rank in {List[index]} Is {my_ranks[List[index]]} And This Equal {"100" if (my_ranks[List[index]]== "A") else "80" if (my_ranks[List[index]]== "B") else "40"} Points")
    if (my_ranks[List[index]]== "A"):
        Total += 100
    elif (my_ranks[List[index]]== "B"):
        Total += 80
    else:
        Total += 40
    index += 1 
else: 
    print(f"Total Points Is {Total}")
print("=" * 50)

# Task 4 
students = {
    "Ahmed": {
        "Math": "A",
        "Science": "D",
        "Draw": "B",
        "Sports": "C",
        "Thinking": "A"
    },
    "Sayed": {
        "Math": "B",
        "Science": "B",
        "Draw": "B",
        "Sports": "D",
        "Thinking": "A"
    },
    "Mahmoud": {
        "Math": "D",
        "Science": "A",
        "Draw": "A",
        "Sports": "B",
        "Thinking": "B"
    }
}

# Methode 1 (simple)
index1 = 0  
while index1 < len(students):
    Students_name = list(students.keys())[index1]
    print("-" * 30)
    print(f"-- Student Name => {Students_name}")
    print("-" * 30)
    index2 = 0
    Total = 0
    while index2 < len(students[Students_name]):
        module_name = list(students[Students_name].keys())[index2]
        module_degree = students[Students_name][module_name]
        print(f"- {module_name} => {"100"  if (module_degree == "A") else "80" if (module_degree == "B") else "40" if (module_degree == "C") else "20"} Points")
        if (module_degree == "A"):
            Total += 100
        elif (module_degree == "B"):
            Total += 80
        elif (module_degree == "C"):
            Total += 40
        else:
            Total += 20
        index2 += 1
    else:
        print(f"Total Points For {Students_name} Is {Total}")
    index1 += 1   
print("=" * 50)

# Methode 2 (using item())
index1 = 0
while index1 < len(students):
    student_names=list(students.items())[index1][0]
    student_modules=list(students.items())[index1][1]
    print("-" * 30)
    print(f"-- Student Name => {student_names}")
    print("-" * 30)
    index2 = 0
    Total = 0
    while index2 < len(student_modules):
        module_name = list(student_modules)[index2]
        module_degree = students[student_names][module_name]
        print(f"- {module_name} => { "100" if module_degree == "A" else "80" if module_degree == "B" else "40" if module_degree == "C" else "20"} Points")
        if module_degree == "A":
            Total += 100
        elif module_degree == "B":
            Total += 80
        elif module_degree == "C":
            Total += 40
        else:
            Total += 20
        index2 += 1
    else :
        print(f"Total Points For {student_names} Is {Total}")
    index1 += 1

################################### Using for ###################################################
# Task 1
my_nums = [15, 81, 5, 17, 20, 21, 13]
my_nums.sort(reverse=True)
index = 1
for num in my_nums:
    if num % 5 == 0: 
        print(f"{index} => {num}")
        index += 1
print("All Numbers Printed")
print("=" * 50)

# Task 2
for num in range (1,21):
    if num != 6 and num != 8 and num != 12:
        print(str(num).zfill(2))
print("All Numbers Printed")
print("=" * 50)

# Task 3
my_ranks = {
    'Math': 'A',
    "Science": 'B',
    'Drawing': 'A',
    'Sports': 'C'
}  
Total = 0  
for module in my_ranks: 
    print(f"My Rank in {module} Is {my_ranks[module]} And This Equal {"100" if my_ranks[module] == "A" else "80" if my_ranks[module] == "B" else "40"} Points")
    if my_ranks[module] == "A":
        Total += 100
    elif my_ranks[module] == "B":
        Total += 80 
    else:
        Total += 40
print(f"Total Points Is {Total}")
print("=" * 50)

# Task 4
students = {
    "Ahmed": {
        "Math": "A",
        "Science": "D",
        "Draw": "B",
        "Sports": "C",
        "Thinking": "A"
    },
    "Sayed": {
        "Math": "B",
        "Science": "B",
        "Draw": "B",
        "Sports": "D",
        "Thinking": "A"
    },
    "Mahmoud": {
        "Math": "D",
        "Science": "A",
        "Draw": "A",
        "Sports": "B",
        "Thinking": "B"
    }
}
for student, module in students.items():
    print("-"*30)
    print(f"-- Student Name => {student}")
    print("-"*30)
    Total = 0
    for module_name, module_degree in module.items():
        print(f"- {module_name} => {"100" if module_degree == "A" else "80" if module_degree == "B" else "40" if module_degree == "C" else "20"} Points")
        if module_degree == "A":
            Total += 100
        elif module_degree == "B":
            Total += 80
        elif module_degree == "C":
            Total += 40
        else:
            Total += 20
    print(f"Total Points For {student} Is {Total}")