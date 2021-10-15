# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 11:23:43 2021

@author: get-a
"""


import requests
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data = response.json()
print(data["bpi"]["USD"]["rate"])

