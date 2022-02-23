from audioop import reverse


def buyStock(list):
    totalPrice = 0
    for item in list:
        precio = item['price']
        totalPrice += precio
    return totalPrice

def sortStocks(list):
    list.sort(key=lambda x: x['price'], reverse=True)
    return list


def buyFor(mont, stock):
    price = stock['price']
    rest = (mont%price) 
    return [int(mont/price), rest]
    