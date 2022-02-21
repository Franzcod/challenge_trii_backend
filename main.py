

import requests
from controllers import buyStock

if __name__ == '__main__':
    
    stocks = ['AAPL','GOOGL','AMZN','TSLA','FB','TWTR','UBER','LYFT','SNAP','SHOP']
    
    listPrices = []
    
    
    for stock in stocks:
        url = f'https://financialmodelingprep.com/api/v3/quote-short/{stock}?apikey=c13a5d2ecf7cc6b8c50c06d7e1dfce22'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            listPrices.append(data[0]['price'])
    
    buyAllStock =buyStock(listPrices)
    
    print("El usuario necesita {buyAllStock} para comprar todos los stocks".format(buyAllStock=buyAllStock))   
    
    
    
    

    
    
    