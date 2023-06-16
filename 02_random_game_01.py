'''
학과 : 컴퓨터공학부
학번 : 202395025
이름 : 이준서
'''
'''
숫자 추측 게임 만들기

[문제 분석]
사용자가 입력한 값과 컴퓨터가 생성한 랜덤 값을 비교한다.
몇번만에 맞혔는지 알려준다.

사용자에게 힌트를 준다.
사용자가 입력한 값이 랜덤값보다 크면 숫자는 작다라고 한다.
사용자가 입력한 값이 랜덤값보다 작으면 숫자는 크다고 한다.

사용자가 값을 입력하여 힌트를 받을때마다 count를 증가한다.

'''

# 알고리즘
#


import random
count = 0
random_num = random.randint(1,10)
int(random_num)
while True :
    input_num = int(input('숫자 입력 : '))
    if input_num == random_num :
        print('힌트 사용 : ' + str(count) + '번, 정답입니다.')
        break
    if input_num != random_num:
        if input_num > random_num:
            print('입력한 정수가 랜덤 숫자보다 작습니다.')
            count += 1
        elif input_num < random_num:
            print('입력한 정수가 랜덤 숫자보다 큽니다.')
            count += 1
print('프로그램을 종료합니다.')