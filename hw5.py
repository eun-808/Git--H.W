# 사용자 정의 함수
def read_single_digit(a):
    b = int(a)
    if b == 0 : return '영'
    if b == 1 : return '일'
    if b == 2 : return '이'
    if b == 3 : return '삼'
    if b == 4 : return '사'
    if b == 5 : return '오'
    if b == 6 : return '육'
    if b == 7 : return '칠'
    if b == 8 : return '팔'
    if b == 9 : return '구'
def read_number(aa):
    hunds = int(num[0])
    res1 = read_single_digit(hunds)
    tens = int(num[1])
    res2 = read_single_digit(tens)
    ones = int(num[2])
    res3 = read_single_digit(ones)
    return res1+res2+res3

# 주 프로그램부
num = (input('세 자리 정수 입력: '))
if 0 <= int(num) <= 9 :
    res = read_single_digit(num)
    print(res)
elif 10 <= int(num) <= 99 :
    tens = int(num[0])
    res1 = read_single_digit(tens)
    ones = int(num[1])
    res2 = read_single_digit(ones)
    print(res1+res2)
elif 100 <= int(num) <= 999 :
    print(read_number(num))
else:
    print('세 자리 이하의 정수를 입력하세요.')