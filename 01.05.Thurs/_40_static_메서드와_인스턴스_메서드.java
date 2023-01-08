// ▶ 속성(멤버 변수)중에서 공통 속성에 static을 붙인다. -> 35 참조 : 공통된 변수는 static, 아닌거는 인스턴스 변수

// ▶인스턴스 멤버(iv, im)을 사용하지 않는 메서드에 static을 붙인다.
public class _40_static_메서드와_인스턴스_메서드 {
    public static void main(String[] args) {
// ch6-26 static 메서드와 인스턴스 메서드
        // 메서드 앞에 static이 붙은 것
        // 클래스 메서드 == static 메서드


// ▶ static 메서드(클래스메서드) - iv 사용  x
//      - 객체 생성없이 '클래스 이름.메서드이름()'으로 호출
//      - 인스턴스 멤버(iv, im)와 관련없는 작업을 하는 메서드
//      - 메서드 내에서 인스턴스 변수(iv) 사용불가
//      - 예를 들어 Math.random() 혹은 Math.round()


// ▶ 인스턴스 메서드(메서드 앞에 static이 붙지 않은 것) - iv 사용 o
//      - 인스턴스 생성 후, '참조변수.메서드이름()'으로 호출
//      - 인스턴스 멤버(iv, im)와 관련된 작업을 하는 메서드   / im: 인스턴스 메서드
//  `   - 메서드 내에서 인스턴스 변수(iv) 사요가능

    }

// 클래스 메서드와 인스턴스 메서드 예시

static class MyMath2 {
        long a,b;   // iv(instance variable 인스턴스 변수)

        long add() {    // 인스턴스 메서드
            return a + b;   //iv
        }

        static long add (long a, long b) {    // 클래스메서드(static 메서드), lv(local variable) 매개변수
            return a + b;                     // lv

        }
}
class MyMathTest2 {
        public static void main(String args[]) {
            System.out.println(MyMath2.add(200L,100L)); // 클래스 메서드 호출
            MyMath2 mm = new MyMath2();     // 인스턴스 생성(==iv 생성),  mm 참조변수(인스턴스 변수), a 객체, b 객체
            mm.a = 200L;
            mm.b = 100L;
            System.out.println(mm.add());   // 인스턴스메서드 호출, 참조변수.메서드이름();

        }
}

// 객체란? iv(instance variable - 인스턴스 변수)들의 모음

//===============================================================================================================

// ch6-28 static을 언제 붙여야 할까?
    // ▶속성(멤버 변수)중에서 공통 속성에 static을 붙인다. -> 35 참조 : 공통된 변수는 static, 아닌거는 인스턴스 변수

    // ▶인스턴스 멤버(iv, im)을 사용하지 않는 메서드에 static을 붙인다.

//================================================================================================================

// ch6-29 메서드 간의 호출과 참조
    // ▶static 메서드는 인스턴스 변수(iv)를 사용할 수 없다.

class TestClass2 {
        int iv;         // 인스턴스 변수
        static int cv;  // 클래스 변수

        void instanceMethod() {     // 인스턴스 메서드
            System.out.println(iv); // 인스턴스 변수를 사용할 수 있다.
            System.out.println(cv); // 클래스 변수를 사용할 수 있다.
        }

        static void staticMethod() {// static 메서드
//            System.out.println(iv); // 에러!!! 인스턴스 변수를 사용할 수 없다.
            System.out.println(cv); // 클래스 변수는 사용할 수 있다.
        }
}

//===============================================================================================

    // ▶ static 메서드는 인스턴스 메서드(im)을 호출할 수 없다.

    class TestClass {
        void instanceMethod() {}        // 인스턴스 메서드
        static void staticMethod() {}   // static 메서드

        void instanceMethod2() {        // 인스턴스 메서드
            instanceMethod();           // 다른 인스턴스메서드를 호출한다.
            staticMethod();             // static메서드를 호출한다.
        }

        static void staticMethod2() {
//                instanceMethod();           // 에러!!! 인스턴스메서드를 호출할 수 없다.   => 객체가 있을지 없을지 모르기 때문에 호출 불가능
            staticMethod();             // static메서드는 호출 할 수 있다.
        }
    }
//===========================================================================================================

    // Q. static 메서드는 static 메서드 호출가능? Y

    // Q. static 메서드는 인스턴스 변수(iv) 사용가능? N

    // Q. static 메서드는 인스턴스 메서드(im) 호출가능? N - 인스턴스 메서드는 iv로 작업하는 메서드

    // Q. 왜? static 메서드는 인스턴스 멤버를 쓸 수 없나요? - 인스턴스 멤버는 iv와 im이다. static 메서드 호출시 객체(iv묶음)가 없을 수도 있어서




}
