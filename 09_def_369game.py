'''
학과 : 컴퓨터공학부
학번 : 202395025
이름 : 이준서

사용자로부터 정수를 입력 받아 1부터 입력 받은 수까지
369 게임을 진행합니다.
3, 6, 9에서는 '짝'을
10, 20, 30... 10의 배수 자리에는 '만세'를 출력하는 부분을 함수로 작성하시오.
'''
def jjak(input_num):
    for i in range(1, input_num+1):
        if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
            print('짝', end=' ')
        elif i % 10 == 0:
            print('만세 \n')
        else :
            print(i, end=' ')
input_num = int(input('369게임 숫자 입력 : '))
jjak(input_num)