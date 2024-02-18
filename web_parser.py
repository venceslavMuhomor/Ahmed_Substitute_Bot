import logging
import random

import httpx

from bs4 import BeautifulSoup
from config import URL


def GetHTML():
    url = URL

    response = httpx.get(url)

    with open('test.html', 'w') as file:
        soup = BeautifulSoup(response.text.encode('utf-8'), 'html.parser')
        soup = str(soup.encode('utf-8')).split("b'")[1][0:-1]
        soup = BeautifulSoup(soup, 'html.parser').prettify()
        file.write(soup)


try:
    with open('test.html', 'r', encoding='utf-8', errors='ignore') as file:
        response = BeautifulSoup(file, 'html.parser')

except Exception as e:
    logging.error(e)
    GetHTML()

    with open('test.html', 'r', encoding='utf-8', errors='ignore') as file:
        response = BeautifulSoup(file, 'html.parser')


def WebImages():
    img_list = []

    for image in response.find_all('img', attrs={'src': True}):
        img_list.append(image['src'])

    return img_list


def RandomImage():
    return random.choice(WebImages())
