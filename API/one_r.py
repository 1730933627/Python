import requests
import json

# url = "http://127.0.0.1:8856/bl-api?vinfo=BV1jD4y1m7HU"
# url = "http://127.0.0.1:8856/bl-api?uid=22516494"
# url = "http://127.0.0.1:8856/bl-api?relation=22516494"
url = "http://yanlinn.com:8856/bl-api?relation=22516494"
# url = "http://127.0.0.1:8856/bl-api"
# url = "http://localhost:8856/bl-api?dynamic=407623788310130382"

res = requests.post(url)
res.encoding = 'utf-8'
html = res.text
# data = json.loads(html)
print(html)
