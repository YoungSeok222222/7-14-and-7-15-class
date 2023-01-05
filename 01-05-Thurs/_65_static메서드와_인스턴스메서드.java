public class _65_static메서드와_인스턴스메서드 {
    public static void main(String[] args) {


        // 메서드 == 명령문 집합
        // 공통 속성인 변수 => static을 붙이는 변수
        // iv를 사용하지 않는 메서드 => static을 붙이는 메서드

//ch6-29 메서드 간의 호출과 참조

        // ▶ static 메서드는 인스턴스 변수(iv)를 사용할 수 없다.

        class TestClass2 {
            int iv;          // 인스턴스 메서드
            static int cv;   // 클래스 변수

            void instanceMethod() {         // 인스턴스 메서드 => 이미 객체가 생성됐다.(객체가 있어야 호출 가능)
                System.out.println(iv);     // 인스턴스 변수를 사용할 수 있다.
                System.out.println(cv);     // 클래스 변수를 사용할 수 있다.(언제든 사용가능)
            }

            static void staticMethod() {    // static 메서드 => 객체 여부와 상관없이 항상 호출 가능
//                System.out.println(iv);     // 에러!! 인스턴스 변수를 사용할 수 없다.
                System.out.println(cv);     // 클래스 변수는 사용할 수 있다.

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
}
