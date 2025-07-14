#                     while loop practical question
# write a program which print number from 10 to 15
# number=10
# while number <= 15:
#     print(number)
#     number+= 1


#  print cubes of number from 1 to 5
# num=1
# while num <= 5:
#     print(num ** 3 , end=" ")
#     num+=1 

#   print od number from 1 to 10

# i = 1

# while i <= 10:
#     if i % 2 != 0:
#         print(i)
#     i += 1

#  calculte product of number from 1 to 5
# number=1
# product=1
# while number <= 5:
#     product*=number
#     number+=1

# print("product from 1 to 5 is: ",  product )

#          reverse each word in sentence"Hello World"
# sentence = "Hello World"
# words = sentence.split()

# for word in words:
#     i = len(word) - 1
#     while i >= 0:
#         print(word[i], end="")
#         i -= 1
#     print(end=" ")

#        write a program which count number of consonants in word "learning"

# word=input("enter a word")
# vowels="aeiou"
# count=0
# index=0
# while index < len(word):
#     if word[index].lower() not in vowels and word[index].isalpha():
#         count+=1
#     index+=1
# print(f"number of consonants in '{word}' is {count}")



# wap to calculate first five multiple of three
# multiple=3
# count=1
# while count <= 5:
#     print(multiple , end=" ")
#     multiple+=3
#     count+=1


#                      write a program to calculate 3 to power 4
# base = 3
# exponent = 4

# result = 1
# count = 0

# while count < exponent:
#     result = result * base
#     count = count + 1

# print(f"{base} to the power {exponent} is {result}")

#       wap to check if a given number is perfect square

# number =int(input("Enter a number : "))
# i=1
# is_perfect_square=False
# while i*i <= number:
#     if i * i == number:
#         is_perfect_square= True
#         break
#     i+=1
# if is_perfect_square:
#         print(f"{number} is a perfect square")
# else:
#         print(f"{number} is not a perfect square")



#      WAP to count specific character "s" in a string "success"  or any input


string=input("Enter a string:  ")
char_to_count= input("Enter a specific char in string you want to count to count : ")
count=0
index=0
while index < len(string):
    if string[index] == char_to_count:
        count+=1
    index+=1
    
print(f"character to count in a {string} is {count}")

# finish

    

    
        
