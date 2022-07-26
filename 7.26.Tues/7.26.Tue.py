
##제너레이터 
num = input()
def fn_d(num):
    result = 0
    for x in range(len(num)):
        result += int(num[x])
    return result+int[num]
  
     

print(fn_d(num))
#
number = int(input())
def is_selfnumber(x):
    fn_d(x)


is_selfnumber(number)
###################################
#월말평가 6번




# def caesar(word,n):
#     li = list(word)
#     print(li)
#     #소문자는 소문자로 / 대문자는 대문자로 암호화
#     #문자열의 islower(), isupper() 메서드로 소문자, 대문자 여부를 알 수 있다.
#     for i in range(len(li)):
#         if li[i].isupper():
#             li[i] = chr(65 + ((ord(li([i])) - 65 + n) % 26))
#         elif li[i].islower():
#             li[i] = chr(97 + ((ord(li[i])- 97 + n)%26))
        
#     return ''.join(li)    
        
# print(caesar('apple',5))
#################################################


#1번
def count_vowels(x):
    result = 0
    voewels = ['a','e','i','o','u']
    for vowel in voewels:
        result += x.count(vowel)
    
    return result
print(count_vowels('apple'))
print(count_vowels('banana'))
### 또다른 방법
def count_vowels(word):
    vowels = 'aeiou'
    count = 0
    for vowel in vowels:
        count += word.count(vowel)
    return count
print(count_vowels('apple'))
print(count_vowels('banana'))

# #2번 4번?

#3번########################
square_area= ([32,55,63],[13,32,40,55])
def only_square_area(L1,L2):
    new_list = []
    for i in range(len(L1)):
        for j in range(len(L2)):
            if L1[i] == L2[j]:
                new_list.append(L1[i]*L2[j])
    return new_list 

           
print(only_square_area([32,55,63],[13,32,40,55]))

####또다른 방법
def only_square_area(widths,heights):
    combination_list = []
    for width in widths:
        if width in heights:
            combination_list.append(width**2)
    return combination_list
print(only_square_are([32,55,63],[13,32,40,55]))


#######################
##데일리 실습 6-5
# 교수님 코드 (재귀함수를 이용해 각 자리수의 합을 구하는것 ex.123 => 6)

# def sum_of_digit(num):
#     if num < 10:
#         return num
#     return num % 10 + sum_of_digit(num//10)



# print(sum_of_digit(5))
# print(sum_of_digit(1234))
       
##############################################
#0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
#피보나치 수열
def fibonacci(num):
    if nuㅡ <2:
        return num
    return fibonacci(num-1) + fibonacci(num-2)
   
        

### list로 피보나치 받을 때
fibo_list = []
for i in range(18):
    fibo_list.append(fibonacci(i))
print(fibo_list)
###

print(fibonacci(5))  
      
   
#####################
#하노이 탑

def hanoi(N,start,end,other):
    if N ==1:
        print(f'{start}->{end}')
        return
    
    hanoi(N-1,start,other,end)
    print(f'{start}->{end}')
    hanoi(N-1, other, end, start)


#원판의 갯수, 시작, 도착, 서브 기둥 번호
N = 3
hanoi(3,1,2,3)  
#############################

###########################
#데일리 6-2
#### mass_percent.py 파일

def mass_1():
    result_s = []
    result_w = []
    for i in range(6):
        if i == 5: # 5번까지만 입력
            break

        a = list(input('소금물의 농도와 소금물의 양을 입력하세요 : ').split())
        s = a[0]

        if i >= 1 and s == 'Done': # 1번이상의 입력값을 받은 상태에서 Done 입력시 계산
            break
        else:
            w = a[1]
            s,w = int(s),int(w)
            s = (s*w) / 100 # 소금의 양
            w = w - s # 물의 양 (소금물- 소금)
            result_s.append(s)
            result_w.append(w)

    result_w = sum(result_w) # 총 물의 양
    result_s = sum(result_s) # 총 소금의 양
    result_sw = result_w+result_s # 총 소금물의 양

    s = (result_s/result_sw)*100 # 농도
    w = result_w + result_s # 소금물의 양
    return print(f"소금물의 농도는 : {round(s,2)}%\n소금물의 양은 : {round(w,2)}g")
mass_1()
#################

import mass_percent

mass_percent.mass_1()
###########
#소금 = 농도/100 * 소금물
#농도 = 소금/소금물 *100
##############################################
# 소금물 농도 = 소금의양/소금물의 양 *100
# 소금의 양 = 소금물 농도*소금물의 양 /100

salt=0
total=0
for _ in range(5):
    arr = list(map(str, input().split()))
    if arr[0]=='Done':
        break
    else:
        perc, s_water = int(arr[0][:-1]), int(arr[1][:-1]) #perc: 소금물의 농도, s_water: 소금물의 양
        salt+=perc*s_water/100
        total+=s_water
percent = salt/total*100
print(f'{percent: .2f}% {round(total, 2)}g')


##############################################

#무엇이 중복일까 (오늘자 workshop 1번 문제)
def duplicated_letters(words):
    result = []
    for word in words:
        if  words.count(word) > 1 and word not in result:
            result.append(word)
    return result
    
duplicated_letters('apple') #=> ['p']
duplicated_letters('banana') # =>['a','n']
##########
#다른 풀이 법
def duplicated_letters(words):
    return list(word for word in words if words.count(word)>1)

duplicated_letters('apple') #=> ['p']
duplicated_letters('banana') # =>['a','n']
######
result = []
def duplicated_letters(words):
    return [word for word in words if words.count(word) > 1 and not (word in result or result.add(word))]
###############################
#workshop 2번문제
def low_and_up(word):
    new_str = ''
    for idx, char in enumerate(word,start=1):
        if idx % 2 ==1:
            new_str += char.lower()  
        else:
            new_str += char.upper()

    return new_str

print(low_and_up('apple'))
print(low_and_up('banana'))
####
def low_and_up2(word):
    new_str = [(char.lower() if idx %2 else char.upper()) for idx,char in enumerate(word,start = 1)]
    return ''.join(new_str)

print(low_and_up('apple'))
print(low_and_up('banana'))








