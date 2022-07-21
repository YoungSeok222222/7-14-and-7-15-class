# 함수(function): 반복하고 싶은 것을 모아 놓은 것
# Built -in Functions(내장함수) / not built-in Functions


def hello():
    print('안녕하세요!')
    
print(hello())

count = 0
while count <3:
    hello()
    count +=1

# 모듈 = 함수 파일 /  모듈 사용할 때는 import 사용
# 이 코드는 random 모듈을 불러와  random 모듈의 choice 함수를 사용한 것
import random

menu = ['pork','rice','water']

lunch = random.choice(menu)
print(lunch)
print(f'오늘의 점심은 {lunch}입니다.')

import random 
numbers = range(1,46)
lucky = random.sample(numbers,6)
print(lucky)
print(f'오늘의 행운의 번호는{sorted(lucky)}')





