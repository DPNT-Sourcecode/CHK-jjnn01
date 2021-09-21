# noinspection PyUnusedLocal
# skus = unicode string

class InvalidOperationException(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

def checkout(skus):
    products = {
        'A': productA, 'B': productB, 'C': productC,'D': productD,'E': productE,
        'F': productF, 'G': productG, 'H': productH,'I': productI,'J': productJ,
        'K': productK, 'L': productL, 'M': productM,'N': productN,'O': productO,
        'P': productP, 'Q': productQ, 'R': productR,'S': productS,'T': productT,
        'U': productU, 'V': productV, 'W': productW,'X': productX,'Y': productY,
        'Z': productZ}
    combo_offers = [
        Offer({productA: 3}, 130),
        Offer({productA: 5}, 200),
        Offer({productB: 2}, 45),
        Offer({productB: 1, productE: 2}, 80),
        Offer({productF: 3}, 20),
        Offer({productH: 5}, 45),
        Offer({productH: 10}, 80),
        Offer({productK: 2}, 150),
        Offer({productN: 3, productM:1}, 120),
        Offer({productP: 5}, 200),
        Offer({productQ: 3}, 80),
        Offer({productR: 3, productQ:1}, 150),
        Offer({productU: 4}, 120),
        Offer({productV: 2}, 90),
        Offer({productV: 3}, 130)
        ]
    basket = Basket(combo_offers, {}, 0)
    for letter in skus:
        try:
            basket.add_item(products[letter])
        except Exception as e:
            return -1
    return basket.calculate_value()

class Offer:
    def __init__(self, combinationDict, dealPrice):
        self.combinationDict = combinationDict
        self.dealPrice = dealPrice

    def apply_offer(self, basket):
        for key,value in self.combinationDict.items():
            basket.remove_items(key, value)
        basket.add_item_price(self.dealPrice)
        return basket

class Item:
    def __init__(self, name, standardPrice):
        self.name = name
        self.standardPrice = standardPrice

class Basket:
    def __init__(self, viable_offers, items, price):
        self.viable_offers = viable_offers.copy()
        self.items = items.copy()
        self.price = price

    def add_item(self, item):
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def remove_items(self, item, count):
        if self.items[item] < count:
            raise InvalidOperationException("Too few items to remove")
        self.items[item] = self.items[item] - count

    def add_item_price(self, price):
        self.price += price
    
    def calculate_value(self):
        new_potential_baskets = self.apply_offers()
        if new_potential_baskets:
            return min(x.calculate_value() for x in new_potential_baskets)
        for item, count in self.items.items():
            self.price += item.standardPrice * count
        return self.price

    def apply_offers(self):
        unviable_offers = []
        new_potential_baskets = []
        for offer in self.viable_offers:
            try:
                basket = Basket(self.viable_offers, self.items, self.price)
                basket = offer.apply_offer(basket)
                new_potential_baskets.append(basket)
            except:
                unviable_offers.append(offer)
        for unviable_offer in unviable_offers:
            self.viable_offers.remove(unviable_offer)
        return new_potential_baskets


productA = Item('A',50)
productB = Item('B',30)
productC = Item('C',20)
productD = Item('D',15)
productE = Item('E',40)
productF = Item('F',10)
productG = Item('G',20)
productH = Item('H',10)
productI = Item('I',35)
productJ = Item('J',60)
productK = Item('K',80)
productL = Item('L',90)
productM = Item('M',15)
productN = Item('N',40)
productO = Item('O',10)
productP = Item('P',50)
productQ = Item('Q',30)
productR = Item('R',50)
productS = Item('S',30)
productT = Item('T',20)
productU = Item('U',40)
productV = Item('V',50)
productW = Item('W',20)
productX = Item('X',90)
productY = Item('Y',10)
productZ = Item('Z',50)





