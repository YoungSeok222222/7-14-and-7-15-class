def module_func(word):
    print(f'{word}를 전달 받은 함수입니다.')


class moduleClass():
    def _int__(self, word='class'):
        self.word = word

    def __str__(self):
        return f'{self.word}를 전달받은 클래스입니다.'


###############
다른 모듈 불러와서 쓸 때, 
import module_class import module_func, moduleClass

cLs = modulecalss()
print(cLs)



def hello():
    print('hello')

def add_print(original):
    def wrap():
        print('add_print 함수 시작')
        original()
        print('add_print 함수 끝')
        return wrapper
        

########  
def add_print(original)
     