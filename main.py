import requests
from urllib.parse import urlencode


def search(term):
    url = build_url(term)
    data = get_api(url)
    text = abstract(data)
    return text


def abstract(data):
    text = data['Abstract']
    if not text:
        raise ValueError('Not found.')
    return text


def get_api(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f'Response {response.status_code}')
    return response.json()


def build_url(term):
    url = 'https://api.duckduckgo.com/?'
    qs = {'q': term, 'format': 'json', 'pretty': 1}
    url += urlencode(qs)
    return url


print(search('Brasil'))
