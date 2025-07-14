#  Topic no 1:-    escape sequence character
# str1= "This is string.\nand we are creating it in a python"
# print(str1) 
# str2="This is string.\twe are creating it in a python"
# print(str2)
# # concatenation
# name1= "Hello"
# name2= "World"
# length of string:-
# print(len(name1+ " " +name2))      #we will use len(str) funtion to caluclating lenth of string. 
# indexing
# str = ("MUHAMMAD TALHA")
# ch= str[2]
# print(ch)
# print(str[3])
# slicing the string
# str=("SCHOOL")
# print(str[2:4])
# print(str[0:6])
# print(str[0:])    it will automatically detect we have to go end
# print(str[:6])   it will give full string slice from zero to 5
# print(str[0:len(str)])
# NEGATIVE INDEX
# str=("APPLE")
# print(str[-3:-1])
# rint(str[-3:])
# print(str[-5:])
#  string Functions   eg   str.ends with("")
# str=("i am a coder")
# print(str.endswith("er"))
#    str.capitalize
# str=("i am going to school.")
# print(str.capitalize())
# str=("i am going to school.")
# str=str.capitalize()
# print(str)
#    str.replaced
# str=("my  name is talha")
# print(str.replace("talha","umer"))
#    str.find
# str="my name is talha"
# print(str.find("name"))
#    str.count
# str=("name is talha")
# print(str.count("a"))
#                pratice questions
# firstname=input("Enter your First Name:-")
# print(len(firstname))
#                  WAP ask user to enter their full name and print total number of character excluding space?
# name=input("ENTER YOUR FULL NAME:-")
# no_space=name.replace(" " , "")
# print("TOTAL Character excluding space is :-" , len(no_space))
#                   WAP  ask user to input their first and last name and print total length of both name combine?
# first_name=input("Enter your first name:-")
# last_name=input("Enter your last name:-")
# full_name=first_name+"   "+last_name
# print("length of both combine name is :-" , full_name  ,"|" len(full_name))
#                         conditional statements
# age=19
# if (age>=18):
#     print("Eligible for Vote")
         # another practice question 
light="green"
if(light=="red"):
    print("stop")
elif(light=="green"):
    print("go")
elif(light=="blue"):
    print("look")


    