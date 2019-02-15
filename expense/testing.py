import requests
import json
def convertCurrency(amount, fromCurrency, toCurrency):
    apiKey = '4ed858fd053071297e9d'
    fromCurrency = fromCurrency
    toCurrency = toCurrency
    query = fromCurrency + "_" + toCurrency
    url = 'https://free.currencyconverterapi.com/api/v6/convert?q=' + query + '&compact=ultra&apiKey=' +apiKey
    print(url)
    response = requests.get(url) 
    json_response = response.json()
    print(query)
    return json_response[query]

print(convertCurrency(10, 'EUR', 'GBP'))
