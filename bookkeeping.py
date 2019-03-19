#encoding = utf-8
#two dimentional list 二維清單

import os

def read_file(filename, products):#讀取檔案
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '商品名稱,商品價格' in line:
                continue
            name, price = line.strip().split(',') 
            products.append([name, price])   
    return products

def user_input(products):#讓使用者輸入
    while True:
        name = input('請輸入商品名稱: ')
        if name == 'q':
            break
        price = input('請輸入商品價格: ')
        products.append([name, price])
    print(products)
    return products

def print_product(products):#印出所有購買記錄
    for p in products:
        print(p[0], '的價格是', p[1])

def write_file(filename, products):#寫入印出所有購買記錄
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('商品名稱,商品價格\n')
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n')

def main():
    products = []
    filename = input('請輸入檔案名稱: ')
    if os.path.isfile(filename):
        print('已找到檔案')
        products = read_file(filename, products)
    else:
        print('對應檔案不存在')
    
    products = user_input(products)
    print_product(products)
    write_file(filename, products)

main()