

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    dict = {'A': 0, 'B':0, 'C':0, 'D':0}
    for letter in skus:
        try:
            dict[letter.upper()] = dict[letter.upper()] + 1
        except:
            return -1

def getValue(letter, number):
    #This is ugly. Should be a class. 
    switch letter:
        case 'A':
            return (number % 3) * 130 + (number/3) * 50
        case 'B':
            return (number % 2) * 45 + (number/2) * 30
        case 'C':
            return number * 20
        case 'D':
            return number * 15

class Item:
    name

