class A{
    public void method(B b) {}// <A가 B대신 C를 사용하려면 두 곳 수정해야함>
    public void method(I i) {   // 인터페이스 I를 구현한 넘듦나 들어와라
        i.method();
    }
}

// B 클래스의 선언과 구현을 분리
interface I {
    public void method();   // method()의 선언
}
class B implements I{
    public void method() {                      // method()의 구현
        System.out.println("B클래스의 메서드");
    }
}

class C implements I{
    public void method() {
        System.out.println("C클래스의 메서드");
    }
}

public class _65_인터페이스의_장점1_예제 {
    public static void main(String[] args) {
        A a = new A();
        a.method(new B());  // A가 B를 사용(의존), <A가 B대신 C를 사용하려면 두 곳 수정해야함>


    }
}
