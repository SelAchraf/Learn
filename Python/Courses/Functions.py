# ============================================== Function Packing, Unpacking Arguments *Args ==============================================

# myList = [1, 2, 3, 5]
# def show_details(name, *skills):
#     print(f"Hello {name} Your Skills Is: ")
#     for skill in skills:
#         print(skill)
# show_details("Osama", "Html", "CSS", "JS")

# ============================================== Function Packing, Unpacking Arguments **KWArgs ==============================================

# mySkills = {
#     'Html': "80%",
#     'Css': "70%",
#     'Js': "50%",
#     'Python': "80%",
#     "Go": "40%"
#     }
# def show_skills(**skills):
#     for skill, value in skills.items():
#         print(f"{skill} => {value}")
# show_skills(**mySkills)

# ============================================== Function Scope ==============================================

# mySkills = {
# x = 1     # Global Scope
# def one():
#     global x
#     x = 2
#     print(f"Print Variable From Function Scope {x}")
# def two():
#     x = 10
#     print(f"Print Variable From Function Scope {x}")
# one()       # 2
# print(f"Print Variable From Global Scope {x}")      # 2
# two()       # 10
# print(f"Print Variable From Global Scope After One Function Is Called {x}")     #2

# ============================================== Function Recursion ==============================================

# def cleanWord(word):
#     if len(word) == 1:
#         return word
#     if word[0] == word[1]:
#         return cleanWord(word[1:])
#     return word[0] + cleanWord(word[1:])
# print(cleanWord("WWWoooorrrldd"))

# ============================================== Function lambda ==============================================

# [1] It Has No Name
# [2] You Can Call It Inline Without Defining It
# [3] You Can Use It In Return Data From Another Function
# [4] Lambda Used For Simple Functions and Def Handle The Large Tasks
# [5] Lambda is One Single Expression not Block Of Code

# def say_hello(name, age) : return f"Hello {name} your Age Is: {age}"
# hello = lambda name, age : f"Hello {name} your Age Is: {age}"