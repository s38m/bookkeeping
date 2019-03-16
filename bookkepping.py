#encoding = utf-8
#dictionary 字典

products = {}
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')
    products[name] = price
print(products)
