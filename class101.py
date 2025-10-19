class item:
    pay_rate = 0.8
    def __init__(self, name:str, price:float, quantity=0):
        #this is for validation
        assert price >=0, f"{price} is not greater or equal to zero"
        assert quantity>=0, f"{quantity} is not greater or equal to zero"
        
        #over here we are assigning self to the object
        self.name = name 
        self.price = price
        self.quantity = quantity
        
    def cal_total_price(self):
        return self.price * self.quantity
    
    def discount(self):
        self.price *=self.pay_rate # its a good idea to access the pay rate from the instance level so when u want to add a specific dicount to an item it will be easy 
         
 
#creating new instances of the class

item1=item("laptop",1000,2)
item2=item("phone", 500, 1)

print(item1.cal_total_price())
item1.pay_rate = 0.3
item1.discount()
print(item1.price)
print("")

print(item2.cal_total_price())
item2.discount()
print(item2.price)
        
        