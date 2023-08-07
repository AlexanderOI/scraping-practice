import os
import requests
from bs4 import BeautifulSoup

# product-title-link
# productPrice
# picture-link ?pageindex=2
# url-pages: 'https://www.stock.com.py/default.aspx?pageindex=1'

directory_path_img = 'images/'


def get_products(url):
    response = requests.get(url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')

        titles = soup.find_all('a', class_='product-title-link')

        prices = soup.find_all('span', class_='productPrice')

        if titles == [] or len(titles) == 1:
            with open('data/products.txt', 'a', encoding='utf-8') as file:
                file.write(' \n')
            return

        for title, price in zip(titles, prices):

            with open('data/first_product.txt', 'a', encoding='utf-8') as file:

                file.write(title.text + '\n')

            print(title.text)

            break

        return

    else:
        print(
            f"Error al obtener la página. Código de estado: {response.status_code}")
        with open('data/products.txt', 'a', encoding='utf-8') as file:
            file.write(' \n')
        return


space = '\n'

with open('data/URL_products.txt', 'r', encoding='utf-8') as file:
    URL_products = file.readlines()

for url in URL_products:
    if url == space:
        with open('data/first_product.txt', 'a', encoding='utf-8') as file:
            file.write(space)
    else:
        url_op = url.replace('\n', '')
        get_products(f'{url_op}')
