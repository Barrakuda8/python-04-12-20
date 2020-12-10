# версия, в которой подзадания выполняются одновременно (более оптимальная)

all_products = []
analytics = {"название": [], "цена": [], "количество": [], "единица измерения": []}

while True:
    products_count = input("Введите количество наименований: ")
    # можно было бы через "стоп-слово" определять количество, но мне кажется, что так красивее
    if products_count.isdigit():
        products_count = int(products_count)
        break

for i in range(products_count):
    product_characteristics = {"название": None, "цена": None, "количество": None, "единица измерения": None}
    for characteristic in product_characteristics:
        product_characteristics[characteristic] = input(f"{characteristic} для товара №{i + 1}: ")
        if characteristic.isdigit():
            characteristic = int(characteristic)
        analytic_characteristic = analytics[characteristic]
        if product_characteristics[characteristic] not in analytic_characteristic:
            analytic_characteristic.append(product_characteristics[characteristic])
    product = (i + 1, product_characteristics)
    all_products.append(product)

print(all_products)
print(analytics)

