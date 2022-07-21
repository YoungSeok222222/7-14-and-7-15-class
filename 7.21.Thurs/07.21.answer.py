# 과일 봉지를 입력 받는다
# # 입력: 과일끼리는 , 로 구분
# # 출력: 신선한 과일 리스트(새로운 리스트)
# # 조건: 썩은 과일에는 접두사로 'RoTTen' / 반한된 요소는 모두 소문자로
# # 대소 관계 x 

#  ####################       
from pyrsistent import b


def problem3_1():
    fruits = input('과일을 입력하세요:').split(',')
    result = []
    for x in fruits:
        x.lower()
        if x[:6] == 'rotten':
            x = x[6:]
        result.append(x)
            
    print(result)


problem3_1()
# ####################


def problem3_2():
    name = input("입력하세요:")
    if len(name) %2 ==1:
        a = len(name)//2
        print(name[a:a+1])
    else:
        b= len(name)//2-1
        print(name[b:b+2])


problem3_2()
######################
# 문제 풀이 법
#  1. List 안의 Dictionary 요소 하나하나에 접근하는 방법
#  2. Dictionary에서 key 값으로 value를 꺼내오는 방법
#

infos = [{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]

def problem3_3():
    result = 0
    for x in infos:
        result= result + x['age']  # result += x.get('age')) /result += x['age'])
    print(result)
    
    
     
problem3_3()
###############################################
    
blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']

def problem3_4():
    blood_dict={}
    A_num = 1
    B_num = 1
    AB_num = 1
    O_num = 1
    for x in blood_types:
        if x == 'A':
            A_num += 1
        elif x == 'B':
            B_num += 1
        elif x == 'AB':
            AB_num += 1
        else:
             O_num += 1 
    blood_dict['blood type A'] = A_num
    blood_dict['blood type B'] = B_num
    blood_dict['blood type AB'] = AB_num
    blood_dict['blood type O'] = O_num
    print(blood_dict)
problem3_4() 
########################################
# blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']

count_dict = {}
for x in blood_types:
    try:
        count_dict[x]+= 1# key: value
    except:
        count_dict[x] = 1


#########################################
def problem3_4_0():
    count_dict={
        'A': 0,
        'B': 0,
        'AB': 0,
        'O': 0
    }

    for x in blood_types:
        count_dict[x] = count_dict[x] + 1
    print(count_dict)


               
problem3_4_0()   
##############################################

#####################################################  ############################       
#문제: 혼합물의 퍼센트 농도와 양이 출력되도록 하는 것
#입력: 퍼센트 농도, 소금물의 양, Done (입력 시 종료)
#조건: 
#  1.최대 5개의 소금물을 입력받을 수 있다.
#  2.출력된 혼합물의 농도를 반올림하여 소수점 2자리까지만 출력

#문제풀이 방법
# 1.입력을 어떻게 받을 것인가?
# 2.계산 시 이전의 소금물들을 어떻게 저장하고 있을 지?
# 3.소금물 농도 계산하는 법
def problem3_5():
    d = [] #퍼센트 농도
    w = [] #소금물의 양
    
    while True:
        s = input(f'{len(d)+1}:퍼센트 농도와 소금물의 양을 띄어쓰기로 구분하여 입력하세요(Done시 최종 계산):')
        if s == 'Done':
            break
        
        d.append(float(s.split()[0]))
        w.append(float(s.split()[1]))
        
        if len(d) == 5:
            break
    
    # print('d=',d )
    # print('w=', w)

#소금의 양: 소금물의 농도 / 100 * 소금물의 양
    solt = []
    for index in range(len(d)):
        s = d[index] * w[index] / 100
        solt.append(s)    
#소금물의 퍼센트 농도: (전체 소금의 양/ 전체 소금물의 양)
    result = (sum(solt) / sum(w)) * 100

    print(f'혼합물 퍼센트 농도:{round(result,2)}%  / 혼합물의 양: {sum(w)}')
problem3_5()
 ##########################################################################
############
def problem_daily1():
    year = int(input())
    if (year % 4 ==0 and year % 100!=0) or year % 400==0:
        print('윤년입니다.')
    else:
        print('윤년이 아닙니다.')


problem_daily1()
##########################################

def problem_daily2():
    
    a = list(map(int,input("각변의 길이를 입력하세요:").split()))
    cm= sorted(a)
    print(cm)
    
    if cm[0] == cm[1] == cm[2]:
        print('정삼각형 입니다.')
    elif cm[0] == cm[1] or cm[0] ==cm[2] or cm[1] ==cm[2]:
        print('이등변삼각형 입니다.')
    elif cm[0]**2 + cm[1]**2 == cm[2]**2:
        print('직각삼각형입니다.')
    elif cm[0] + cm[1] > cm[2]:
        print('삼각형입니다.')
    else:
        print('삼각형이 아닙니다.')    

problem_daily2()
    
############################








