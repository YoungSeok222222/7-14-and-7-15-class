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
