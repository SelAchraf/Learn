# ============================================== Built In Functions ==============================================

# all()                             return true if all are true 
# any()                             return true if at least one is true 
# bin()
# id()
# sum()                             print(sum(iterable))         print(sum(iterable, 40))
# round()                           print(round(150.501))        print(round(150.554, 2))
# range()                           print(list(range(0, 20, 2)))
# print("Hello", "Osama", "How", "Are", "You", sep=" | ")
# print("First Line", end=" ")
# abs()                             9ima motla9a 
# pow()                             print(pow(2, 5, 10))  # (2 * 2 * 2 * 2 * 2) % 10
# min()                             min(item, item , item, or iterator)
# max()                             max(item, item , item, or iterator)
# slice()                           print(a[slice(5)])          print(a[slice(2, 5)])
# enumerate(iterable, start=0)      object
# reversed(iterable)                object

# ============================================== Built In Functions => Map ==============================================

# [1] Map Take A Function + Iterator
# [2] Map Called Map Because It Map The Function On Every Element
# [3] The Function Can Be Pre-Defined Function or Lambda Function

# def formatText(text):
#     return f"- {text.strip().capitalize()} -"
# myTexts = [" OSama ", "AHMED", "  sAYed  "]
# myFormatedData = map(formatText, myTexts)           # object
# for name in list(myFormatedData):
#     print(name)

# ============================================== Built In Functions => Filter ==============================================

# [1] Filter Take A Function + Iterator
# [2] Filter Run A Function On Every Element
# [3] The Function Can Be Pre-Defined Function or Lambda Function
# [4] Filter Out All Elements For Which The Function Return True
# [5] The Function Need To Return Boolean Value

# def checkNumber(num):
#     return num > 10
# myNumbers = [0, 0, 1, 19, 10, 20, 100, 5, 0]
# myResult = filter(checkNumber, myNumbers)
# for number in myResult:
#     print(number)

# ============================================== Built In Functions => Reduce ==============================================

# [1] Reduce Take A Function + Iterator
# [2] Reduce Run A Function On FIrst and Second Element And Give Result
# [3] Then Run Function On Result And Third Element
# [4] Then Run Function On Rsult And Fourth Element And So On
# [5] Till One ELement is Left And This is The Result of The Reduce
# [6] The Function Can Be Pre-Defined Function or Lambda Function

# from functools import reduce
# def sumAll(num1, num2):
#     return num1 + num2
# numbers = [1, 8, 2, 9, 100]
# result = reduce(sumAll, numbers)
# result = reduce(lambda num1, num2: num1 + num2, numbers)
# print(result)

# ============================================== Built In Functions => zip ==============================================

# Loop on Many Iterators With Zip() 
# zip() Return A Zip Object Contains All Objects
# zip() Length Is The Length of Lowest Object

# list1 = [1, 2, 3, 4, 5]
# list2 = ["A", "B", "C", "D"]
# tuple1 = ("Man", "Woman", "Girl", "Boy")
# dict1 = {"Name": "Osama", "Age": 36, "Country": "Egypt", "Skill": "Python"}

# for item1, item2, item3, item4 in zip(list1, list2, tuple1, dict1):

#     print("List 1 Item =>", item1)
#     print("List 2 Item =>", item2)
#     print("Tuple 1 Item =>", item3)
#     print("Dict 1 Key =>", item4, "Value =>", dict1[item4])

# ultimateList = zip(list1, list2)
# print(ultimateList)
# for item in ultimateList:
#     print(item)