class Item:
    def __init__(self, name:str, price:float, quantity=0):
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"
        
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def cal_total_price(self):
        return self.price * self.quantity
    
item1 = Item('Phone', 500,2)
item2 = Item('Laptop', 1500, 1)

print(item1.cal_total_price())
print(item2.cal_total_price())