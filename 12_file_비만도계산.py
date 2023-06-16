'''
학과 : 컴퓨터공학부
학번 : 202395025
이름 : 이준서

키와 몸무게로 비만도 계산하기
'''
with open('info.txt','r') as f:
    for line in f :                   #strip() : 공백제거, split(',') 쉼표를 구분자로 사용
        (name, weight, height) = line.strip().split(',')
        
        if (not name) or (not weight) or (not height):
            continue
        # 비만도 계산하기 
        bmi = int(weight) / (int(height) / 100) ** 2
        if bmi >= 25:
            result = '과체중'
        elif bmi >= 18.5:
            result = '정상체중'
        else :
            result = '저체중'
            
        print('\n'.join(['이름 : {}', '몸무게 : {}', '키 : {}', 'bmi : {:.2f}', '결과 : {}']).format(name, weight, height, bmi, result))
        