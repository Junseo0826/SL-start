'''
학과 : 컴퓨터공학부
학번 : 202395025
이름 : 이준서
'''
'''
"학생 관리" 프로그램을 작성하시오.
이 프로그램은 종료 시킬 때까지 무한 반복된다.
- "작업 선택 : "에서 0 입력 시 프로그램이 종료된다.
- "작업 선택 : "에서 1 입력 시 관리하는 학생 목록이 조회된다.
- "작업 선택 : "에서 2 입력 시 학생을 추가할 수 있다.
- "작업 선택 : "에서 3 입력 시 학생을 삭제할 수 있다.
이때 입력한 학생은 관리하는 학생 목록에 있는 데이터만 삭제 가능하도록 하며
목록에 없는 학생을 삭제하고자 할 때는
'삭제할 학생이 없습니다. 다시 입력하세요!'를 화면에 출력한다.
'''
stu = []
while True:
    selection = int(input('작업 선택 : '))
    if selection == 0:
        break
    elif selection == 1:
        print(stu)
    elif selection == 2:
        name = input('학생 이름 입력 : ')
        stu.append(name)
    elif selection == 3:
        find_name = input('삭제할 학생 이름 : ')
        if find_name == name:
            stu.remove(find_name)
        else:
            print('삭제할 학생이 없습니다. 다시 입력하세요!')

print('프로그램을 종료합니다.')