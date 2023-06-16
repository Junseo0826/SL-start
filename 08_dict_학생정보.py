'''
학과 : 컴퓨터공학부
학번 : 202395025
이름 : 이준서

학생 정보(학번, 이름)를 사전에 저장하고,
특정 학생의 정보(학번)을 입력하여 학생을 찾아주세요.

[알고리즘]
1. 학생 정보 저장 사전 만들기 (빈 사전 만들기)
2. 학생 정보를 입력받기 (사전에 저장) , (z키를 누르면 종료 - 무한 반복)
3. 학번으로 검색하여 학생 찾기 (학번이 빈칸이면 검색 종료 - 무한 반복)
'''
student = {}

while True:
    num = input('학생 학번 : ')
    if num == 'z':
        break
    name = input('학생 이름 : ')
    student[num] = name 
while True:
    key = input('찾고 싶은 키 입력 : ')
    if key in student:
        print(student[key])