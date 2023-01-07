
public class _47_단일상속_Object클래스 {
    public static void main(String[] args) {
//ch7-5 단일 상속(Single Inheritance)
        // - Java는 단일상속만 허용한다.(C++은 다중상속 허용)
        // - 비중이 높은 클래스 하나만 상속관계로, 나머지는 포함관계로 한다.



//ch7-6 Object클래스 - 모든 클래스의 ◤조상◢
        // - 부모가 없는 클래스는 자동적으로 Object클래스를 상속받게 된다.
        // - 모든 클래스는 Object클래스에 정의된 11개의 메서드를 상속받는다.
                // toString(), equals(Object obj), hashCode(), ...


/*
class Tv {     부모 X                                     class Tv extends Object {   부모 없으면 컴파일러가 자동으로 추가
    ...                                컴파일러 이후              ...
}                                           =>            }

class smartTv extends Tv {  부모 O                        class smartTv extends Tv {
    ...                                                         ...
}                                                        }
*/


    }
}


