# ============================================== Intro ==============================================

# [1] OOP Is A Paradigm Or Coding Style
#     OOP Paradigm => Means Structuring Program So The Methods[Functions] and Attributes[Data] are Bundled Into Objects
# [2] Methods => Act As Function That Use The Information Of The Object
# [3] Everything in Python is Object
# [4] If Man Is Object
#     - Attributes => Name, Age, Address, Phone Number, Info [Can Be Differnet]
#     - Methods[Behaviors] => Walking, Eating, Singing, Playing
# [5] Class Is The Template For Creating Objects [Object Constructor | Blueprint]
#     - Class Car Can Create Many Cars Object

# ============================================== Class Syntax and Info ==============================================

# [01] Class Instantiate Means Create Instance of A Class
# [02] Instance => Object Created From Class And Have Their Methods and Attributes
# [03] Class Defined With Keyword class
# [04] When Creating Object Python Look For The Built In __init__ Method
# [05] __init__ Method Called Every Time You Create Object From Class
# [06] __init__ Method Is Initialize The Data For The Object
# [07] Any Method With Two Underscore in The Start and End Called Dunder or Magic Method
# [08] self Refer To The Current Instance Created From The Class And Must Be First Param
# [09] self Can Be Named Anything
# [10] In Python You Dont Need To Call new() Keyword To Create Object

# ============================================== Instance Attributes and Methods ==============================================

# class Member:
#     def __init__(self, first_name, middle_name, last_name):
#         self.fname = first_name
#         self.mname = middle_name
#         self.lname = last_name
# member_one = Member("Osama", "Mohamed", "Elsayed")
# print(member_one.fname, member_one.mname, member_one.lname)

# ----------------------------------------------------

# Instance Methods: Take Self Parameter Which Point To Instance Created From Class
# Instance Attributes: Instance Attributes Defined Inside The Constructor
# Instance Methods Can Have More Than One Parameter Like Any Function
# Instance Methods Can Freely Access Attributes And Methods On The Same Object
# Instance Methods Can Access The Class Itself

# class Member:
#     def __init__(self, first_name, middle_name, last_name, gender):
#         self.fname = first_name
#         self.mname = middle_name
#         self.lname = last_name
#         self.gender = gender
#     def full_name(self):
#         return f"{self.fname} {self.mname} {self.lname}"
#     def name_with_title(self):
#         if self.gender == "Male":
#             return f"Hello Mr {self.fname}"
#         elif self.gender == "Female":
#             return f"Hello Miss {self.fname}"
#         else:
#             return f"Hello {self.fname}"
#     def get_all_info(self):
#         return f"{self.name_with_title()}, Your Full Name Is: {self.full_name()}"
# member_one = Member("Osama", "Mohamed", "Elsayed", "Male")
# print(member_one.get_all_info())

# ============================================== Class Attributes ==============================================

# Class Attributes: Attributes Defined Outside The Constructor

# class Member:
#     not_allowed_names = ["Hell", "Shit", "Baloot"]
#     users_num = 0
#     def __init__(self, first_name, middle_name, last_name, gender):
#         self.fname = first_name
#         self.mname = middle_name
#         self.lname = last_name
#         self.gender = gender
#         Member.users_num += 1  # Member.users_num = Member.users_num + 1
#     def delete_user(self):
#         Member.users_num -= 1  # Member.users_num = Member.users_num -1
#         return f"User {self.fname} Is Deleted."
# print(Member.users_num)
# member_one = Member("Osama", "Mohamed", "Elsayed", "Male")
# member_two = Member("Ahmed", "Ali", "Mahmoud", "Male")
# member_three = Member("Mona", "Ali", "Mahmoud", "Female")
# member_four = Member("Shit", "Hell", "Metal", "DD")
# print(Member.users_num)
# print(member_four.delete_user())
# print(Member.users_num)

# ============================================== Class Methods & Static Methods ==============================================

# ------------------ Class Methods ------------------------

# - Marked With @classmethod Decorator To Flag It As Class Method
# - It Take Cls Parameter Not Self To Point To The Class not The Instance
# - It Doesn't Require Creation of a Class Instance
# - Used When You Want To Do Something With The Class Itself

# ------------------ Static Methods ------------------------

# - Marked With @staticmethod Decorator To Flag It As Static Method
# - It Takes No Parameters
# - Its Bound To The Class Not Instance
# - Used When Doing Something Doesnt Have Access To Object Or Class But Related To Class

# ----------------------------------------------------

# class Member:
#     users_num = 0
#     @classmethod
#     @staticmethod
#     def say_hello():
#         print("Hello From Static Method")
#     def __init__(self, first_name, middle_name, last_name, gender):
#         self.fname = first_name
#         self.mname = middle_name
#         self.lname = last_name
#         self.gender = gender
#         Member.users_num += 1  
# member_one = Member("Osama", "Mohamed", "Elsayed", "Male")
# member_two = Member("Ahmed", "Ali", "Mahmoud", "Male")
# member_three = Member("Mona", "Ali", "Mahmoud", "Female")
# member_four = Member("Shit", "Hell", "Metal", "DD")
# Member.show_users_count()
# Member.say_hello()

