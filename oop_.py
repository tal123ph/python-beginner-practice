#                                               Classses and objects in oop
# class student:
#     name="MUHAMMAD TALHA"

# s1=student()
# print(s1.name)

# class car:
#     colour="blue"
#     model = 2024
#     brand = "mercedes"


# car1=car()
# print("\n",car1.colour,"\n",car1.model,"\n", car1.brand )
#                                       constructer function
#                                 default constructer
# def __init__(self):
#     pass
       
# class student:
#     def __init__(self , name, marks):        # parametarized constructer
#         self.name = name
#         self.marks = marks
#         print("Adding a new student in data base.")
# s1= student("Talha" , 94)
# print(s1.name , s1.marks)
# s1= student("Ali" , 45)
# print(s1.name , s1.marks)
#                                      class instance attribute
# class student:
#     collegename = "ABCD"   #class attribute

#     def __init__(self , age):
#         self.age=age    # object attribute / variable

# s1=student(19)
# print(s1.age)
# print(s1.collegename)
# #                                    Methods in python
# classes is a collection of two things . attribute(data), and methods
                             #  Methods are functions that belongs to object
# class student:
#     collegename = "ABCD"   #class attribute

#     def __init__(self , age , name):
#         self.age=age    # object attribute / variable
#         self.name =name
#     def welcome(self):
#         print("Welcome Student:" , self.name)

#     def get_age(self):
#         return self.name

# s1= student("Talha", 34)
# s1.welcome()
# print(s1.get_age())
#                Create a Student Class that takes name and marks of three subject as an arguments in constructer
#                      Then create a method to print the average.
# class student:
#     def __init__(self , name , marks):
#         self.name= name
#         self.marks= marks
#     def get_average(self):
#         sum=0
#         for value in self.marks:
#             sum+=value
#         print("hi," , self.name , "your average score is :" ,sum/3)

  
# s1=student("Muhammmad Talha" , [60,70,80])
# s1.get_average()

#                             static methods ( dont use self parameter work as a class level) (not in object level)
# class student:
#     def __init__(self , name , marks):
#         self.name= name
#         self.marks= marks

#     @staticmethod
#     def hello():
#         print("hello")

#     hello()

#     def get_average(self):
#         sum=0
#         for value in self.marks:
#             sum+=value
#         print("hi," , self.name , "your average score is :" ,sum/3)
    
  
# s1=student("Muhammmad Talha" , [60,70,80])
# s1.get_average()



#                four pillars of oop is "Abstraction, Encapsulation , inheritance , polymorphism"
#  "hiding the implementation detail of a class and showing the essential feature to user."

# "wrapping data and function into a single unit object"


#       practical question
#  create account class with 2 attributes balance and account number. Create methods for debit credit and printing the methods.
# class account:
#     def __init__(self , bal , acc):
#         self.balance= bal
#         self.account_no= acc
# #         debit method
#     def debit(self , ammount):
#         self.balance-= ammount
#         print("Rs " , ammount , "was debited")
#         print("Total Balance is :", self.get_balance())
# #         credit method
#     def credit(self , ammount):
#         self.balance+= ammount
#         print("Rs " , ammount , "was credited")
#         print("Total Balance is :", self.get_balance())

#     def get_balance(self):
#         return self.balance


# acc1=account(10000 , 1234563543647)
# acc1.debit(1000)
# acc1.credit(500)


# print("Balance is : " ,acc1.balance)
# print("Account No is : " , acc1.account_no)

#               use of del keyword in python

# class student:
#     def __init__(self , name):
#         self.name= name
        
# s1=student("Talha")
  
# del s1
#                           private and public attributes and methods in python
# class account:
#     def __init__(self , acc_no , acc_pass):
#         self.acc_no= acc_no
#         self.__acc_pass= acc_pass

#     def reset_password(self):
#         print(self.__acc_pass)


# acc1= account("12345", "abcde")
# print(acc1.acc_no)
# print(acc1.reset_password())
#                        Inheritance (single level )
# class car:
#     color= "Blue"
#     engine_number= 1234
#     is_Automatic= True
#     @staticmethod
#     def start():
#         print("car started")

