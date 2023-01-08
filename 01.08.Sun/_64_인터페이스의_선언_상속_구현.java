public class _64_인터페이스의_선언_상속_구현 {
    public static void main(String[] args) {
//ch7-35 인터페이스(interface) == 추상 메서드의 집합
    // - 구현된 것이 전혀 없는 설계도. 껍데기(모든 멤버가 public)

            /*
            interface 선언

            interface 인터페이스이름 {
                 public static final 타입 상수이름 = 값;   상수
                 public abstract 메서드이름(매개변수목록);   추상메서드
             }


             interface PlayingCard {
                  public static fianl int SPADE = 4;
                  final int DIAMOND = 3;                // public static final int DIAMOND = 3;
                  static int HEART = 2;                 // public static final int HEART = 2;
                  int CLOVER = 1;                       // public static final int CLOVER = 1;

                  public abstract String getCardNumber();
                  String getCardKind();                 // public abstract String getCardKind();
            }                                           // 생략가능 생략가능
            */


    // - 인터페이스의 조상은 인터페이스만 가능(Object가 최고 조상 아님)
    // - 다중 상속이 가능(추상메서드는 충돌해도 문제 없음)

            /*
            interface Fightable extends Movable, Attackable {}

            interface Movable {
                // 지정된 위치(x, y)로 이동하는 기능의 메서드
                void move(int x, int y);
            }

            interface Attackable {
                // 지정된 대상(u)을 공격하는 기능의 메서드
                void attack(Unit u);
            }
            */


    // - 인터페이스(미완성 설계도)에 정의된 추상 메서드를 완성하는 것

            /*
            class 클래스이름 implements 인터페이스이름 {
                  // 인터페이스에 정의된 추상메서드를 모두 구현해야 한다.
            }
            */


    // - 일부만 구현하는 경우, 클래스 앞에 abstract를 붙여야 함.
            /*
            abstract class Fighter implements Fightable {
                  public void move(int x, int y) { 내용 생략  }
            }
            */
//=================================================================================================

        // Q. 인터페이스란?
        // A. 추상 메서드의 집합, (상수, static메서드, 디폴트 메서드)

        // Q. 인터페이스의 구현이란?
        // A. 인터페이스의 추상메서드 몸통{} 만들기(미완성 설계도 완성하기)

        // Q. 추상 클래스와 인터페이스의 공통점은?
        // A. 추상 메서드를 가지고 있다.(미완성 설계도)

        // Q. 추상 클래스와 인터페이스의 차이점은?
        // A. 인터페이스는 iv를 가질 수 없다. => 추상 메서드 (+상수, static 메서드)만 가능


    }
}
