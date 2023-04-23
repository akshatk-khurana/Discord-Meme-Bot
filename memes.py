"""Get image results for memes of google"""

from bs4 import BeautifulSoup
from random import randint
import requests
from PIL import Image

name_of_file = 'meme.png'

categories = ['programming', 'coding', 'memes', 'duolingo']

def process_msg(message):
    msg = str(message.content)[1:]

    category = 'memes' if msg.strip() == '' else msg.lstrip()

    if category.lower() not in categories:
        return ('Whoops, meme category not supported.', None)

    category = category + '+memes' if category != 'memes' else category

    url = f'https://www.google.com/search?q={category}&source=lnms&tbm=isch'
    find_meme(url)

    return (None, name_of_file)

def find_meme(url):
    #get page HTML
    site = requests.get(url)
    html = site.text

    #initialise soup
    soup = BeautifulSoup(html, 'html.parser')

    img_divs = soup.find_all('table', class_='IkMU6e')

    r = randint(0, len(img_divs) - 1)

    src = img_divs[r].find('img')['src']

    img = requests.get(src).content

    with open(name_of_file, 'wb') as m:
        m.write(img)

    image = Image.open(name_of_file)
    image = image.resize((image.size[0]*2, image.size[1]*2))
    image.save(name_of_file)