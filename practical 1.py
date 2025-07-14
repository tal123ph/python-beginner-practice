#   Write a class called Order which stores item and its prices.Use Dunder function __gt__ () to convey that:
#   "order1 > order2 if price of order 1 > order 2"
class Order:
    def __init__(self , item , price):
        self.items= item
        self.price= price

    def __gt__(self , ord2):
        return self.price > ord2.price
ord1=Order("chips" , 20)
ord2=Order("tea" , 15)

print(ord1>ord2)

    
        
    