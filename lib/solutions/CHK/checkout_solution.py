

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    dict = {'A': 0, 'B':0, 'C':0, 'D':0}
    for letter in skus:
        try:
            dict[letter.upper()] = dict[letter.upper()] + 1
        except:
            return -1
    return getValue('A', dict['A']) + getValue('B', dict['B']) + getValue('C', dict['C']) + getValue('D', dict['D'])

def getValue(letter, number):
    
    if letter == 'A':
        return (number % 3) * 130 + (number/3) * 50
    elif letter == 'B':
        return (number % 2) * 45 + (number/2) * 30
    elif letter ==  'C':
        return number * 20
    elif letter == 'D':
        return number * 15


