import json
import random


with open('data/type_products.txt', 'r', encoding='utf-8') as file:
    type_products = file.readlines()

with open('data/category_products.txt', 'r', encoding='utf-8') as file:
    category_products = file.readlines()


type_len = len(type_products)
category_len = len(category_products)

products = ''

count = 0

for type_product in type_products:
    type_product = ' "' + type_product.replace("\n", "") + '" |'
    products += type_product

print(products)
