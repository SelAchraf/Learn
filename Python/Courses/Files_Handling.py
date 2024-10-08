# ============================================== How to use relative path for file handling ==============================================

# import os
# print(f"The main current working directory is : {os.getcwd()}")                                              
# print(f"The current file absolute path is : {os.path.abspath(__file__)}")  
# print(f"The directory path of the opened file is : {os.path.dirname(os.path.abspath(__file__))}")              
# os.chdir(os.path.dirname(os.path.abspath(__file__)))            # Change the current working directory to the directory path of the opened file 
# print(f"The new current working directory is : {os.getcwd()}")    

# ============================================== File handling ==============================================

# "r" Read    [Default Value] Open File For Read and Give Error If File is Not Exists
# "w" Write   Open File For Writing, Create File If Not Exists
# "a" Append  Open File For Appending Values, Create File If Not Exists
# "x" Create  Create File, Give Error If File Exists

# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

# file = open(r"D:\Python\Files\nfiles\osama.txt")              # r it for ignore the \n

# ============================================== Read file ==============================================

# myFile = open("File_path", "r")

# print(myFile)                       # object contain all the file lines with an \n in the end of each line
# print(myFile.name)                  # return the file path 
# print(myFile.mode)                  # return the mode (r, a, w, x)
# print(myFile.encoding)      

# print(myFile.read())                # read the file content (the default value is -1)
# print(myFile.read(5))               # read just the first 5 characters from the file 

# print(myFile.readline(5))           # read just 5 characters from the first line of the file
# print(myFile.readline())            # read the rest of the first line of the file
# print(myFile.readline())            # read the second line of the file

# print(myFile.readlines())           # return a list contain all the file lines 
# print(myFile.readlines(50))         # return a list contain the file lines but it d'ont exceed a 50 characters

# for line in myFile:                 # by looping through the lines of the file, you can read the whole file, line by line:
#     print(line)

# myFile.close()                      # Close The File

# ============================================== Write in file ==============================================

# myFile = open("File_path", "w")                         # the write mode will overwrite any existing content
# myFile.write("Hello\n")
# myFile.write("Elzero Web School\n" * 1000)

# myList = ["Oasma\n", "Ahmed\n", "Sayed\n"]              
# myFile.writelines(myList)                               # the writelines must have a list like a parameter

# ============================================== Append in file ==============================================

# myFile = open("D:\Python\Files\osama.txt", "a")         # the append mode will append to the end of the file
# myFile.write("Elzero")

# ============================================== Important infos ==============================================

# import os

# os.path.exists("demofile.txt")                        # check if the file exists or no and it return a boolean value

# os.remove("demofile.txt")                             # delete a file 

# os.rmdir("myfolder")                                  # delete an empty folder

# myFile = open("file_path", "a")
# myFile.truncate(5)                                      # it reserve the first 5 characters of the file and delete the rest

# print(myFile.tell())                                    # it show the cursor position in the file 

# myFile = open("file_path", "r")
# myFile.seek(11)                                         # it change the cursor position to read the file from the new cursor position to the end of the file 
# print(myFile.read())