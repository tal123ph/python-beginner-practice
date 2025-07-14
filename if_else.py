#             if else and nested if else practical question
#Check if a Number is Even or Odd

num=int(input("enter a number"))
if (num%2==0):
  print("number is even")
else:
  print("number is odd")

  #Check if a Number is Positive, Negative, or Zero
  num=int(input("Enter a number"))
if (num>0):
  print("number is postive ")
elif(num<0):
  print("number is negative")
else:
    print("number is zero")

    #  Grade Classification

    marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
    print("Excellent")
    print("you are passed")
elif (marks >= 80 and marks<90):
    print("Grade B")
    print("Very Good")
    print("you are passed")
elif (marks >= 70 and marks<80):
    print("Grade C")
    print("Good")
    print("you are passed")
elif (marks >= 60 and marks<70):
    print("Grade D")
    print("Fair")
    print("you are passed")
elif (marks >= 50):
    print("Grade F")
    print("intermediate")
    print("you are passed")
else:
    print("Fail")

    # Age Check for Voting

age=int(input("Enter your age: "))
if (age>=18):
  print("you are eligible for voting")
  print("GO AHEAD")
  print("you can vote")
  print("Welcome to Voting Portal system.")
else:
  print("you are not eligible for voting")
  print("you have to wait for",18-age,"years")
  print("you will be eligible after",18-age,"years")
  print("Please be Paient")

  #Password Checker

  Password=input("enter a password you have granted from your college :")
if Password == "Admin123":
  print("Access Granted")
else:
  print("Access Denied")
#  Largest of Three Numbers

a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=int(input("enter third number: "))
if (a>b and a>c):
  print("first is largest number")
elif (b>c):
  print("second is largest number")
else:
  print("Third is largest number")

# Leap Year Checker

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# Check for Vowel or Consonant

ch=input("Enter a character: ").lower()
if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":   # ch in "aeiou"
  print("ch is a vowel")
elif ch .isalpha():
  print("it is a consonant")
else:
  print("invalid input")

#   Simple Login System

username=input("enter username")
password=input("enter password")
if (username=="admin" and password=="123"):
  print("login successful")
else:
  print("invalid username or password")

#Traffic Signal

signal = input("Enter traffic signal color (red/yellow/green): ").lower()

if signal == "red":
    print("Stop")
elif signal == "yellow":
    print("Ready to go")
elif signal == "green":
    print("Go")
else:
    print("Invalid signal")

#                               nested if else

#  Check if number is positive, negative or zero

num=int(input("Enter a number"))
if (num>=0):
  if(num==0):
    print("number is zero")
  else:
    print("number is positive")
else:
  print("number is negative")

#  Check whether a number is even or odd and positive or negative
num = int(input("Enter a number: "))

if num >= 0:
    if num % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
else:
    if num % 2 == 0:
        print("Negative Even")
    else:
        print("Negative Odd")

#  Find the largest of three numbers
a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=int(input("enter third number: "))
if (a>b):
  if(a>c):
    print("first is largest number")
  else:
    print("Third is largest number")
elif (b>c):
  print("second is largest number")

else:
    print("Third is largest number")

#   Check triangle type based on sides
a = int(input("Enter side x: "))
b = int(input("Enter side y: "))
c = int(input("Enter side z: "))

if a + b > c and b + c > a and c + a > b:
    if a == b and b == c:
        print("Equilateral triangle")
    elif a == b or b == c or c == a:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")
else:
    print("Not a valid triangle")

#  Check login credentials

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Invalid username")