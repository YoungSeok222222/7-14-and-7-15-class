# 제어문 
- 파이썬은 기본적으로 위에서부터 아래로 차례대로 명령을 수행
특정 상황에 따라 코드를 선택적으로 실행(반복)하는 제어가 필요함
- 제어문은 순서도(flowchart)로 표현이 가능

 ### 조건문 conditional statement
- 조건문은 참/거짓을 판단할 수 있는 조건식과 함께 사용
- 조건에는 참/거짓에 대한 조건식 
  - 조건이 참인 경우 이후 들여쓰기 되어있는 코드 블록을 싱행
  - 이외의 경우 else 이후 들여쓰기 되어있는 코드 블록을 실행
      - else는 선택적으로 활용할 수 있음
---



### 중첩 조건문 
- 조건문은 다른 조건문에 중첩되어 사용할 수 있음
 #### 조건 표현식
     - 조건 표현식 conditional expression
    - 조건 표현식을 일반적으로 조건에 따라 값을 정할 떄 사용
    - 삼항 연산자(Ternary Operator)
        True 경우 값 if 조건 else Flase 인 경우 값
```python
value = num if num>=0 else -num
```
---

### 반복문; 특정 조건을 만족할 때까지 같은 동작을 계속 반복하고 싶을 때 사용
#### 반복문의 종류
#### __while 문__
    - 종료 조건에 해당하는 코드를 통해 반복문을 종료시켜야 함
    - while문은 조건식이 참인 경우 반복적으로 코드를 실행
    - 코드 블록이 모두 실행되고, 다시 조건식을 검사하면 반복적으로 실행됨
    - while문은 무한 루프를 하지 않도록 종료 조건이 반드시 필요
#### 복합 연산자(In-Place Operator)
- 복합 연산자는 연산과 할당을 합쳐 놓은 것
```python
a = 0
while a< 5:
    print(a)
    a+= 1
print('끝')
```
        
#### __for 문__
  - 반복가능한 객체를 모두 순회하면 종료(별도의 종료 조건이 필요 없음)
- for문은 시퀀스(string,tuple,list,range)를 포함한 순회 가능한 객체(iterable)의 요소를 모두 순회
    - 처음부터 끝까지 모두 순회하므로 별도의 종료 조건이 필요하지 않음
#### iterable
- 순회할 수 있는 자료형(string,list,dict,tuple,range,set등)
- 순회형 함수(range,enumerate)
- 반복 제어
    - break, continue,for-else(끝까지 반복문을 실행한 이후에 else문 실행)
- for문을 이용한 문자열(string)순회
```python
#for문을 이용한 문자열(string) 순회
x = input()
for word in x:
    print(word)
--- 
x = input()
for idx in range(len(x)):
    print(x[idx]) #input으로 받은   
                #단어[idx번째 문자]   
#
h
a
p
p
y
```
```python
#딕셔너리 순회
topgun = {'goose': 75, 'maverick':97}
for students in topgun:
    print(students,topgun[students])
    #딕셔너리를 순회하여 students 값에 key값을 넣고, topgun[student]는 딕셔너리의 value 값을 key값에 따라 출력 
topgun.keys() #key값
topgun.value() #value 값
topgun.itmes() # key + value 값
```
```python
# enumerate 순회
members = ['goose','iceman','maverick']
for idx, name in enumerate(members):
    print(idx,name)
'''
0 goose
1 iceman
2 mavercik
'''
#enumerate(members,start=1) # 인덱스를 1부터 시작
```    
## List Comprehension
- 표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성하는 방법
    - __[code for 변수 in iterable]__
    - __[code for 변수 in iterable if 조건식]__ 
```python
#1~3의 세제곱 리스트 만들기
num_list = []
for number in range(1,4):
    num_list.append(number**3)
print(num_list)
#[1,8,27]

num1_list = [number ** 3 for number in range(1,4)]
#[1,8,27]
```
---
## 함수를 왜 사용할까?
- __Decomposition(분해)__: 기능을 분해하고 재사용 가능하게 만들고
- __Abstraction(추상화)__: 복잡한 내용을 모르더라도 사용할 수 있도록(스마트폰) / 재사용성과 가독성, 생산성
  - 사실 내부 구조를 변경할게 아니라면 몰라도 무방
  - 그것이 함수의 장점이자 프로그래밍의 매력
  - 스마트폰의 원리를 잘 몰라도 우리는 잘 사용할 수 있음
---
## 함수 기초
### 함수의 종류
- 함수는 크게 3가지로 분류
    - 내장함수: 파이썬에 기본적으로 포함된 함수
    - 외장함수: import문을 통해 사용하며, 외부 라이브러리에서 제공하는 함수
    - 사용자 정의 함수: 직접 사용자가 만드는 함수 def
---
### 함수의 기본 구조
- 선언과 호출(defin & call)
  - 함수의 선언은 def키워드를 활용함
    - 들여쓰기를 통해 Function body(실행될 코드 블록)을 작성함
    - Docstring은 함수 body 앞에 선택적으로 작성 가능
    - 작성 시에는 반드시 첫 번째 문장에 문자열
    - 함수는 Parameter를 넘겨줄 수 있음
    - 함수는 동작 후에 return을 통해 결괏값을 전달함
---       
### 함수의 정의
- 함수를 사용하기 위해서는 먼저 함수를 정의해야 함
```python
def function_name(parameter)
                #code block 
                return
                returning_value
```
- 선언과 호출(define & call)
    - Parameter가 있는 경우, 함수명 (값1,값2...)로 호출
---        
## 함수의 결과값(output) - 값에 따른 함수의 종류
- void function
    - 명시적인 return값이 없는 경우, None을 반환하고 종료
