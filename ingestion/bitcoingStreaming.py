import requests
import logging
import time
import yaml
import datetime
from urllib.parse import urlencode

import apiHelper
import config

BITCOIN_API_URL = "https://api.coindesk.com/v1/bpi/currentprice.json"
CURRENCY_API_URL = "https://api.fixer.io/latest?base=USD"
#For new token https://goldprice.com/


def main():

    response = apiHelper.GetAPIResponse(getMetalURI())
    


def getMetalURI(metal="Gold", interval="1", days="1"):
    
    baseURI = "https://service.nfusionsolutions.biz/api/Metals/IntradaySpots?"

    params = {
        "token": config.GOLD_API_TOKEN,
        "metals": metal,
        "currency": "USD",
        "indicators": "%5B%5D",
        "interval": interval,
        "days": days
    }

    return baseURI + urlencode(params)

def createMetalJSON(response):
    curr = response[0]['data']['intervals'][-1]

    {'start': curr['start'][6:-7], 'low': 1321.505, 'end': curr['end'][6:-7],
     'high': 1321.505, 'open': 1321.505, 'last': 1321.505}
    
    #Printing timestamp in human readable format
    #datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    
    return {'start': curr['start'][6:-7], 'low': 1321.505, 'end': curr['end'][6:-7],
            'high': 1321.505, 'open': 1321.505, 'last': 1321.505}

def createCurrencyJSON(response):
    return {}

def createBitcoinJSON(response):
    return {
        "code": response["bpi"]["USD"]["code"],
        "time": response["time"]["updatedISO"],
        "currRate": response["bpi"]["USD"]["rate_float"],
        "currRateString": response["bpi"]["USD"]["rate"]
    }



if __name__ == '__main__':
   
   main()
    

