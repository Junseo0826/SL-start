'''
continue
'''
# 리스트의 값 10개 중에서 10보다 큰 수를 출력하시오.
numbers = [2,4,16,54,47,99,21,34,61,28]

print('리스트 값 중 10보다 큰 수 - 반복문 사용')
numbers.sort()
for i in numbers:
    if i >= 10:
        print(i, end=', ')
        
print()
print('\n')

print('리스트 값 중 10보다 큰 수 - continue 사용')
for i in numbers:
    if i < 10:
        continue
    print(i, end=', ')
    
print()
print('\n')
# 1~30 사이의 수 중에서 7의 배수만 출력하시오. - continue 사용
number = range(1,31)
for i in number:
    if i % 7 != 0:
        continue
    print(i, end=', ')
print()
