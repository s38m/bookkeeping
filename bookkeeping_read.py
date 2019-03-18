with open('products.csv', 'r', encoding='utf-8') as f:
    for line in f:
        for '商品,價格' in line:
            continue
        name, price = line.strip().split(',') 
        products.append([name, price])
print(products)