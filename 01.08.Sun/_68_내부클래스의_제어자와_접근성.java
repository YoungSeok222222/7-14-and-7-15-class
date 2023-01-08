public class _68_내부클래스의_제어자와_접근성 {

//ch7-45 내부 클래스의 제어자와 접근성
        // ▶ 내부 클래스의 제어자는 변수에 사용 가능한 제어자와 동일


/*
class InstanceInner {
    int iv = 100;
    static int cv = 100;            // 에러! static변수를 선언할 수 없다.
    final static int CONST = 100;   // final static은 상수이므로 허용
}

static class StaticInner {
    int iv = 200;
    static int cv = 200;            // static클래스만 static 멤버를 정의할 수 있다. - 객체 생성 없이 사용 가능해야
}

void myMethod() {
    class LocalInner {
        int iv = 300;                   // 에러! static 변수를 선언할 수 없다.
        static int cv = 300;            // final static은 상수이므로 허용
        final static int CONST = 300;
    }
}

*/

    class InstanceInner {
        int iv = 100;
        static int cv = 100;                // 에러! static 변수를 선언할 수 없다.
        final static int CONST = 100;       // final static은 상수이므로 허용
    }

    static class StaticInner {
        int iv = 200;
        static int cv = 200;                // static 클래스만 static 멤버를 정의할 수 있다.
    }

    void myMethod() {
        class LocalInner {
            int iv = 300;
            static int cv = 300;            // 에러! static 변수를 선언할 수 없다.
            final static int CONST = 300;   // final static은 상수이므로 허용
        }
        int i = LocalInner.CONST;   // OK
    }

    public static void main(String[] args) {
        System.out.println(InstanceInner.CONST);
        System.out.println(StaticInner.cv);
//        System.out.println(LocalInner.CONST); // 에러. 지역 내부 클래스는 메서드 내에서만
    }


}

