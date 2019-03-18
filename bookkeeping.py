#encoding = utf-8
#two dimentional list 二維清單

products = []
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')
    products.append([name, price])
print(products)

for p in products:
    print(p[0], '的價格是', p[1])

with open('products.csv', 'w', encoding='utf-8') as f:
    f.write('商品名稱,商品價格\n')
    for p in products:
<<<<<<< HEAD
        f.write(p[0] + ',' + p[1] + '\n')
=======
        f.write(p[0] + ',' + p[1] + '\n')
>>>>>>> 35bdff83ce85ca78f270dc7acfd9ed9856410f83
