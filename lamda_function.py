#                     What is lamda function
# x=lambda x: x**2
# print(x(2))

# q=lambda x: x+x**2
# print(q(2,2))

# a=lambda x,y: x+y
# print(a(2,4))

# z=lambda x,y: x%y
# print(z(2,4))
#                       we use this along with hiegher order function(a funtion which needs another funtion in his 
 #input to complete his work)#

# a =lambda x: x[0]=='a'
# print(a("apple"))            #gives True

# a =lambda x: x[0]=='a'
# print(a("banana"))            #gives False
#                 we can make funtion of even and odd number only in a single line

a=lambda x: "Even" if x%2==0  else "Odd"
print(a(4))