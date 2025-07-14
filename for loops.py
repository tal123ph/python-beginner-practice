#                                   For loop practical questions
# Print num from 1 to 5 using for loop
# for i in range(1, 11):
#     print(i,end="  ")       
        
# # Print name upto 10 times  using for loop
# for i in range(1, 11):
#     print("Muhammad Talha", )

# # Print num from 1 to 5 using for loop
# for i in range(1, 3):
#     print((1,2,3,4,5,6,7,8,9,10),end=" , ")   


#  print squares of number from 1 to 5
# for i in range(1, 6):
#     print(i ** 2, end="  ")


# #  print all even number from 1 to 10
 
# for i in range(1, 11):
#     if i % 2==0:
#         print(i, end=" ")
#     print("loop has ended")

# calculate sum of number b/w 1 to 10

# sum=0
# for i in range(1, 11):
#     sum+=i
# print(f"sum is {sum}")

#  reverse the word python using for loop

# word="Python"
# for i in range(len(word)-1, -1, -1):
#     print(word[i], end="")


#  write a prograam to count vowels in word "Education"
# vowels="aeiou"
# word="education"
# count=0
# for chr in word:
#     if chr in vowels:
#         count+=1
    
# print(f"Total vowels in {word} is {count}")


#  calculate factorial of a given number
# number=int(input("Enter a number"))
# fact=1
# for i in range(1, number+1):
#     fact*=i

# print(f"factorial of {number} is {fact}")

#  print fiabonnaci sequence upto 10 terms
n_terms = 10                                    
first = 0                                       
second = 1

print("Fibonacci sequence up to 10 terms:")
for i in range(n_terms):
    print(first, end=" ")
    next_term = first + second
    first = second
    second = next_term





                   
                   
             