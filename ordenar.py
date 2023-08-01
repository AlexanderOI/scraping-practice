'''
import json
import random

from typing import Dict

def get_json(path: str) -> Dict:
    with open(path, 'r') as file:
        data = json.load(file)
    return data


products = get_json("datos.json")

# Products section
section_products = input("Ingresa la seccion de productos: ")
products[section_products] = {}

# Type of products
type_products = input("Ingresa el tipo de producto: ")
list_product = products[section_products][type_products] = []

# Products category
category = input("Ingrese la categoria: ")

id = 0
with open("data/1_aceites.txt", "r") as file:
    product = file.readlines()
    
with open("data/category.txt") as file:
    catgory = file.readlines()

list_product.append(
    {
        "productId": 1,
        "category": category,
        "product": "",
        "price": 0,
        "stock": random.randint(40, 100),
        "img": "https://images.vexels.com/media/users/3/131854/isolated/preview/d939c27b70134fa62d08031cca214c29-preguntas-signo-by-vexels.png"
    }
)

with open("products.json", "w") as file:
    json.dump(products, file, indent=2)
'''

with open("data/category_products.txt", "r") as file:
    category_products = file.readlines()

print(category_products)
