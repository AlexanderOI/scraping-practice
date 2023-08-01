with open("data/type_products.txt", "r", encoding="utf-8") as file:
    type_products = file.readlines()

with open("data/category_products.txt", "r", encoding="utf-8") as file:
    category_products = file.readlines()

for type_product in type_products:
    cont = 0
    for category_product in category_products:
        if (type_product == category_product):
            category_products[cont] = " \n"
        print(cont)
        cont += 1

print(category_products)

for i in range(0, len(category_products)):
    with open("category_productv2.txt", "a", encoding="utf-8") as file:
        file.write(category_products[i])
