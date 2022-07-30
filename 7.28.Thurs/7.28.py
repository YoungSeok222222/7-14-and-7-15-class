#데일리 7-2
class Doggy:
    num_of_dogs = 0
    birth_of_dog = 0
     

    def __init__(self,name,breed):
        self.name = name #dog1.name = "ssafy"
        self.breed = breed #dog1.breed = "jindo"
        Doggy.birth_of_dog += 1
        Doggy.num_of_dogs += 1



    def get_status(): #클래스로 함수 호출하는 경우 self 없어도 됨 / 인스턴스로 함수 호출하는 경우 self필요
        return f"태어난 개의 수: {Doggy.birth_of_dog},현재 개의 수: {Doggy.num_of_dogs}"
    
    def bark(self):
        return f"견종: {self.breed}, 이름:{self.name}, 멍멍"

    def __del__(self):
        Doggy.num_of_dogs -= 1


dog1 = Doggy("싸피","jindo")
dog2 = Doggy("삼성","dacks")
print(dog1.bark())
print(dog2.bark())
del dog1
print(Doggy.get_status())
##############
7-3

class Calculator:
    def add(self,a,b):
        return a + b
        
    def substract(self,a,b):
        return a - b 

    def multiply(self,a,b):
        return a * b

    def divide(self,a,b):
        try:
           return  a / b
        except:
            return "0으로 나눌 수 없습니다."

cal = Calculator()
print(cal.add(1,2))
print(cal.substract(2,1))
print(cal.multiply(1,2))
print(cal.divide(4,0))
            
