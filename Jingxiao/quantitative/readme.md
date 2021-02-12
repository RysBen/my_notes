# 网络编程
## REST
> REST: 通过 URL 定位资源，通过 GET, POST, PUT, DELETE 等动作操作资源。

## TCP/IP



- 例1. 用 GET 获取行情信息
```python
import json
import requests

ticker = 'https://api.gemini.com/v1/pubticker/{}'
symbol = 'btcusd'
btc = requests.get(ticker.format(symbol)).json()

print(json.dumps(btc,indent=4))
```

- 例2. 用 POST 进行交易
```python
import requests

gemini = 'https://api.sandbox.gemini.com'
endpoint = '/v1/order/new'
url = gemini + endpoint

。。。

request_headers={'Content-Type': "text/plain",
                 'Content-Length': "0",
                 'X-GEMINI-APIKEY': gemini_api_key,
                 'X-GEMINI-PAYLOAD': b64,
                 'X-GEMINI-SIGNATURE': signature,
                 'Cache-Control': "no-cache"
                  }

response = requests.post(url, data=None, headers = request_headers)
```
