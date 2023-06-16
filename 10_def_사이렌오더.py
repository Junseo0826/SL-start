'''
학과 : 컴퓨터공학부
학번 : 202395025
이름 : 이준서

사이렌 오더를 통해 음료를 미리 예약하는 프로그램을 만드시오.
<메뉴>
아메리카노 : 2500원
카페라떼 : 3000원
바닐라 라떼 : 3000원
메뉴 번호를 선택하면 해당 메뉴와 가격을 출력해 주는 부분을
함수로 작성하시오.
선택한 메뉴는 인수로 전달되어
가격이 결과 값으로 반환되는 함수로 작성하시오.

사용자가 음료를 선택하면 음료의 가격을 알려주는 프로그램
'''
def order(selection):
    if selection == 1:
        result = '아메리카노 가격은 2500원입니다.\n'
        return result
    elif selection == 2:
        result = '카페라떼 가격은 3000원입니다.\n'
        return result
    elif selection == 3:
        result = '바닐라 라떼 가격은 3000원입니다.\n'
        return result
    elif selection < 0 or selection > 3:
        print('잘못된 메뉴 번호를 입력하였습니다.')

print('가격 정보 확인')
print('아메리카노 메뉴 번호 : 1번\n카페라떼 메뉴 번호 : 2번\n바닐라 라떼 메뉴 번호 : 3번')
while True:
    selection = int(input('메뉴 번호 (종료:0): '))
    if selection == 0:
        break
    order(selection)
    result = order(selection)
    print(result)