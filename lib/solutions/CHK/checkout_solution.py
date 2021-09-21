

# noinspection PyUnusedLocal
# skus = unicode string

class InvalidOperationException(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

def checkout(skus):
    basket = Basket()
    for letter in skus:
        try:
            basket.add_item(products[letter])
        except:
            return -1
    return basket.calculate_value

class Offer:
    def __init__(self, combinationDict, dealPrice):
        self.combinationDict = combinationDict
        self.dealPrice = dealPrice

    def apply_offer(basket):
        for key,value in offer.combindationDict.Items():
            basket.remove_items(key, value)
        basket.add_item_price(offer.dealPrice)

class Item:
    def __init__(self, name, standardPrice):
        self.name = name
        self.standardPrice = standardPrice

class Basket:
    def __init__(self):
        self.viable_offers = offers
        self.items= {}
        self.price = 0

    def __init__(self, viable_offers, items, price):
        self.viable_offers = viable_offers
        self.items = items
        self.price = price

    def add_item(item):
        if item in self.items:
            self.items[item] = self.items[item] + 1
        else:
            self.items[item] = 1

    def remove_items(item, count):
        if self.items[item] < count:
            raise InvalidOperationException("Too few items to remove")
        self.items[item] = self.items[item] - count

    def add_item_price(price):
        self.price = self.price + price
    
    def calculate_value():
        new_potential_baskets = apply_offers()
        if new_potential_baskets:
            return min(new_potential_baskets, lambda x: x.calculate_value)
        for item, count in self.items.Items():
            self.price += item.standardPrice * count
        return self.price

    def apply_offers():
        unviable_offers = []
        new_potential_baskets = [] 
        for offer in self.viable_offers:
            try:
                basket = Basket(self.viable_offers, self.items, self.price)
                offer.apply_offer(basket)
                new_potential_baskets.add(basket)
            except:
                unviable_offers = offer
        for unviable_offer in unviable_offers:
            self.viable_offers.remove(unviable_offer)
        for basket in new_potential_baskets:
            basket.viableOffers = self.viable_offers
        return new_potential_baskets


productA = Item('A',50)
productB = Item('B',30)
productC = Item('C',20)
productD = Item('D',15)
productE = Item('E',40)
products = { 'A': productA, 'B': productB, 'C': productC, 'D': productD, 'E': productE}
offers = [Offer({productA: 3}, 130), Offer({productA: 5}, 200), Offer({ProductB: 2}, 45), Offer({ProductB: 1, ProductE: 2}, 80)]


