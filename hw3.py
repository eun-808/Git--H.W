def get_fixed_price():
    global dicount_price
    global discount_rate
    full_price = int(discount_price * 100 // (100 - discount_rate))
    return full_price


discount_rate = float(input('할인율은? '))
discount_price = float(input('A 상품의 할인된 가격은? '))
result1 = get_fixed_price()
discount_price = float(input('B 상품의 할인된 가격은? '))
result2 = get_fixed_price()
print('A 상품의 정가는',result1,' 원')
print('B 상품의 정가는',result2,' 원')