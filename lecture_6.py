#                        print("welcome to python lecture number 6")
#                           Function and recurrison
# def cal_sum(a,b):
#     sum=a+b
#     print(sum)
#     return sum
# cal_sum(1,2)
# def print_hello():
#     print("Hello World. I am Talha. Nice to meet you.")

# print_hello()
# print_hello()
# print_hello()
# print_hello()
# print_hello()
# print_hello()
# print_hello()
# print_hello()
# print_hello()
# def print_hello():
#      print("Hello World. I am Talha. Nice to meet you.")
# output=print_hello()
# print(output)    
#     made a function which calculate avarege of three number .
# def cal_average(a,b,c):
#      sum=a+b+c
#      average=sum / 3
#      print(average)
#      return average

# cal_average(2,2,2)
#       default parameters
# def cal_product(a=1,b=3):
#     product=a*b
#     print(product)
#     return product
# cal_product()
#                  wap to print lent of list
# cities=[1,2,2,2,23,3,4,4,34,5]
# def cal_len(cities):
#   print(len(cities))

# cal_len(cities)
#     print all item in list in one line using function
# cities=[1,2,2,2,23,3,4,4,34,5]
# def cal_len(list):
#     for item in list:
#         print(item,end=" ")
        
# cal_len(cities)
# print()
#                    find factorial of n

# def cal_fac(n):
#     fac=1
#     for i in range(1,n+1):
#          fac*=i
#     print(fac)
# cal_fac(5)
#                                   currency converter
# def converter(usd_val):
#     pk_val=usd_val*270
#     print(usd_val,"usd_val=" , pk_val , "pk_val")

# converter()
#                                         recurrsion function
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
print("end")
show(10)