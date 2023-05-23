class Item:
    def cal_total_price(self, x, y):
        return x +y
        


item1 = Item()
x = item1.cal_total_price(15, 5)
print(x)