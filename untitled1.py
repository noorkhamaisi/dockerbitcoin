
from flask import Flask
import requests
import time
from datetime import datetime

def calculateavg(bitcoin_history):
    summ=0.0
    for price in bitcoin_history:
        price= price.replace(',', '')
       #print(float(price))
        summ = summ+float(price)
    return summ/10

def get_latest_bitcoin_price():
  response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
  data = response.json()
  mynum=(data["bpi"]["USD"]["rate"])
 
  return (mynum)
 

def main():
    bitcoin_history = []
    while True:
        price = get_latest_bitcoin_price()
        bitcoin_history.append(price)

       

        
        if len(bitcoin_history) == 3:
            avg = calculateavg(bitcoin_history)
            return avg

        # Sleep for 1 minutes 
       # time.sleep(1 * 60)
    
    
    
print (main())
print(get_latest_bitcoin_price())
