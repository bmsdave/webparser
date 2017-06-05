import urllib3
from bs4 import BeautifulSoup

http = urllib3.PoolManager()
r = http.request('GET', 'http://ya.ru')

soup = BeautifulSoup(r.data, 'html.parser')
print(r.data)
print(soup)
print(soup.prettify())
