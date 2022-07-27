class Nationality():
    def __init__(self,nation):
        self.nation = nation

    def __str__(self):
        return f'나의 국적은{self.nation}'



Korea_nationality = Nationality("대한민국")
print(Korea_nationality)        #나의 국적은 대한민국


###################################
#7-3
# Calculator 클래스
#add
#substract
#multiply
#divide
class Calculator():
    def __init__(self):
        pass

    def add(self,a,b):
        return a + b
    
    def substract(self,a,b):
        return a + b
    
    def multiply(self,a,b):
        return a + b
    
    def divide(self,a,b):
        try:
            return a/b
        except:
            return '0으로는 나눌 수 없습니다.'

cal = Calculator()
print(cal.add(2,3))
print(cal.substract(2,3))
print(cal.mulitply(2,3))
print(cal.divide(2,3))



