import requests
# Requests is an HTTP library, written in Python, for human beings. Basic GET usage:
r=requests.get('https://newsapi.org/v2/everything?q=apple&from=2023-05-12&to=2023-06-1&sortBy=popularity&apiKey=ba51b77e3dd443e18a3836600c6b8ecd')

content =r.json()
print(type(content))
# print(content)
# print(content['articles'])
# print(content)
print(content['articles'][0]['title'])

