import json
import random

with open('data/section_products.txt', 'r', encoding='utf-8') as file:
    section_products = file.readlines()

with open('data/type_products.txt', 'r', encoding='utf-8') as file:
    type_products = file.readlines()

with open('data/category_products.txt', 'r', encoding='utf-8') as file:
    category_products = file.readlines()

with open('data/products.txt', 'r', encoding='utf-8') as file:
    products_txt = file.readlines()

type_len = len(type_products)
category_len = len(category_products)
products_len = len(products_txt)

products = {}

count_type = 0

for section_product in section_products:
    section_product = section_product.replace("\n", "")
    products[section_product] = {}
    while count_type < type_len:
        if type_products[count_type] == ' \n':
            count_type += 1
            break

        type_product = type_products[count_type].replace("\n", "")
        products[section_product][type_product] = []
        count_type += 1


count_categoty = 0
count_products = 0
products_id = 0
for section in products:
    for type_product in products[section]:
        list_products: list = products[section][type_product]
        while products_txt != ' \n':
            if products_txt[count_products] == ' \n':
                count_products += 1
                if products_txt[count_products] == ' \n':
                    count_products += 1
                    break

            products_id += 1
            list_products.append({
                "productId": products_id,
                "category": category_products[count_categoty].replace('\n', ''),
                "product": products_txt[count_products].replace('\n', ''),
                "alt": products_txt[count_products + 1].replace('\n', ''),
                "price": int(products_txt[count_products + 2].replace('Gs   ', '').replace('.', '').replace('\n', '')),
                "stock": random.randint(40, 150),
                "img": "https://images.vexels.com/media/users/3/131854/isolated/preview/d939c27b70134fa62d08031cca214c29-preguntas-signo-by-vexels.png"
            })

            count_products += 3
        count_categoty += 1


with open("json/products.json", "w", encoding="utf-8") as file:
    json.dump(products, file, ensure_ascii=False, indent=2)
