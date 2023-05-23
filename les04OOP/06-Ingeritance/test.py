class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name:str, price:float, quantity=0):
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"
        
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)
        
    def cal_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
    def __repr__(self):
        return f"Item of toString func: ('{self.name}', '{self.price}', '{self.quantity}')"
    

class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        super().__init__(name, price, quantity) 
        
        # Run validations to the received arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater or equal to zero!"
        
        #Asign obj
        self.broken_phones = broken_phones
    
phone1 = Phone("jscPhonev10", 500, 5, 1)

print(Phone.all)