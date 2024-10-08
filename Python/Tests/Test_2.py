from random import randint
from colorama import Fore, Style, init
init()
# Make a random list
Random_List = []
for i in range(0,10):
    Random_List.append(randint(0,9))
chances = 6
Result = ""
while chances > 0 :
    Try_List = []
    for i in range(0,10):
        num = int(input(f"Enter the {i+1} number: "))
        Try_List.append(num)    
    def check(Try_List):
        global Result
        for i in range (0,10):
            if Try_List[i] == Random_List[i]:
                colored_number = f"{Fore.GREEN}{Try_List[i]}{Style.RESET_ALL}"
            else:   
                exist = False
                for j in Random_List:
                    if Try_List[i] == j:
                        exist = True
                        break    
                if exist:    
                    occ, sub = 0, 0
                    # Calcule the number of occurrences of the number in Random_List where it is not equal to its counterpart in the Try_List
                    for j in range(0,10):
                        if Try_List[i] == Random_List[j] and Random_List[j] != Try_List[j]:    # we7d blasto ghalta:
                            occ +=1
                    # Calcule the number of occurrences of the number in the left part of Try_List where it is not equal to its counterpart in the Random_List
                    for j in range (0,i):
                        if Try_List[j] == Try_List[i] and Try_List[j] != Random_List[j]:
                            sub += 1
                    jaune = occ - sub
                    if jaune > 0:
                        colored_number = f"{Fore.YELLOW}{Try_List[i]}{Style.RESET_ALL}"
                    else:
                        colored_number = f"{Fore.RED}{Try_List[i]}{Style.RESET_ALL}"
                else:
                    colored_number = f"{Fore.RED}{Try_List[i]}{Style.RESET_ALL}"
            Result += colored_number + " "
        Result += "\n"
        print("Your tries :\n" + Result)
    check(Try_List)
    chances -= 1
else:
    print("Your chances are ended")
    print(f"The correct answer is:\n {Random_List}")