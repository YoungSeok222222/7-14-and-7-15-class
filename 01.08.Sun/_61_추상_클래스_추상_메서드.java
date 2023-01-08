public class _61_추상_클래스_추상_메서드 {
    public static void main(String[] args) {
//ch7-31 추상 클래스 (abstract class)
        // - 미완성 설계도. 미완성 메서드를 갖고 있는 클래스
        // - 미완성 메서드. 구현부(몸통{})가 없는 메서드
            // 추상메서드: 꼭 필요하지만 자손마다 다르게 구현될 것으로 예상되는 경우

        abstract class Player { // 추상클래스(미완성클래스)
            abstract void play (int pos);   // 추상메서드(몸통{}이 없는 미완성 메서드)
            abstract void stop();           // 추상메서드 == 미완성메서드
        }


        // - 다른 클래스 작성에 도움을 주기 위한 것. 인스턴스 생성 불가.

            // Player p = new Player();     // 에러. 추상 클래스의 인스턴스 생성 불가

        // - 상속을 통해 추상 메서드를 완성해야 인스턴스 생성가능

            /*
            class Audio extends Player{
                void play(int pos) { ... }  // 추상메서드를 구현
                void stop() { ... }         // 추상메서드를 구현
            }

            AudioPlayer ap = new AudioPlayer();   // OK.
            */


        // - 추상 메서드 호출 가능(호출할 때는 선언부만 필요)
            abstract class Player2 {
                boolean pause;
                int currentPos;

                Player2() {
                    pause = false;
                    currentPos = 0;
                }
                // 지정된 위치(pos)에서 재생을 시작하는 기능이 수행하도록 작성되어야 한다.
                abstract void play (int pos);   // 추상 메서드
                // 재생을 즉시 멈추는 기능을 수행하도록 작성되어야 한다.
                abstract void stop();           // 추상 메서드

                void play() {
                    play(currentPos);           // 추상메서드를 사용할 수 있다. - 메서드는 선언부만 알면 호출가능하므로 추상메서드도 호출 가능!!!
                }
            }










    }
}
