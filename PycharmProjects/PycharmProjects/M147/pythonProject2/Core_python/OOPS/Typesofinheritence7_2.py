# multiple inheritance : it is process of deriving the properties from
# multiple parent class to single child class
'''
class A:
    pass
class B:
    pass
class C(A,B):
    pass
'''

class Cart:
    products = {'iphone':5,'imac':3,'iwatch':2,'ipad':4}
    prices = {'iphone':800,'imac':3000,'iwatch':2000,'ipad':4000}
    def __init__(self):
        self.item = []


    def add_item(self,name,quantity = 1):
        if name not in self.__class__.products.keys():
            raise Exception('product not available')
        elif self.__class__.products[name]>=quantity:
            self.item.append({'name': name, 'prices': self.__class__.prices[name], 'quantity': quantity})

        else:
            raise ValueError('product out of stock')
    def total_cost(self):
        self.total = sum([i['prices']*i['quantity'] for i in self.item])
        return self.total

    def remove_item(self,name):
        for i in self.item:
            if name==i['name']:
                if i['quantity']==1:
                    self.item.remove(i)
                else:
                    i['quantity']-=1

class Discount:
    def appley_discount(self,amount):
        return amount*0.9

class Tax:
    def calculate_tax(self,amount):
        return amount*0.07

class ShoppingCart(Cart,Discount,Tax):
    def get_final_amount(self):
        subtotal = self.total_cost()
        discounted_total = self.appley_discount(subtotal)
        tax_amount = self.calculate_tax(discounted_total)
        final_amount = discounted_total+tax_amount
        return final_amount

c2 = ShoppingCart()
c2.add_item('iphone',2)
c2.add_item('ipad')
print(c2.get_final_amount())

# c1 = Cart()
# c1.add_item('iphone',2)
# c1.add_item('ipad')
#
# print(c1.item)
# print(c1.total_cost())
# print(c1.remove_item('iphone'))
# print(c1.remove_item('ipad'))
# print(c1.item)
# ---------------------------------------------------------------------------
# hybrid inheritance:

class Product:
    def __init__(self,name,prices):
        self.name = name
        self.prices = prices

    def display_info(self):
        print(f'name:{self.name},prices:{self.prices}')
#1 parent 2 child---Hierarchical inheritance
class Smartphone(Product):
    def __init__(self,name,prices,brand,model):
        super().__init__(name,prices)
        self.brand = brand
        self.model = model

    def display_info(self):
        super().display_info()
        print(f'barnd:{self.brand},model:{self.model}')


class Laptop(Product):
    def __init__(self, name, prices, brand, model):
        super().__init__(name, prices)
        self.brand = brand
        self.model = model

    def display_info(self):
        super().display_info()
        print(f'barnd:{self.brand},model:{self.model}')

#creating new class by taking input from 2 parent
class PremiumProduct:
    def __init__(self,warranty_years):
        self.warranty_years = warranty_years
    def display(self):
        print(f'warranty:{self.warranty_years}')
#Hybrid- creating new class by using any of the 4 inheritence
class PremiumSamrtphone(Smartphone,PremiumProduct):
    def __init__(self,name, prices, brand, model,warranty_years):
        Smartphone.__init__(self,name, prices, brand, model)
        PremiumProduct.__init__(self,warranty_years)

    def display_info(self):
        Smartphone.display_info(self)
        PremiumProduct.display(self)

Premium = PremiumSamrtphone('iphone',8000,'Apple','iphone13 pro max',2)
Premium.display_info()
#check this
class Premiumlaptop(Laptop,PremiumProduct):
    def __init__(self,name, prices, brand, model,warranty_years):
        Smartphone.__init__(self,name, prices, brand, model)
        PremiumProduct.__init__(self,warranty_years)

    def display_info(self):
        Smartphone.display_info(self)
        PremiumProduct.display(self)
Premium = Premiumlaptop('Inspiron 15',60000,'Dell','Inspiron 15 3000',2)
Premium.display_info()