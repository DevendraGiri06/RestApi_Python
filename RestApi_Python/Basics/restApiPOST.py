import requests
payload = dict(key1='value1', key2='value2')
r = requests.post('https://httpbin.org/post', data=payload)
# print(r.text)

# check code status 
print(r.status_code)