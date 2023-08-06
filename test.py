
# def test(ids):
#     if ids == 10:
#         return False, ids

#     id_num = ids + 1
#     return True, id_num


# bools = True
# arrays = ['a', 'b', 'c', 'd']

# for array in arrays:
#     print(array)
#     ids = 0
#     while bools:
#         bools, ids = test(ids)
#         print(bools)
#         print(ids)

############################################################
# json = {}

# json['primero'] = {}

# array = json['primero']['segundo'] = []

# array.append(1)
# array.append(2)
# array.append(3)

# # print(array)
# print(json)

############################################################

import json
import random
with open('data/products.txt', 'r', encoding='utf-8') as file:
    products_txt = file.readlines()

with open('data/category_products.txt', 'r', encoding='utf-8') as file:
    category_products = file.readlines()

index = 0
products_id = 0
arary = []
for category in category_products:
    while products_txt[index] != ' \n' and index < 54982:
        if products_txt[index] == ' \n':
            index += 1

        products_id += 1
        arary.append({
            "productId": products_id,
            "category": category.replace('\n', ''),
            "product": products_txt[index].replace('\n', ''),
            "alt": products_txt[index+1].replace('\n', ''),
            "price": int(products_txt[index+2].replace('Gs   ', '').replace('.', '').replace('\n', '')),
            "stock": random.randint(40, 150),
            "img": "https://images.vexels.com/media/users/3/131854/isolated/preview/d939c27b70134fa62d08031cca214c29-preguntas-signo-by-vexels.png"
        })
        index += 3
        if index > 54980:
            break

    if index > 54980:
        break
    index += 1


with open("prueba.json", "w", encoding="utf-8") as file:
    json.dump(arary, file, ensure_ascii=False, indent=2)
