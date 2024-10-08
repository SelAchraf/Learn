def add_two_lists(first,second):
    print(f"The result of adding {first} + {second} is:", end=" ")
    
    if len(first) > len(second):
        difference = len(first) - len(second)
        for i in range (0,difference):
            second.append(0)
    elif len(first) < len(second):
        difference = len(second) - len(first) 
        for i in range (0,difference):
            first.append(0)

    List_result = []
    index, add = 0, 0
    while index < len(first):
        result = first[index] + second[index]
        if add:
            if result + add >= 10:
                # List_result.append(int(str(result + add)[1]))
                # add = int(str(result + add)[0])
                List_result.append((result + add) % 10)
                add = (result + add) // 10
            else:
                List_result.append(result + add)
        else:
            if result >= 10:
                # List_result.append(int(str(result)[1]) )
                # add = int(str(result)[0])
                List_result.append(result % 10)
                add = result // 10
            else:
                List_result.append(result)
        index += 1
    else:
        if add:
            List_result.append(add)
    
    print(List_result)

add_two_lists([9, 0, 1],[9, 9, 9])    