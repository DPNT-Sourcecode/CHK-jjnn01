# noinspection PyUnusedLocal
# skus = unicode string

class InvalidOfferException(Exception):
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
    competing_offers = [
        [Offer({productB: 2}, 45), Offer({productB: 1, productE: 2}, 80)],
        [Offer({productQ: 3}, 80), Offer({productR: 3, productQ:1}, 150)]
        ]
    non_competing_offers = [
        Offer({productA: 5}, 200, Offer({productA: 3}, 130)),
        Offer({productH: 10}, 80, Offer({productH: 5}, 45)),
        Offer({productV: 3}, 130, Offer({productV: 2}, 90)),
        Offer({productF: 3}, 20),
        Offer({productK: 2}, 120),
        Offer({productU: 4}, 120),
        Offer({productN: 3, productM:1}, 120),
        Offer({productP: 5}, 200)
        ]
    group_offers = [GroupOffer([productZ, productS, productT, productY, productX], 3, 45)]
    
    basket = Basket(competing_offers, non_competing_offers, group_offers, {}, 0)
    for letter in skus:
        try:
            basket.add_item(products[letter])
        except Exception as e:
            return -1
    return basket.calculate_value()

class GroupOffer:
    def __init__(self, elements, required_number, price):
        self.elements = elements.copy()
        self.elements.sort(key= lambda l: l.price, reverse=True)
        self.required_number = required_number
        self.price = price

    def apply_offer(self, basket):
        value_ranked_collection = [(x,basket.items[x]) for x in self.elements]
        if (sum(value_ranked_collection[1]) < self.required_number):
            raise InvalidOfferException("Invalid Offer")
        still_required = self.required_number
        for item in value_ranked_collection:
            if item[1] == 0:
                continue
            if item[1] < still_required:
                still_required -= item[1]
                basket.remove_items(item[0], time[1])
            else:
                basket.remove_items(item[0], still_required)
        basket.add_item_price(self.price)
        return basket

class Offer:
    def __init__(self, combinationDict, dealPrice, dominated_offer=None):
        self.combinationDict = combinationDict
        self.dealPrice = dealPrice
        self.dominated_offer = dominated_offer

    def apply_offer(self, basket):
        for key, value in self.combinationDict.items():
            if value > basket.items[key]:
                raise InvalidOfferException("Invalid Offer")
        for key,value in self.combinationDict.items():
            basket.remove_items(key, value)
        basket.add_item_price(self.dealPrice)
        return basket

class Item:
    def __init__(self, name, standardPrice):
        self.name = name
        self.standardPrice = standardPrice

class Basket:
    def __init__(self, competing_offers, non_competing_offers, group_offers, items, price):
        self.non_competing_offers = non_competing_offers.copy()
        self.competing_offers = competing_offers.copy()
        self.items = items.copy()
        self.price = price
        self.group_offer = group_offer.copy()

    def add_item(self, item):
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def remove_items(self, item, count):
        self.items[item] = self.items[item] - count

    def add_item_price(self, price):
        self.price += price
    
    def calculate_value(self):
        if self.non_competing_offers:
            self.apply_non_competing_offers()
        if self.group_offer:
            self.apply_group_offer()
        if self.competing_offers:
            competing_offer = self.competing_offers[0]
            return min(self.apply_competing_offer(competing_offer[0], competing_offer[1], competing_offer),
                       self.apply_competing_offer(competing_offer[1], competing_offer[0], competing_offer))
        for item, count in self.items.items():
            self.price += item.standardPrice * count
        return self.price

    def apply_non_competing_offers(self):
        for offer in self.non_competing_offers:
            while True:
                try:
                    self = offer.apply_offer(self)
                except:
                    try:
                        self = offer.dominated_offer.apply_offer(self)
                    except:
                         break
                    break

    def apply_group_offers(self):
        for offer in self.group_offers:
            while True:
                try:
                    self = offer.apply_group_offer(self)
                except:
                    break
        
    def apply_competing_offer(self, offer, alternative, competing_offer):
        basket = Basket(self.competing_offers,[],[],self.items, self.price)
        try:
            basket = offer.apply_offer(basket)        
        except:
            basket.competing_offers.remove(competing_offer)
            basket.non_competing_offers.append(alternative)
        return basket.calculate_value()
            


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
productK = Item('K',70)
productL = Item('L',90)
productM = Item('M',15)
productN = Item('N',40)
productO = Item('O',10)
productP = Item('P',50)
productQ = Item('Q',30)
productR = Item('R',50)
productS = Item('S',20)
productT = Item('T',20)
productU = Item('U',40)
productV = Item('V',50)
productW = Item('W',20)
productX = Item('X',17)
productY = Item('Y',20)
productZ = Item('Z',21)


