

# noinspection PyUnusedLocal
# skus = unicode string
productA = Item('A',50)
productB = Item('B',30)
productC = Item('C',20)
productD = Item('D',15)
productE = Item('E',40)
products = { 'A': productA, 'B': productB, 'C': productC, 'D': productD, productE]
offers = [Offer({productA: 3}, 130), Offer({productA: 5}, 200), Offer({ProductB: 2}, 45), Offer({ProductB: 1, ProductE: 2}, 80)]

def checkout(skus):
    basket = Basket()
    for letter in skus:
        try:
            basket.add_item(products[letter])
        except:
            return -1
    return basket.calculate_value


class Basket:
    def __init__(self):
        self.items={}
        self.price = 0

    def add_item(item):
        if item in self.items:
            self.items[item] = self.items[item] + 1
        else:
            self.items[item] = 1

    def remove_items(item, count):
        if self.items[item] < count:
            throw
    
    def calculate_value():
        
    def apply_offer(offer):
        
        for key,value in combindationDict:
            basket[key] = basket[key] - value
        basket.price += self.dealPrice

class Offer:
    def __init__(self, combination, dealPrice):
        self.combinationDict = combinationDict
        self.dealPrice = dealPrice

    def offer_applicable():
        for key,value in self.combinationDict.items():
            try:
                if self.items[key] < value:
                    return false
            except:
                return false
        return true

class Item:
    def __init__(self, name, standardPrice):
        self.name = name
        self.standardPrice = standardPrice

class InvalidOfferException(Excetion):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

