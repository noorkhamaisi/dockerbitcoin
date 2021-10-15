
from flask import Flask
import requests



  
    
  
app = Flask(__name__)

@app.route('/')
def home():
  response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
  data = response.json()
  print(data["bpi"]["USD"]["rate"])
  return (data["bpi"]["USD"]["rate"])




        
   
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)




