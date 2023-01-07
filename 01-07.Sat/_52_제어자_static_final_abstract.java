public class _52_제어자_static_final_abstract {
    public static void main(String[] args) {
//ch7-17 제어자(modifier)
        // - 클래스와 클래스의 멤버(멤버 변수, 메서드)에 부가적인 의미 부여 == 영어의 형용사

        // 접근 제어자: public, protected, (default), private
        // 그 외: static, final, absract, native, transient, synchronized, volatile, strictfp

        // - 하나의 대상에 여러 제어자를 같이 사용가능(접근 제어자는 하나만)
            // ex. public static final int WIDTH = 200;    보통 접근 제어자를 제일 왼쪽에

//ch7-18 static - 클래스의, 공통적인
        // static:
            // - 멤버변수
                //◦ 모든 인스턴스에 공통적으로 사용되는 클래스 변수가 된다.
                //◦ 클래스 변수는 인스턴스를 생성하지 않고도 사용 가능하다.
                //◦ 클래스가 메모리에 로드될 때 생성된다.

        // - 메서드
            //◦ 인스턴스를 생성하지 않고도 호출이 가능한 static 메서드가 된다.
            //◦ static 메서드 내에서는 인스턴스멤버들을 직접 사용할 수 없다.

    }
}

class StaticTest {
    static int width = 200;     // 클래스 변수(static 변수)
//                   = 간단한 초기화
    static int height = 120;    // 클래스 변수(static 변수)

    static {    // 클래스 초기화 블럭 - static {}
        // static 변수의 복잡한 초기화 수행
    }

    static int max(int a , int b) { // 클래스 메서드(static 메서드)
        return a > b ? a:b;         // iv 사용 불가, instance method 사용 불가
    }
}
//====================================================================================

//ch7-19 final - 마지막의, 변경될 수 없는
    // final
        // - 클래스: 변경될 수 없는 클래스, 확장될 수 없는 클래스가 된다.
        // - 메서드: 변경될 수 없는 메서드, final로 지정된 메서드는 오버라이딩을 통해 재정의 될 수 없다.
        // - 멤버변수: 변수 앞에 final이 붙으면, 값을 변경할 수 없는 상수가 된다.
        // - 지역변수:  ''

final class FianlTest {         // 조상이 될 수 없는 클래스
    final int MAX_SIZE = 10;    // 값을 변경할 수 없는 멤버변수(상수)

    final void getMaxSize() {       // 오버라이딩할 수 없는 메서드(변경불가)
        final int LV = MAX_SIZE;    // 값을 변경할 수 없는 지역변수(상수)
//        return MAX_SIZE;
    }
}

//=======================================================================================================================

//ch7-20 abstract - 추상의, 미완성의
    // abstract
        // 클래스: 클래스 내에 추상 메서드가 선언되어 있음을 의미한다.
        // 메서드: 선언부만 작성하고 구현부는 작성하지 않은 추상 메서드임을 알린다.

abstract class AbstractTest {   // 추상 클래스(추상 메서드를 포함한 클래스) == 미완성 클래스(미완성 설계도, 제품 생성 불가)
    abstract void move();       // 추상 메서드(구현부{}가 없는 메서드) - 미완성 메서드
}
// AbstractTest a = new AbstractTest(); // 에러. 추상 클래스의 인스턴스 생성불가

// 완전한 클래스(완성된 설계도) == 구상 클래스


