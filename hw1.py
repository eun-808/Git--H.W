def get_radius(prompt):
    r = int(input(prompt)) 
    return r
def get_circle_area():
    area = result * result * 3.14
    return area
print('넓이를 구하고자 하는 원의 반지름은? ', end = '')
result = get_radius('')
print('반지름',result,'인 원의 넓이 = 3.14 x', result ,'x', result ,'=', get_circle_area())