#     @staticmethod
#     def stop():
#         print("car stopped")  


# class Toyotacar (car):
#     def __init__(self , nae):
#         self.name=name

# car1= Toyotacar("fortuner")
# car2= Toyotacar("peris")

# print(car1.name)
# print(car1.start())
# print(car1.color)
# print(car1.engine_number)
# print(car1.is_Automatic)

#                                            Multilevel inheritance
# class car:
#     # color= "Blue"
#     # engine_number= 1234
#     # is_Automatic= True
#     @staticmethod
#     def start():
#         print("car started")

#     @staticmethod
#     def stop():
#         print("car stopped")  


# class Toyotacar (car):
#     def __init__(self , brand):
#         self.brand=brand


# class Fortuner(Toyotacar):
#     def __init__(self, type):
#         self.type= type


# car1=Fortuner("disel")
# car1.start()

#                          multiple inheritance
# class A():
#     var1="welcome to class A"
# class B():
#     var2="welcome to class B"

# class C(A, B):
#     varc="Welcome to class C"

# c1=C()
# print(c1.var1)
# print(c1.var2)
# print(c1.varc)

#                  Super method(is used to access methods of parent class)

# class car:
#      def __init__(self, type):
#          self.type=type
#      @staticmethod
#      def start():
#          print("car started")

#      @staticmethod
#      def stop():
#          print("car stopped")  


# class Toyotacar (car):
#      def __init__(self , name ,type):
#         super().__init__(type)
#         self.name=name
#         super().start()

# car1=Toyotacar("Perious", "Electric")
# print(car1.type)

# class person:
#     name="anonymous"

#     def changeName(self,name):
#         person.name=name

# p1=person()
# p1.changeName("Rahul Kumar")
# print(p1.name)
# print(person.name)



#classs method (change the attributes of class)

# class person:
#     name="anonymous"

#     # def changeName(self,name):
#     #     person.name=name
#     @classmethod
#     def ChangeName(cls, name):
#         cls.name=name
# p1=person()
# p1.changeName("Rahul Kumar")
# print(p1.name)
# print(person.name)

             #Property 

# class person:
#     def __init__(self , math ,che ,phy ):
#         self.math=math
#         self.che=che
#         self.phy=phy
#     @property
#     def persentage(self):
#         return str((self.math + self.che + self.phy)/3) + "%"
    

# stu1=person(98,97,99)
# print(stu1.persentage)


#                                              Polymorphism in python
#                     When same operter is allowed to have different meanings according to context.
# class complex:
#     def __init__(self , real , imag):
#         self.real=real
#         self.imag=imag
#     def ShowNumber(self):
#         print(self.real,"i +",self.imag,"j")

#     def __add__(self, num2):             # for subtraction, multiplication,division we use this
#         NewReal = self.real + num2.real
#         NewImag = self.imag + num2.imag
#         return complex(NewReal , NewImag)
    

# num1=complex(1,3)
# num1.ShowNumber()
# num2=complex(5,8)
# num2.ShowNumber()
# num3= num1 + num2
# num3.ShowNumber()


#                                         Practical questions

# class circle:
#     def __init__(self, radius):
#         self.radius=radius
#     def area(self):
#         return (22/7) * self.radius ** 2        
#     def perimeter(self):
#         return 2 * (22/7) * self.radius        
# c1=circle(21)

# print(c1.area())
# print(c1.perimeter())


#                                   pracytical q 2

class Employ:

    def __init__(self , role , department , salary):
        self.role=role
        self.department=department
        self.salary=salary
    
    def ShowDetails(self):
        print("Role =" , self.role)
        print("Department =" , self.department)
        print("salary =" , self.salary)

class Engineer(Employ):                     #     Inheritance
    def __init__(self , name , age):
        self.name= name
        self.age= age
        super().__init__("Engineer" , "It" , "30,000")


eng1= Engineer("Muhammad Talha" , 40)
eng1.ShowDetails()





