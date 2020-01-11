import requests
from bs4 import BeautifulSoup

def web_crawler(max_page):
    page = 1
    while page <= max_page:
        url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=sports&_sacat=0&_pgn=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, features="html.parser")
        for link in soup.find_all('a', {'class': 's-item__link'}):
            href = link.get('href')
            title = link.string
            get_every_data(href)
        page += 1


def get_every_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, features="html.parser")
    for item_name in soup.find_all('h1', {'class': 'it-tt1'}):
        print(item_name.string)


web_crawler(1)
