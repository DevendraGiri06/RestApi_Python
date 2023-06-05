import requests

def get_news(country, api_key='ba51b77e3dd443e18a3836600c6b8ecd'):
  url =f'https://newsapi.org/v2/top-headlines?country={country}&category=business&apiKey={api_key}'
  r = requests.get(url)
  content = r.json()
  articles = content['articles']
  results = []
  for article in articles:
    results.append(f"TITLE\n'{article['title']}, '\nDESCRIPTION\n', {article['description']}")
  return results

print(get_news(country='in'))