shopping_bag = {}
def add_product(dict_name, product_name, product_q):
    dict_name[product_name] = product_q
print('[ 구입 ]')
while True :
    item_name = input('상품명? ')
    if item_name == '' :
        break 
    else:
        item_count = int(input('수량은? '))
        add_product(shopping_bag,item_name, item_count)
        print(f'장바구니에 {item_name} {item_count}개가 담겼습니다.')

print(f'>>> 장바구니 보기: {shopping_bag}')

while True :
    print('[ 검색 ]')
    to_find = input('장바구니에서 확인하고자 하는 상품은? ')
    if to_find == '' :
        break
    res = shopping_bag.get(to_find)
    print(f'{to_find}은(는) {res}개 담겨 있습니다.')
    
print('프로그램 종료')