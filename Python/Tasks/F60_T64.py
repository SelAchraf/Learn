# Task 1
def get_score(**modules):
    for module_name, module_score in modules.items():
        print(f"{module_name} => {module_score}")
    
get_score(Math=90, Science=80, Language=70)
print("-" * 17)
get_score(Logic=70, Problems=60)
print("=" * 50)

# Task 2
def get_people_scores(name=None, **modules):
    if name and modules:
        print(f"Hello {name} This Is Your Score Table:")
        for module_name, module_score in modules.items():
            print(f"{module_name} => {module_score}")
    elif name and not modules:
        print(f"Hello {name} You Have No Scores To Show")
    else:
        for module_name, module_score in modules.items():
            print(f"{module_name} => {module_score}")
get_people_scores("Osama", Math=90, Science=80, Language=70)
print("-" * 17)
get_people_scores("Mahmoud", Logic=70, Problems=60)
print("-" * 17)
get_people_scores(Logic=70, Problems=60)
print("-" * 17)
get_people_scores("Ahmed")
print("=" * 50)

# Task 3
modules={
    "Math":90,
    "Science":80,
    "Language":70
}
def get_the_scores(name=None, **modules):
    if name and modules:
        print(f"Hello {name} This Is Your Score Table:")
        for module_name, module_score in modules.items():
            print(f"{module_name} => {module_score}")
    elif name and not modules:
        print(f"Hello {name} You Have No Scores To Show")
    else:
        for module_name, module_score in modules.items():
            print(f"{module_name} => {module_score}")
get_the_scores("Osama", **modules)
print("-" * 17)
get_the_scores("Osama")
print("-" * 17)
get_the_scores(**modules)