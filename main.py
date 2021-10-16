
from flask import Flask
import requests
#import time

URL = "https://min-api.cryptocompare.com/data/v2/histominute?fsym={}&tsym={}&limit={}"



def get_price(coin,currency,limit):
    sum = 0
    try:
        response = requests.get(URL.format(coin,currency,limit)).json()
        for i in range(10):
            sum += response['Data']['Data'][i]['close']
     #   data = {'price': response['Data']['Data'][9]['close'], 'average': sum/10}
        return response['Data']['Data'][9]['close'],sum/10
    except:
        return False
    
'''

def calculateavg(bitcoin_history):
    summ=0
    for price in bitcoin_history:
        price= price.replace(',', '')
        #print(float(price))
        summ = summ+float(price)
        
    return summ/10

def get_latest_bitcoin_price():
  response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
  data = response.json()
  return (data["bpi"]["USD"]["rate"])
 

def main():
    bitcoin_history = []
    while True:
        price = get_latest_bitcoin_price()
        bitcoin_history.append(price)

       

        
        if len(bitcoin_history) == 10:
            avg = calculateavg(bitcoin_history)
            return avg

        # Sleep for 1 minutes 
        time.sleep(1 * 60)
    
  
app = Flask(__name__)

@app.route('/')
def home():

  avg10=main()
  print(get_latest_bitcoin_price())
  return ("The average of the 10 minutes is: " + str(avg10) + "\nThe current Price is :"+ str(get_latest_bitcoin_price()) )

'''
app = Flask(__name__)
@app.route("/")
def hello_world():
    currentprice,avg10= get_price("BTC","USD","10")
   
    return ("The average of the 10 minutes is: " + str(avg10) + "\nThe current Price is :"+ str(currentprice) )


        
 
if __name__ == "__main__":
    app.run()




