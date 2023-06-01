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

def show_scores(s):
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
    ones_s = load_scores(filepath)
    avg_s = load_scores(filepath)
    print('[파일 읽기]\n\n[점수 출력]')
    print(f'개인점수: {ones_s}')
    print(f'평균: {avg_s}')
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