###################################
#데일리 7 -4   
class Carsharing:
    def __init__(self,time, distance):   
        
        self.time = time
        self.distance = distance
    
    # @classmethod
    def fee(self):
        
        lent_fee =  (self.time//10) * 1200
        if (self.time + 10) % 60 ==0:
            insurance_fee = (self.time//60) *1050 
        else:
            insurance_fee = (self.time//30) * 525
        
        if self.distance >100:
            driving_fee =  100 * 170 +((self.distance - 100)*85)
        else:
            driving_fee = self.distance * 170
        result = lent_fee + insurance_fee + driving_fee
      
            
        return f"총액: {result}"


    
time, distance  = map(int, input("시간과 거리를 띄어쓰기로 구분하여 입력하세요").split())
car1 = Carsharing(time,distance)
print(car1.fee())
#########################################
#데일리과제 7-4
class calculator:
    count = 0
    def __init__(self,num):
        self.num = num


    def collatz(self):
        while self.num != 1:
            calculator.count += 1
            if self.num %2 ==0:
                self.num = self.num //2
                
            else:
                self.num = self.num * 3 + 1
            if calculator.count > 500:
                return -1
        return calculator.count 




number = calculator(int(input()))
print(number.collatz())

 ####################################
# 8 - 2
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def detail(cls,name,year):
        age = 2022 - year
        return cls(name,age)

    def get_info(self):
        print(f"이름:{self.name}, 나이{self.age}")

    def check_age(self):
        print(f"현재 나이는 {self.age}입니다.")
        if self.age < 19:
            return True
        return False



# p1 = Person("Maverick", 56)
# print(p1.check_age())
p1 = Person.detail("Maverick",2000)
print(p1.check_age())
# print("미성년자 입니다.") if p1.check_age() == True else print("성인입니다.")
#    True                /    조건                   /    거짓


##################################################
# 8-3
class PublicTransport():
    def __init__(self,passengers, fare):
        self.passengers = passengers
        #인당 요금
        self.fare = fare
       
        #탑승할 때마다 요금 추가
        self.total = 0

    def get_in(self,passenger):
            self.passengers += passenger
            self.total += passenger * self.fare
            print(f"현재 탑승인원 {self.passengers}")

        #내리는 메서드
        #승객 수만 감소
    def get_off(self,passenger):
        self.passengers -= passenger
        print(f"현재 탑승인원 {self.passengers}")


    def profit(self):
        print(f'현재 탑승중인 인원:{self.passengers}/ 총 수익:{self.total}')


transport = PublicTransport(0,100)
transport.get_in(20)
transport.get_in(10)
transport.get_in(40)
transport.get_off(30)
transport.profit() # 탑승인원 : 40 / 총 수익 : 7000

# #################
# 8-3 다른 풀이법
# 탑승객 수(passengers) 와 요금(fare)를 받는다.
class PublicTransport():
    # 탑승객 수와 요금을 입력받아 초기화하는 메서드
    total_profit = 0
    person = 0
    def __init__(self,passengers, fare):
        self.passengers = passengers
        self.fare = fare
        

    # 탑승 메서드
    # passenger 를 파라미터로 받음
    # 새로 탄 승객에 따라 총 요금에 추가
    def get_in(self, passenger):
        PublicTransport.person += passenger
        PublicTransport.total_profit += self.fare * passenger
        print(f"총 승객 수: {PublicTransport.person}, 현재 수익{PublicTransport.total_profit}")
        

    # 내리는 메서드
    # 승객 수만 감소
    def get_off(self, passenger):
        PublicTransport.person -= passenger
        print(f"총 승객 수: {PublicTransport.person}, 현재 수익{PublicTransport.total_profit}")
     

    # 현재 탑승중인 인원과 최종 수익을 출력
    def profit(self):
        print(f"총 수익: {PublicTransport.total_profit}")
      


if __name__ == '__main__':
    transport = PublicTransport(0, 1200)
    transport.get_in(20)
    transport.get_in(10)
    transport.get_in(40)
    transport.get_off(30)
#     transport.profit() # 탑승인원 : 40 / 총 수익 : 7000
#####################################
# 데일리 8-4
class Bus(PublicTransport):
    def __init__(self,limit,passengers,fare):
        self.limit = limit
        super().__init__(passengers,fare)



    #overide
    def get_in(self,passenger):
        
        
        if PublicTransport.person + passenger > self.limit:
            print("더 이상 탑승할 수 없습니다.")
            rest = passenger - (self.limit - PublicTransport.person)
            print(f"더 태울 수 있는 인원 수:{rest}")
            PublicTransport.person += passenger - (self.limit - PublicTransport.person)
            #제한에 딱 맞도록 인원을 태움
            print(f"총 승객 수: {PublicTransport.person-(PublicTransport.person-self.limit)}, 현재 수익{PublicTransport.total_profit}")
           
           
            
if __name__ == '__main__':
    # transport = PublicTransport(0, 100)
    bus = Bus(100,0,1200)
    bus.get_in(70)
    bus.profit()
    # transport.get_in(20)
    # transport.get_in(10)
    # transport.get_in(40)
    # transport.get_off(30)
    # transport.profit() # 탑승인원 : 40 / 총 수익 : 7000


###############################################
# 데일리 과제 8-2
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
class Rectangle:
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
    
    #넓이 변환
    def get_area(self):
        return abs((self.p2.x - self.p1.x) * (self.p2.y - self.p1.y))

    #둘레 반환
    def get_perimeter(self):
       return (abs(self.p2.x - self.p1.x) + abs(self.p2.y - self.p1.y))*2
    #정사각형 판별
    def is_square(self):
        return abs(self.p2.x - self.p1.x) == abs(self.p2.y - self.p1.y)

p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())
p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())
###########################
# 데일리 과제 8-4
#8-4
class Stack:
    def __init__(self):
        self.data = []
    
    #스택이 비었다면 True, 그렇지 않다면  False를 반환
    def empty(self):
        if self.data == []:
            return True
        return False 
        #return True if self.data ==[] else False    <==삼항 연산자로 위 코드 작성

    #스택의 가장 마지막 데이터 반환, 스택이 비었다면 None을 반환
    def top(self):
        flag  = self.empty()
        if flag == True:
            return None
        return self.data[-1]
        #return self.data[-1] if self.empty() is not True else None 주석을 바로 삼항연산자로 바꾼것
    
    #스택의 가장 마지막 데이터 값을 반환하고, 해당 데이터 삭제
    #스택의 가장 마지막 데이터 반환, 스택이 비었다면 None을 반환
    def pop(self):
        flag = self.empty()
        if flag == True:
            return None
        #리스트의 함수 중 삭제 + 반환을 동시에 해준는 함수 = pop()
        return self.data.pop(len(self.data)-1)
        #return self.data.pop(len(self.data)-1) if self.empty() is not True else None #True를 삼항 연산자 앞에
        #return None if self.empty() else self.data.pop(len(self.data)-1) #False를 삼항 연산자 앞에
    
    #스택의 가장 마지막 데이터 뒤에 값 추가. 반환값 없음
    def push(self,data):
        self.data.append(data)

    #현재 스택 요소들 출력       
    def __rper__(self):
        return f'{self.data}'


stack = Stack()
print(stack.empty())
print(stack.top())
print(stack.pop())
print(stack.push(5))
print(stack.__repr__())

##################
# 데일리 실습 7-5
import random

class Students():
    # pass 는 주석을 포함하여 지워주세요.
    
    # 1. 초기화 메서드 작성
    def __init__(self,students_list):
        self.students_list = students_list
        

    # 2. 학생들 인자에서 인자 n 명 만큼 랜덤으로 추출하여 return 하는 pick 함수 작성
    # 참고 - random.sample 함수를 검색해보세요.
    def pick(self):
        return random.sample(self.students_list,2)

    # 3. 랜덤으로 2명(명단의 수가 홀수면 한 팀은 3명) 매칭하여 리스트로 반환하는 함수 match_pair 작성
    def match_pair(self):
        n_list1 = []
        while len(self.students_list) >3:
           
            result = self.pick()
            print(result)
            n_list1.append(result)
            self.students_list.remove(result[0])
            self.students_list.remove(result[1])
           
        n_list1.append(self.students_list)
        return n_list1
          

if __name__ == '__main__':
    students_list = ['김싸피', '금해피', '테스트', '철수킴', '박영희','고사피']
    students = Students(students_list)
    print(students.match_pair())
            