class Item:
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
    
    def __repr__(self):
        return f"Item of toString func: ('{self.name}', '{self.price}', '{self.quantity}')"
    
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)


print(Item.all)