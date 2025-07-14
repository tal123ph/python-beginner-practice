# i=1
# while i<=5:
#     print("Muhammad talha", i)
#     i+=1
# i=1
# while i<=18:
#     print(i)
#     i+=1
 #for reverse iteration
# i=1
# while i<=100:
#     print(i)
#     i+=1
# i=100
# while i>=1:
#     print(i)
#     i-=1
# n=int(input("enter the name of table you want to print: "))
# i=1
# while i<=10:
#     print(n * i)
#     i+=1
#  print element of the following list using loops.
# num=[1,4,9,16,25,36,49,64,81,100]
# idx=0
# while idx<len(num):
#     print(num[idx])
#     idx+=1

# students=["TALHA","MUHAMMAD","REHAN","AFZAL","HUZAIFA"]
# idx=0
# while idx<len(students):
#     print(students[idx])
#     idx+=1
                        #  search for a number x in this tuple using loop
# num=(1,4,9,16,25,36,49,64,81,100)
# x=25
# i=0
# while i<len(num):
#     if (num[i]==x):
#         print("found at idx",i)
#     else:
#         print("Finding___")
#     i+=1

# i=1
# while i<=20 :
#     print(i)
#     if (i==15):
#         break
#     i+=1
# print("loop has ended")
# i=0
# while i<=20 :
    
#     if (i==15 or i==16):
#         i+=1
#         continue
#     print(i)
#     i+=1
# print("loop has ended")
#                         for loop for traversing on a list,tuple or any string
# tuple=(1,2,3,4,5,6,7,8,9,10)
# for num in tuple:
#     print(num)
# str=("MUHAMMADTALHAAFZAL")
# for cha in str:
#     if (cha=="D"):
#         print("o found")
#         break
#     print(cha)
# print("end")

#        for loop in python
# num=(1,2,2,3,45,79,45,79)
# x=79
# idx=0
# for el in num:
#     if(el==x):
#         print("number found at idx", idx)
#     idx+=1
# range in python
#print(range(5))
# seq=range(5)
# print(seq[0])
# print(seq[1])
# print(seq[2])
# print(seq[3])
# seq=range(5)
# for el in seq:
#     print(el)
# for el in range(10,20,2):
#     print(el)
#                                  practice questions
# for el in range(1,101):
#     print(el)
# for el in range(100,0,-1):
#      print(el)
#            prnt the multiplication table of number n
# n=int(input("enter a number of multiplication"))
# for el in range(1,11,):
#     print(n*el)
#                                          pass statement
# for i in range(5):
#     pass
# print("some useful work")
#                          to find the sum of natural number
# n=5
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print("sum of natural number is :",sum )
#                                                         using while loop
# n=5
# sum=0
# i=1
# while(i<=5):
#     sum+=i
#     i+=1
# print("sum of natural number is :",sum )
#                                                  factorial first five natural number 
n=5
fac=1
i=1
while(i<=5):
    fac*=i
    i+=1
print("fac of first five natural number is :",fac )
