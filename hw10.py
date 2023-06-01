# 사용자 정의 함수부
import os
import pickle
def input_scores():
    s = []
    i = 1
    while (True) :
        n = int (input (f'#{i}? '))
        if n < 0: 
            break
        s.append(n)
        i += 1 
    return s
def get_average(s):
    total = 0
    for n in s:
        total += n
    return total/len(s)

def show_scores(s): # 리스트 s의 각 요소를 순회하면서 각 요소 n을 출력
    for n in s:
        print (n, end=' ') 
    print ()
# 추가 함수
def save_scores(s, filename):
    with open(filename, 'wb') as file:
        pickle.dump(s, file)

def load_scores(filename):
    if os.path.exists(filename):
        with open(filename, 'rb') as file:
            s = pickle.load(file)
            return s
    
# 주 프로그램부
filepath = 'score.bin' 
if os.path.exists(filepath):
    f = open(filepath, 'r')
    cnt = ['개인점수: ', '평균: ']
    while True:
        str1 = filepath.readline()
        if str1 == '' :
            break
        else:
            for i in cnt :
                print(f'{cnt}{str1}')
else :
    print('[점수 입력]')
    scores = input_scores()
    print('\n[점수 출력]')
    print('개인점수: ', end='')
    ones_score = show_scores(scores)
    avg = get_average(scores)
    print(f'평균: {avg:.1f}')
    save_scores(ones_score, filepath)
    save_scores(avg, filepath)