# ============================================== Magic Methods ==============================================

# self.__class__ => The class to which a class instance belongs
# __str__ => Gives a Human-Readable Output of the Object
# __len__ => Returns the Length of the Container, called When We Use the Built-in len() Function on the Object
#            

# class Skill:
#     def __init__(self):
#         self.skills = ["Html", "Css", "Js"]
#     def __str__(self):
#         return f"This is My Skills => {self.skills}"
#     def __len__(self):
#         return len(self.skills)
# profile = Skill()
# print(profile)
# print(len(profile))
# print(profile.__class__)
# my_string = "Osama"
# print(my_string.__class__)
# print(str.upper(my_string))

# ============================================== Inheritance ==============================================

# class Food:                                                   # Base Class
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#         print(f"{self.name} Is Created From Base Class")
#     def eat(self):
#         print("Eat Method From Base Class")
# class Apple(Food):  # Derived Class
#     def __init__(self, name, price, amount):
#         # Food.__init__(self, name)                           # Create Instance From Base Class
#         super().__init__(name, price)
#         self.amount = amount
#         print(f"{self.name} Is Created From Derived Class And Price Is {self.price} And Amount Is {self.amount}")
#     def get_from_tree(self):
#         print("Get From Tree From Derived Class")
# food_two = Apple("Pizza", 150, 500)
# food_two.eat()
# food_two.get_from_tree()

# ============================================== Multiple Inheritance ==============================================

# ------------------ First method ------------------------

# class BaseOne:
#     def __init__(self):
#         print("Base One")
#     def func_one(self):
#         print("One")
# class BaseTwo:
#     def __init__(self):
#         print("Base Two")
#     def func_two(self):
#         print("Two")
# class Derived(BaseOne, BaseTwo):
#     pass
# my_var = Derived()
# print(Derived.mro())
# my_var.func_one()
# my_var.func_two()

# ------------------ Second method ------------------------

# class Base:
#     pass
# class DerivedOne(Base):
#     pass
# class DerivedTwo(DerivedOne):
#     pass

# ============================================== Polymorphism ==============================================

# class A:
#     def do_something(self):
#         print("From Class A")
#         raise NotImplementedError("Derived Class Must Implement This Method")
# class B(A):
#     def do_something(self):
#         print("From Class B")
# class C(A):
#     def do_something(self):
#         print("From Class C")
# my_instance = B()
# my_instance.do_something()

# ============================================== Encapsulation ==============================================

# Restrict Access To The Data Stored in Attirbutes and Methods

# ------------------ Public ------------------------

# - Every Attribute and Method That We Used So Far Is Public
# - Attributes and Methods Can Be Modified and Run From Everywhere
# - Inside Our Outside The Class

# ------------------ Protected ------------------------

# - Attributes and Methods Can Be Accessed From Within The Class And Sub Classes
# - Attributes and Methods Prefixed With One Underscore _

# ------------------ Private ------------------------

# - Attributes and Methods Can Be Accessed From Within The Class Or Object Only
# - Attributes Cannot Be Modified From Outside The Class
# - Attributes and Methods Prefixed With Two Underscores __

# ----------------------------------------------------

# class Member:
#     def __init__(self, name):
#         self.name = name              # Public
# one = Member("Ahmed")
# print(one.name)
# one.name = "Sayed"
# print(one.name)
# class Member:
#     def __init__(self, name):
#         self._name = name             # Protected
# one = Member("Ahmed")
# print(one._name)
# one._name = "Sayed"
# print(one._name)
# class Member:
#     def __init__(self, name):
#         self.__name = name            # Private
#     def say_hello(self):
#         return f"Hello {self.__name}"
# one = Member("Ahmed")
# print(one.__name)
# print(one.say_hello())
# print(one._Member__name)              # To acces into a private attribute

# ============================================== Getters & Setters ==============================================

# class Member:
#     def __init__(self, name):
#         self.__name = name  # Private
#     def get_name(self):  # Getter
#         return self.__name
#     def set_name(self, new_name):
#         self.__name = new_name
# one = Member("Ahmed")
# print(one.get_name())
# one.set_name('Abbas')
# print(one.get_name())

# ============================================== @Property Decorator ==============================================

# class Member:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     @property
#     def age_in_days(self):
#         return self.age * 365
# one = Member("Ahmed", 40)
# # print(one.age_in_days())
# print(one.age_in_days)

# ============================================== ABCs => Abstract Base Class ==============================================

# - Class Called Abstract Class If it Has One or More Abstract Methods
# - abc module in Python Provides Infrastructure for Defining Custom Abstract Base Classes.
# - By Adding @absttractmethod Decorator on The Methods
# - ABCMeta Class Is a Metaclass Used For Defining Abstract Base Class

# from abc import ABCMeta, abstractmethod
# class Programming(metaclass=ABCMeta):
#     @abstractmethod
#     def has_oop(self):
#         pass
#     @abstractmethod
#     def has_name(self):
#         pass
# class Pascal(Programming):
#     def has_oop(self):
#         return "No"
#     def has_name(self):
#         return "Pascal"
# one = Pascal()
# print(one.has_oop())
# print(one.has_name())