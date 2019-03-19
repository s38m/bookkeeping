import os
products = []
'''
if os.path.isfile('products.csv'):
    print('File exist')
'''    
#讀取檔案
    with open('products.csv', 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',') 
            products.append([name, price])
else:
    print('File not found')

print(products)