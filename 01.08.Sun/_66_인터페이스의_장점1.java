public class _66_인터페이스의_장점1 {
    public static void main(String[] args) {
//ch7-39 인터페이스의 장점
        // - 두 대상(객체) 간의 '연결, 대화, 소통'을 돕는 '중간 역할'을 한다.
        // - 선언(설계)와 구현을 분리시킬 수 있게 한다.
            // 껍데기    알맹이

        // - 인터페이스 덕분에 B가 변경되어도 A는 안 바꿀 수 있게 된다.(느슨한 결합)

        // ▶ 직접적인 관계의 두 클래스(A-B)                            ▶ 간접적인 관계의 두 클래스 (A-I-B)
            /*
            class A {                                                class A {
                  public void methodA(B b) {                                public void method(I,i) {
                        b.methodB();                                              i.methodB();
                  }                                                         }
            }                                                        }

            class B {                                                interface I { void methodB(); }
                  public void methodB() {
                        System.out.println("methodB()");             class B implements I {
                  }                                                        public void methodB() {
            }                                                                     System.out.println("methodB()");
                                                                           }
            class InterfaceTest {                                    }
                  public static void main(String args[]) {
                        A a = new A();
                        a.methodA(new B());
                  }
            }
            */

    }
}
