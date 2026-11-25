class Product:
    tax_rate=0.3
    
    def __init__(self,name,price):
        if not Product.validate_price(price):
            raise ValueError("Price must be greater than zero")
        self.name=name
        self.price=price
    
    def final_price(self):  ## Instance method
        return self.price+self.price*Product.tax_rate
    
    @classmethod                                                                                                          
    def set_tax_rate(cls,rate): ## class method
        cls.tax_rate=rate
    
    @staticmethod   ## static method 
    def validate_price(price):
        return price>0
    
    
laptop=Product("Laptop",234.0)
print(laptop.final_price())

Product.set_tax_rate(5.0)
print(laptop.final_price())

try:
    Product("Brkoen",-19)
except ValueError as e:
    print(e)
    

    