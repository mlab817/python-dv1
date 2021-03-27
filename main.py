from bs4 import BeautifulSoup
import requests
import pandas as pd
import deep_translator
from deep_translator import GoogleTranslator
import math
import time

translator = GoogleTranslator(source='auto', target='en')

dragons = []

baseUrl = 'https://www.dragonvillage.net/dv1/info/dragoninfo/'

def main():
    # iterate page number
    i = 29
    while i <= math.ceil(1140/12):

        # do it while there is still page
        # page status_code = 200
        # else break
        i += 1
        url = baseUrl + str(i*12)

        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        li = soup.find_all('li', { 'class': 'list_row'})

        dragons = []

        for item in li:
            dragon = dict()
            href = item.find('a', href=True)
            dragon['link'] = href['href']
            name = item.find('span', { 'class': 'info_list_name'}).text
            try:
                dragon['name'] = translator.translate(name)
            except deep_translator.exceptions.NotValidLength:
                pass
            # print(translator.translate(name))
            desc = item.find('span', { 'class': 'info_list_desc'}).text
            dragon['desc'] = translator.translate(desc)
            # print(translator.translate(desc))
            image_span = item.find('span', { 'class': 'info_list_img'})
            images = image_span.find_all('img')
            dragon_images = []
            for image in images:
                dragon_images.append(image['src'])
                # print(image['src'])
            dragon['dragon_images'] = dragon_images
            # print(dragon_images)
            # print(dragon)
            dragons.append(dragon)

        print('done page' + str(i))

        df = pd.DataFrame.from_dict(dragons)

        with open('dragons.csv', 'a') as f:
            df.to_csv(f, header=f.tell() == 0)

        time.sleep(3)

main()