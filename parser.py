import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    if r.ok:
        return r.text
    print(r.status_code)


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    image = soup.find('a', class_='prettyPhotoLink')
    image_link = image['href']
    return image_link


def return_joy():
    html = get_html('http://reactor.cc/tag/%D0%AD%D1%80%D0%BE%D1%82%D0%B8%D0%BA%D0%B0')
    return get_page_data(html)
