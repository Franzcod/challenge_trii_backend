

from ast import Try
import requests
from controllers import buyStock,sortStocks, buyFor

if __name__ == '__main__':
    
    stocks = ['AAPL','GOOGL','AMZN','TSLA','FB','TWTR','UBER','LYFT','SNAP','SHOP']
    
    listPrices = []
    
    
    for stock in stocks:
        url = f'https://financialmodelingprep.com/api/v3/quote-short/{stock}?apikey=62524f9a45adfcbd67b6c6f1105ee7f3'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            # print(data[0])
            listPrices.append(data[0])
        
    
    buyAllStock = buyStock(listPrices)
    
    orden = sortStocks(listPrices)
    
    print("\033[1;33m"+"")
    print("Ejercicio 1 - A")
    print("1-A => El usuario necesita {buyAllStock} para comprar todos los stocks".format(buyAllStock=buyAllStock))  
    
    print("")
    print("\033[;36m"+"------------------------------") 
    
    
    print("Ejercicio 1 - B")
    
    monto = input("Ingrese un monto de dinero para comprar todos los stocks: ")
    
    for stock in listPrices:
        mount = float(monto)
        buystockFor = buyFor(mount, stock)
        
        print('1-B => Con $ {mount} el usuario puede comprar {buystockFor} {stock}. Resto = ${rest} '.format(mount=mount,buystockFor=buystockFor[0], stock=stock['symbol'], rest=buystockFor[1]))
    
    
  
    

    
    
    