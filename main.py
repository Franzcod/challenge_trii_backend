

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
    
    
    
    
    print("1-A => El usuario necesita {buyAllStock} para comprar todos los stocks".format(buyAllStock=buyAllStock))  
    
    for stock in listPrices:
        buystockFor = buyFor(3000000, stock) 
        print('2-B => Con 3000.000 pesos el usuario puede comprar {buystockFor} {stock}'.format(buystockFor=buystockFor, stock=stock['symbol']))
    
    
    

    
    
    