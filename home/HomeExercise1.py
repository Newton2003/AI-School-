"""
Not an assigniment or classwork, just a after class practice

the main section of this code is to make it in a way that has we 
create more instances of our class items, it will be appended in a list 
using the all keyword and assinging it to an empty list[]

"""
class item:
    pay_rate = 0.8
    all=[]
    def __init__(self, name:str, price:float, quantity=0):
        #this is for validation
        assert price >=0, f"{price} is not greater or equal to zero"
        assert quantity>=0, f"{quantity} is not greater or equal to zero"
        
        #over here we are assigning self to the object
        self.name = name 
        self.price = price
        self.quantity = quantity
        
        #actions to execute
        item.all.append(self)
        
    def cal_total_price(self):
        return self.price * self.quantity
    
    def discount(self):
        self.price *=self.pay_rate # its a good idea to asscess the pa rate from the instance level so when u want to add a specific dicount to an item it will be easy 
         
    def __repr__(self):
        return f"item('{self.name}', '{self.price}', '{self.quantity }')"
        
#creating new instances of the class

item1=item("laptop",1000,2)
item2=item("phone", 500, 1)
item3=item("bags", 300, 2)
item4=item("pouch", 200, 2)
item5=item("adapter", 700,3)
item6=item("screens", 100, 6)

print(item.all)        
#  so using this ==> print(item.all) will print out some hex location of the values which is not user friendly so we can use
# using a magic method __repr__