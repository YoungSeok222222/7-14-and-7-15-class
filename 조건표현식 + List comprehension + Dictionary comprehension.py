#조건 표현식(==삼항연산자)  / 좌참 if 우거
num  = 5
print("0보다 큼") if num >0 else print("0보다 작음")
###########################################################

#List comprehension(표현식과 제어문을 통해 리스트 생성)
# 기본형 - 1~3의 세제곱 구하기
cubic_list = []
for num in range(1,4):
    cubic_list.append(num ** 3)
print(cubic_list)    #[1,8,27]

#List comprehension으로 표현    [code for 변수 in iterable] or [code for 변수 in iterable if 조건식]
n_list = []
[n_list.append(num ** 3) for num in range(1,4)]
print(n_list)        #[1, 8, 27]
##########################################################

#Dictionary comprehension {key : value for 변수 in iterable} or {key :value for 변수 in iterable if 조건식}
#기본형
num_dic = {}
for i in range(1,4):
    num_dic[i] = i ** 3
print(num_dic)       #{1: 1, 2: 8, 3: 27}

#Dictionary comprehension으로 표현
print(dict({number : number**3 for number in range(1,4)}))   #{1: 1, 2: 8, 3: 27}