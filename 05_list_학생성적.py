'''
학과 : 컴퓨터공학부
학번 : 202395025
이름 : 이준서
'''
'''
학생 이름과 점수를 입력받아 list에 저장하고,
학생 점수의 총점과 평균을 출력하시오.

[알고리즘]
0. 빈 학생 리스트 생성
1. 학생 수 입력 받기
2. 학생 수 만큼 반복하면서
    1) 학생 이름과 점수 저장 - 리스트
    2) 점수 합계 계산
3. 리스트에 저장된 학생 정보를 출력
4. 총점, 평균 출력
'''
stu = []
sum = 0
num = int(input('학생 수 입력 : '))
for i in range(num):
    print('<', i+1 ,'번째 학생 정보 입력 >')
    name = input('학생 이름 입력 : ')
    score = int(input('%s의 점수 입력 : ' %name))
    stu.append([name, score])
    sum = score + sum

print()
for i in stu:
    print('이름 : ', i[0], '점수 : ', i[1])

print('학생 점수 합계 : ', sum)
print('평균 : {:.2f}' .format(sum/num))