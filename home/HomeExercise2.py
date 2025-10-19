"""
Not an assigniment or classwork, just a after class practice

the main section of this code is to organize our valuse we have in our instance object 
usign csv comma sepreated values 

"""
import csv

class Item:
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
        Item.all.append(self)
        
    def cal_total_price(self):
        return self.price * self.quantity
    
    def discount(self):
        self.price *=self.pay_rate # its a good idea to asscess the pa rate from the instance level so when u want to add a specific dicount to an item it will be easy 
        
        
    #we will use a decorator called the @classmethod that will change the behaviour of the class and must be called before the class  
    @classmethod  
    def instantaite_from_csv(Item):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            
            Item (
                 name = item.get('name'),
                 price = float(item.get('price')),
                 quantity = item.get('quantity')
            )
             
    def __repr__(self):
        return f"item('{self.name}', '{self.price}', '{self.quantity }')"
        
#creating new instances of the class

Item.instantaite_from_csv()   
print(Item.all)     
#  so using this ==> print(item.all) will print out some hex location of the values which is not user friendly so we can use
# using a magic method __repr__