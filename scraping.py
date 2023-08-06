import os
import requests
from bs4 import BeautifulSoup

# product-title-link
# productPrice
# picture-link ?pageindex=2
# url-pages: 'https://www.stock.com.py/default.aspx?pageindex=1'

directory_path_img = 'images/'


def get_products(url, id_num):
    response = requests.get(url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')

        titles = soup.find_all('a', class_='product-title-link')

        prices = soup.find_all('span', class_='productPrice')

        a_images = soup.find_all('a', class_='picture-link')

        if titles == [] or len(titles) == 1:
            with open('data/products.txt', 'a', encoding='utf-8') as file:
                file.write(' \n')
            return False, id_num

        for title, price, a_image in zip(titles, prices, a_images):
            title.text
            price.text

            images = a_image.find_all('img')

            for image in images:

                image_url = image.get('src')
                image_alt = image.get('alt')
                with open('data/products.txt', 'a', encoding='utf-8') as file:
                    if image_alt is None:
                        image_alt = 'None'

                    file.write(title.text + '\n')
                    file.write(image_alt + '\n')
                    file.write(price.text + '\n')

                print(title.text)
                print(image_alt)
                print(price.text)

                if image_url:
                    image_response = requests.get(image_url)
                    id_num += 1
                    if image_response.status_code == 200:
                        image_path = os.path.join(
                            directory_path_img, f"ProductoId - {id_num}.jpg")
                        with open(image_path, 'wb') as file:
                            file.write(image_response.content)
                    else:
                        print(
                            f"Error al descargar la imagen {id_num}. Código de estado: {image_response.status_code}")

        return True, id_num

    else:
        print(
            f"Error al obtener la página. Código de estado: {response.status_code}")
        with open('data/products.txt', 'a', encoding='utf-8') as file:
            file.write(' \n')
        return False, id_num


extent_url_pages = '?pageindex='
space = ' \n'

with open('data/URL_products.txt', 'r', encoding='utf-8') as file:
    URL_products = file.readlines()

id_num = 0
for url in URL_products:
    count = 0
    pages = True
    if url == space:
        with open('data/products.txt', 'a', encoding='utf-8') as file:
            file.write(space)
    else:
        while pages:
            url_op = url.replace('\n', '')
            count += 1
            pages, id_num = get_products(
                f'{url_op}{extent_url_pages}{count}', id_num)
