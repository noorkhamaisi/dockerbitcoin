
from flask import Flask
import requests
import time



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




        
 
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8989)




