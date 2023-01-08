public class _65_인터페이스와_다형성 {
    public static void main(String[] args) {
//ch 7-38 인터페이스를 이용한 다형성
        // Tv t = new SmartTv();
        //조상참조변수   자손객체

        // - 인터페이스도 구현 클래스의 부모? Yes
        // - 인터페이스 타입 매개변수는 인터페이스 구현한 클래스의 객체만 가능


            /*
            class Fighter extends Unit implements Fightable {
                 public void move(int x, int y) { ... }
                 public void attack(Fightable f) { ... }
            }

            조상클래스          자손객체
            Unit      u = new Fighter();                interface Fightable {
            인터페이스                                          void move(int x, int y);
            Fightable f = new Fighter() ;                     void attack(Fightable f);
                                                        }                 인터페이스
                                                               Fightable 인터페이스를 구현한
            f.move(100, 200);                                  클래스의 인스턴스만 가능
            f.attack(new Fighter());
             */


        // - 인터페이스를 메서드의 리턴타입으로 지정할 수 있다.

        /*
        Fightable인터페이스를 구현한 클래스의 인스턴스를 반환
        Fightable method() {
              Fighter f = new Fighter();    두 문장을 한 문장으로 바꾸면 return new Fighter();
              return f;
        }

        class Figther extends Unit implements Fightable {
              public void move(int x, int y) { ... }
              public void attack(Fightable f) { ... }
        }
        */


    }
}
