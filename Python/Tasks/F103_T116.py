# Task 1
class Game:
    def __init__(self, name, developer, year, price):
        self.name = name
        self.developer = developer
        self.year = year
        self.price = price
    
    def price_in_pounds(self):
        return f"{self.price * 15.6} Egyptian Pounds"

game_one = Game("Ys", "Falcom", 2010, 50)
print(f"Game Name Is \"{game_one.name}\", ", end="")
print(f"Developer Is \"{game_one.developer}\", ", end="")
print(f"Release Date Is \"{game_one.year}\", ", end="")
print(f"Price In Egypt Is {game_one.price_in_pounds()}", end="")
print("","=" * 50)

# Task 2
class User:
    def __init__(self, fname, mname, age, gender):
        self.fname = fname 
        self.mname = mname
        self.age = age
        self.gender = gender
    
    def full_details(self):
        return f"Helllo {"Mr" if self.gender == "Male" else "Mrs"} {self.fname} {self.mname[0]}. [{40 - self.age}] Years To Reach 40"
user_one = User("Osama", "Mohamed", 38, "Male")
user_two = User("Eman", "Omar", 25, "Female")

print(user_one.full_details()) # Hello Mr Osama M. [02] Years To Reach 40
print(user_two.full_details()) # Hello Mrs Eman O. [15] Years To Reach 40
print("=" * 50)

# Task 3
class Message:
    @classmethod
    def print_message(cls):
        return "Hello From Class Message"

print(Message.print_message())
print("=" * 50)

# Task 4 
class Games:
    def __init__(self, input):
        self.input = input
        
    def show_games(self):
        if type(self.input) == list:
            print(f"I Have Many Games:")
            for i in self.input:
                print(f"-- {i}")
        elif type(self.input) == str:
            print(f"I Have One Game Called \"{self.input}\"")
        else:   
            print(f"I Have {self.input} Game.")

my_game = Games("Shadow Of Mordor")
my_games_names = Games(["Ys II", "Ys Oath In Felghana", "YS Origin"])
my_games_count = Games(80)

my_game.show_games()
my_games_names.show_games()
my_games_count.show_games()
print("=" * 50)

# Task 5
class Members:
    def __init__(self, n, p):
        self.name = n
        self.permission = p

    def show_info(self):
        return f"Your Name Is {self.name} And You Are {self.permission}"

class Admins(Members):
    pass

class Moderators(Admins):
    pass

member_one = Admins("Osama", "Admin")
member_two = Moderators("Ahmed", "Moderator")

print(member_one.show_info())
print(member_two.show_info())
print("=" * 50)

# Task 6
class A:
    def __init__(self, one):
        self.one = one

class B:
    def __init__(self, two):
        self.two = two

class C:
    def __init__(self, three):
        self.three = three

class Text(A,B,C):
    def __init__(self, one, two, three):
        self.one = one
        self.two = two
        self.three = three
    def show_name(self):
        return f"The Name Is {self.one}{self.two}{self.three}"

the_name = Text("El", "ze", "ro")
print(the_name.show_name())