public class _51_import문_static_import문 {
    public static void main(String[] args) {
//ch7-15 import문
        // - 클래스를 사용할 때 패키지 이름을 생략할 수 있다.
        // - java.lang 패키지의 클래스는 improt하지 않고도 사용할 수 있다.
            // - String, Object, System, Thread ....
            // import java.lang. *; (*생략가능)

        // - import문을 선언하는 방법은 다음과 같다.
        /*
        import 패키지명.클래스명;
                혹은
        import 패키지명 *;

        - import문은 패키지문과 클래스선언 사이에 선언한다.
        - import문은 컴파일 시에 처리되므로 프로그램의 성능에 영향없음.
        */

//ch7-16 static import문
        // - static멤버를 사용할 때 클래스 이름을 생략할 수 있게 해준다.
        /*
        import static java.lang.Integer.*;   // Integer클래스의 모든 static 메서드
        import static java.lang.Math.random; // Math.random()만. 괄호 안 붙임
        import static java.lang.System.oit;  // System.out을 out만으로 참조가능

        System.out.println(Math.random());    =>    out.println(random());



        */



    }
}
