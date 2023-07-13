import requests

url = "https://www.baidu.com"

r = requests.get(url)
print(r.status_code)  # 返回值为200，表示请求成功
print(r.headers)
print(r.encoding)
print(r.text)
print(r.cookies)

r.encoding = 'utf-8'
print(r.text)