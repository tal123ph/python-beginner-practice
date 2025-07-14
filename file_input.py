# f= open("demo.txt" , "r")
# data =f.read()
# print(data)
# print(type(data))
# f.closed


# f= open("demo.txt" , "rt")
# data =f.read()
# print(data)
# print(type(data))
# f.closed


# f= open("demo.txt" , "r+")  # for read and write
# data =f.read()
# print(data)
# print(type(data))
# f.closed



# f= open("demo.txt" , "W+")
# data =f.read()
# print(data)
# print(type(data))
# f.closed



# f= open("demo.txt" , "X+") #for creating  anew file
# data =f.read()
# print(data)
# print(type(data))
# f.closed



# f= open("demo.txt" , "a+")     # open for writing and appending to the end of file
# data =f.read(5)
# line1=f.readline()   # which print the the five character
# print(line1)
# print(type(line1))
# f.closed


# f= open("demo.txt" , "W+")  #it deletes my file and rewrite it again
# data =f.write("I want to learn java script tomorrow.")

# f.closed



# with open("demo.txt" , "W+") as f  #it deletes my file and rewrite it again
# data =f.write("I want to learn java script tomorrow.")
# print(data)


                                       #   Modules 
#                                  OS module

# import os
# os.remove("demo.txt")
#                                      Some practice question
#       Create a new file “practice.txt” using python. Add the following data in it:

# WAF that replace all occurrences of “java” with “python” in above file.

# Search if the word “learning” exists in the file or not.

# with open ("Practice.txt","w") as f:
#     f.write("Hi every one . I am Talha. and\nwe are learning File I/O in Python.\n")
#     f.write("Using java.\nI like programming in java.")
# with open ("Practice.txt","r") as f:
#     data=f.read()
#     new_data=data.replace("java","python")
#     print(new_data)
# with open ("Practice.txt","w") as f:
#     f.write(new_data)
    
# word="learning"
# with open ("practice.txt","r")as f:
#         data=f.read()
#         if data.find(word) !=-1:
#             print("Found")
#         else:
#             print("not found")

# def check_for_line():
#      word="learning"
#      line_no =1
#      data=True
#      with open ("practice.txt","r")as f:
#           while data:
#                data=f.readline()
#                if (word in data):
#                     print(line_no)
#                     return
#                line_no+=1
                     

#           return-1
# check_for_line()


               #From a file containing numbers separated by comma, print the count of even numbers. 
with open ("make.txt","w") as f:
     f.write("1,2,76,84,90,101")
with open ("make.txt","r") as f:
     data=f.read()
count=0
nums=data.split(",")
print(nums)
for value in nums:
     if (int(value) % 2==0):
          print(value)
          count+=1
print("number of even value is :" ,count)         
            
          
     
     
     
     
