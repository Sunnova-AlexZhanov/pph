import http.client
import json
import requests


# http://www.alphavantage.co:80/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&apikey=5Z9B3PIEBAC3A433
def web_call():
    url = "www.alphavantage.co"
    conn = http.client.HTTPSConnection(url, 443)
    par = "/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&apikey=5Z9B3PIEBAC3A433"
    conn.request("GET", par)
    response = conn.getresponse().read().decode('utf-8')
    jn = json.loads(response)
    conn.close()

    ts = jn['Time Series (1min)']
    key = list(ts.keys())[0]
    open_price = ts[key]['1. open']
    print("[web_call]Opening value is: " + open_price)


def anwc():
    req = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&apikey=5Z9B3PIEBAC3A433')
    result = req.json()

    ts = result['Time Series (1min)']
    key = list(ts.keys())[0]
    open_price = ts[key]['1. open']
    print("[anwc]Opening value is: " + open_price)



if __name__ == "__main__":
    web_call()
    anwc()