- value returning function
  - 함수 실행 후, return문을 통해 값 반환
  - return을 하게 되면, 값 반환 후 함수가 바로 종료
- print는 값을 출력하지만, 값을 반환하진 않습니다.
### print 함수와 return의 차이점
- print를 사용하면 호출될 때마다 값이 출력됨(주로 테스트를 위해 사용)
- 데이터 처리를 위해서는 return 사용
---    
#### 두 개 이상의 값 반환
```python
def minus(x,y):
    return x-y, x* y #이건 2개의 값 가능
    #return x*y는 불가능 return은 하나만 즉, 윗줄에서 출력하고 끝
# 또한 반환 값으로 튜플 사용
# 여러 값 반환 원하면 튜플(혹은 리스트와 같은 컨테이너 활용)
y = minus(4,5)
print(y) #(-1,20)
print(type(y)) # <class'tuple'>
```
--- 
### 함수의 입력(input)
#### __parameter: 함수를 정의할 때, 함수 내부에서 사용되는 변수__
#### __arguments: 함수를 호출할 때, 넣어주는 값__
- 함수 호출 시 함수의 parameter를 통해 전달되는 값
- Argumgent는 소괄호 안에 할당  func_name(argument)
    - 필수 Argument:반드시 전달되어야 하는 argument
    - 선택 arguemnt: 값을 전달하지 않아도 되는 경우는 기본값이 전달
---
#### __positional argument:__ 
- 기본적으로 함수 호출 시 argument는 위치에 따라 함수 내에 전달됨
```python
def add(x,y):
    return x + y 

add(2,3) # x=2 y =3
```
#### __keyword arguments:__ 
- 직접 변수의 이름으로 특정 argument를 전달할 수 있음
- keyword argument 다음에 positional argument를 활용할 수 없음
    - keyword argument => positional argument (x)
    - positional argument => keyword argument (o)
```python
def add(x,y):    #add(x=2,y=5) (O)
    return x + y #add(2,y=5) (O)
                 #add(x=2,5) (x)
```
---
### Default Arguments Values
 - 기본값을 지정하여 함수 호출 시 argument 값을 설정하지 않도록 함
 - 정의된 것보다 더 적은 개수의 argument들로 호출될 수 있음
```python
def add(x,y=0):   # x에 2가 들어감
    return x + y
add(2)
```
---
## __정해지지 않은 여러 개의 Arguments 처리__
애스터리스크(Asterisk)혹은 언패킹 연산자라고 불리는 * 덕분 
  ## __가변인자(*args) / args는 변경 가능__ 
    - 여러개의 positional argument를 하나의 필수 parameter로 받아 사용
  - 가변인자는 언제 사용?
    - 몇 개의 positional argument를 받을지 모르는 함수를 정의할 때 유용
```python
def add(*args);
    for arg in args:
        print(arg)

add(2,3,4,5)     
---
#패킹: 여러개의 데이터를 묶어서 변수에 할당하는 것
numbers = (1,2,3,4,5)
print(numbers) #(1,2,3,4,5)


#언패킹: 시퀀스 속의 요소들을 여러 개의 변수에 나누어 할당하는 것
numbers = (1,2,3,4,5)
a, b, c, d, e = numbers #언패킹
print(a, b, c, d, e) #1 2 3 4 5
---
numbers = (5,6,7,8,9)
a,b, *rest = numbers # 5,6을 제외한 나머지를 rest에 대입
print(rest)          # [7,8,9]
---

#가변인자 예시 - packing을 통해 받은 모든 숫자들의 합을 구하는 함수 만들기
def sum_all(*numbers):
    result = 0
    for number in numbers:
        result+= number
    return result
print(sum_all(1,2,3)) #6
print(sum_all(1,2,3,4,5,6)) #21
----

def family_name(father,mother,*pets):
    print(f'아버지:{father}')
    print(f'어머니:{mother}')
    print(f'동물들')
    for name in pets:
        print(f'반려동물:{name}')
family_name('아부지','어머니','멍멍','냥냥')  
```
## 가변 키워드 인자(**kwargs)
```python
 -몇 개의 키워드 인자를 받을지 모르는 함수를 정의할 때 유용
 -**kwargs는 딕셔너리로 묶여 처리되며, parameter에 **를 붙여 표현

 def family(**kwargs):
    for key, value in kwargs.items():
        print(key,':',value)
family(father ='아버지', mother = '어머니', baby = '응애')
'''
father : 아버지
mother : 어머니
baby  : 응애
'''
---
#반드시 받아야하는 키워드 인자와, 추가적인 키워드 인자를 구분해서 사용할 수 있음
def family_name(father,mother, **pets):
    print("아버지:",father)
    print("어머니:", mother)
    if pets:
        print('반려동물들..')
        for species, name in pets. items():
            print(f'{species}:{name}')
family_name('아부지','어머이',dog = '멍멍이', cat ='냥냥이')      

'''
아버지: 아부지
어머니: 어머이
dog : 멍멍이
cat : 냥냥이
'''
```
## __가변인자(*args) + 가변 키워드 인자(**kwargs)동시 사용 예시__
 -가변인자와 가변 키워드 인자를 함꼐 사용할 수 있음
 ```python
def family(*parents, **pets): 
    print("집안의 기둥:", parents[0])
    print("집안의 주인:", parents[1])
    if pets:
        print('반려동물들:')
        for title, name in pets.items():
            print('{}:{}'.format(title,name))
family('아버지','어머니', dog ='멍무이', cat = '야옹이')
'''
집안의 기둥 : 아버지
집안의 주인 : 어머니
반려동물들:
dog : 멍무이
cat : 야옹이