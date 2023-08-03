import os
import requests
from bs4 import BeautifulSoup


# product-title-link
# productPrice
# picture-link

url = 'https://www.stock.com.py/default.aspx/'
directory_path_img = 'images/'

response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')

    titles = soup.find_all('a', class_='product-title-link')

    prices = soup.find_all('span', class_='productPrice')

    a_images = soup.find_all('a', class_='picture-link')

    count = 0

    for title, price, a_image in zip(titles, prices, a_images):
        print(title.text)
        print(price.text)

        images = a_image.find_all('img')

        count += 1
        for image in images:
            image_url = image.get('src')
            image_alt = image.get('alt')
            print(image_alt)

            if image_url:
                image_response = requests.get(image_url)

                if image_response.status_code == 200:
                    image_path = os.path.join(
                        directory_path_img, f"ProductoId - {count}.jpg")
                    with open(image_path, 'wb') as file:
                        file.write(image_response.content)
                else:
                    print(
                        f"Error al descargar la imagen {count}. Código de estado: {image_response.status_code}")

else:
    print(
        f"Error al obtener la página. Código de estado: {response.status_code}")
