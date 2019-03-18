with open('products.csv', 'r', encoding='utf-8') as f:
    for line in f:
        name, price = line.strip().split(',') 
        products.append([name, price])
print(products)