import json

with open("data/section_products.txt", "r", encoding="utf-8") as file:
    section_products = file.readlines()

with open("data/type_products.txt", "r", encoding="utf-8") as file:
    type_products = file.readlines()

type_len = len(type_products)

products = {}

count = 0
for section_product in section_products:
    section_product = section_product.replace("\n", "")
    products[section_product] = {}
    while count < type_len:
        if type_products[count] == ' \n':
            count += 1
            break

        type_product = type_products[count].replace("\n", "")
        products[section_product][type_product] = []
        count += 1

with open("products.json", "w", encoding="utf-8") as file:
    json.dump(products, file, ensure_ascii=False, indent=2)
