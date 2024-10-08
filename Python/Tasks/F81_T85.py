# Task 1
def reverse_string(my_string):
    for index in reversed(my_string):
        yield index

# Reverse The String
for c in reverse_string("Elzero"):
    print(f"{c}", end=" ")
print("\n"+"=" * 50)

# Task 2
def Decorator(function):
    def deco():
        print("Sugar Added From Decorators")
        function()
        print("####################")
    return deco

@Decorator     
def make_tea():
    print("Tea Created")
    
@Decorator
def make_coffe():
    print("Coffe Created")

make_tea()
make_coffe()