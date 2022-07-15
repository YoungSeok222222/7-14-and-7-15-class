
### while문 조건이 True인 동안 반복적으로 실행 되기에 종료조건이 반드시 필요
``` python
n = 1
while n<=10:
    print(n,end=:" ")
    n+= 1
```
---
# if, elif, else 함수
```python
my_level = 1445
if 1490 <= my_level:
    print('아브렐슈드')
elif 1475<= my_level < 1490:
    print('쿠크세이튼')
elif 1430<= my_level < 1475:
    print('비아키스')
elif 1415<= my_level < 1430: 
    print('발탄')
else:
    print('아직 레벨이 낮습니다.')
    
n = 0 
while n<3:
    print(n)
    n+=1
```
----
# for 함수
```python
levels = [1415,1430,1475,1490]
print(levels[0])
print(levels[1])
print(levels[2])
print(levels[3])

# for문 정해진 범위를 반복하기에 종료조건이 필요 없음
for x in levels:
    print(x)
 
 
greeting = '안녕하세요'   
#while 
count = 0
while count< 4:
    print(greeting)
    count+=1
    
#for 
for x in range(4):
    print(greeting)
```
---
# function
```python
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
print(menu)
#print(f'오늘의 점심은 {lunch}입니다.)

import random 
numbers = range(1,46)
lucky = random.sample(numbers,6)
print(lucky)
# print(f'오늘의 행운의 번호는{sorted(lucky)})
```
---
# import 
```python
import random 
numbers = range(1,46)
lucky = random.sample(numbers,6)
print(lucky)
# print(f'오늘의 행운의 번호는 {sorted(lucky)}')

#정렬하여 출력
print(sorted(lucky))
import requests

# 1021 회차 정보를 요청하는 주소
url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1021'

# 요청한 값에 따른 응답을 response 변수에 저장
response = requests.get(url).json()

# 응답(response) 에서 원하는 값 추출
- print('첫 번째 뽑힌 번호 : ', response.get('drwtNo1'))
- print('두 번째 뽑힌 번호 : ', response.get('drwtNo2'))
- print('세 번째 뽑힌 번호 : ', response.get('drwtNo3'))
- print('네 번째 뽑힌 번호 : ', response.get('drwtNo4'))
- print('다섯 번째 뽑힌 번호 : ', response.get('drwtNo5'))
- print('여섯 번째 뽑힌 번호 : ', response.get('drwtNo6'))
- print('보너스 번호 : ', response.get('bnusNo')
--- 
#1~10까지 숫자를 하나씩 출력해라
```
---
# requests
```python
# import requests를 사용하기 위해 터미널 창에 pip version 확인 후, pip install requests 입력
# ctrl + shift + p 로 python 확인(에러 뜨는 경우)
#.json() =  웹에서 제공하는 형태
import requests

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1021'
response = requests.get(url).json()
print(response)
# print(response.get('name'))
# print(response.get('age'))

#drwtNo1: 12 / drwtNo2: 15 / drwtNo3: 17 / drwt No4:24 / drwtNo5:29 / drwtno6: 45 / bnusno: 16
url2 = "http://google.com"
response2 = requests.get(url2)
print(response2)
```










    
   
    
    
    
    
    
    
    
    

        
    



