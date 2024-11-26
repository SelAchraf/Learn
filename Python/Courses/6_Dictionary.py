# ============================================== Dictionary ==============================================

# [1] Dict Items Are Enclosed in Curly Braces {}
# [2] Dict Items Are Contains Key : Value
# [3] Dict Key Need To Be Immutable => (Number, String, Tuple) List Not Allowed
# [4] Dict Value Can Have Any Data Types
# [5] Dict Key Need To Be Unique
# [6] Dict Is Not Ordered You Access Its Element With Key

# ============================================== Dictionary Methods ==============================================

# .clear()
# .update()
# .copy()
# .keys()  
# .values()
# .setdefault()                     print(user.setdefault("age", 36))       if "age" exist in the dict it will print his value else it will add "age" with his value in the dict
# .popitem()                        print the last item of the dict
# .items()
# dict.fromkeys()

# ============================================== Advanced Dictionary Loop ==============================================

# myUltimateSkills = {
#     "HTML": {
#         "Main": "80%",
#         "Pugjs": "80%"
#     },
#     "CSS": {
#         "Main": "90%",
#         "Sass": "70%"
#     }
# }
# for main_key, main_value in myUltimateSkills.items():
#     print(f"{main_key} Progress Is: ")
#     for child_key, child_value in main_value.items():
#         print(f"- {child_key} => {child_value}")