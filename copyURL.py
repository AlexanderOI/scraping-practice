from bs4 import BeautifulSoup
import requests

url = 'https://www.stock.com.py/default.aspx/'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    url_products = soup.find_all('a', class_='collapsed')

    print(url_products)
    for url_product in url_products:
        products_text = url_product.text
        href_url_products = url_product.get('href')

        if href_url_products:
            with open('data/products_name.txt', 'a', encoding='utf-8') as file:
                file.write(products_text + '\n')
        else:
            with open('data/products_name.txt', 'a', encoding='utf-8') as file:
                file.write(' \n')
