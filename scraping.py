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

        id_num += 1
        for title, price, a_image in zip(titles, prices, a_images):
            print(title.text)
            print(price.text)

            images = a_image.find_all('img')

            for image in images:
                image_url = image.get('src')
                image_alt = image.get('alt')
                print(image_alt)

                if image_url:
                    image_response = requests.get(image_url)

                    if image_response.status_code == 200:
                        image_path = os.path.join(
                            directory_path_img, f"ProductoId - {id_num}.jpg")
                        with open(image_path, 'wb') as file:
                            file.write(image_response.content)
                    else:
                        print(
                            f"Error al descargar la imagen {id_num}. Código de estado: {image_response.status_code}")

        return True

    else:
        print(
            f"Error al obtener la página. Código de estado: {response.status_code}")
        return False


extent_url_pages = '?pageindex='
space = " \n"

with open('data/URL_products.txt', 'r', encoding='uft-8') as file:
    URL_products = file.readlines()

pages = True
id_num = 0
for url in URL_products:
    count = 0
    if url == space:
        while pages:
            pages = get_products(f'{url}{extent_url_pages}{count}', id_num)
