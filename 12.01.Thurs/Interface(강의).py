# 파이썬은 아쉽게도 Interface가 존재하지 않기 때문에 class로 대체
class Socket():
    def enable(self):
        pass
    def disable(self):
        pass


class Dansang(Socket):
    def enable(self):
        self.zizizi()

    def disable(self):
        self.gogogo()

    def zizizic(self):
        print('zizi')
    
    def gogogo(self):
        print('ggg')


# Client 코드

s = Dansang()
s.enable()
s.disable()

# 한 클래스에서 다른 클래스를 사용할 때 "의존성을 갖는다"고 표현. 의존성의 정도는 다를 수 있다.


#=================================================================
# 정리!!!!

# Interface 역할
#   1. 리모컨
#   2. 표준화

# 구현 활용
#   1. DI
#   2. Factory