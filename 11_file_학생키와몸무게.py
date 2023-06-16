'''
학과 : 컴퓨터공학부
학번 : 202395025
이름 : 이준서

랜덤으로 10명의 키와 몸무게 생성하여 파일에 저장.
'''
import random

f_name =  list('김이박차성전남소조홍서')
s_name = list('가나다라마바사아자차카타파하')

with open('info.txt','w') as f:
    for i in range(10):
        name = random.choice(f_name) + random.choice(s_name) + random.choice(s_name)
        weight = random.randrange(40,100)
        height = random.randint(140,200)
        f.write('{}, {}, {} \n'.format(name,weight,height))