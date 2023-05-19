shopping_bag = {}

def buy(shopping_ba):
    item_name = input('상품명? ')
    if item_name == '':
        return False

    else :
        item_count = int(input('수량은? '))
        shopping_bag[item_name] = item_count
        print(f'장바구니에 {item_name} {item_count}개가 담겼습니다.')

        return True

def show(shopping_b):
    print(f'>>> 장바구니 보기: {shopping_bag}')

def find(shopping):
    to_find = input('장바구니에서 확인하고자 하는 상품은? ')
    res = shopping_bag.get(to_find)
    if res is not None:
        print(f'{to_find}은(는) {res}개 담겨 있습니다.')
    elif to_find.strip() == '' :
        return False
    
    else :
        print(f'{to_find}은(는) 장바구니에 없습니다.')
        
    

print('[ 구입 ]')
while True:
    if buy(shopping_bag) == False:
        break
    
show(shopping_bag)

while True:
    print('[ 검색 ]')
    if find(shopping_bag) == False :
       break

print('구입 종료')


