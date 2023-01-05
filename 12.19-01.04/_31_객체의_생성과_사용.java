public class _31_객체의_생성과_사용 {
    public static void main(String[] args) {


// ch6-6 객체의 생성과 사용
        /*
        1. 객체의 생성
        클래스명 변수명;           // 클래스의 객체를 참조하기 위한 참조변수를 선언
        변수명  = new 클래스명();  // 클래스의 객체를 생성 후, 객체의 주소를 참조변수에 저장

        Tv t;                   // Tv클래스 타입의 참조변수 t를 선언
        t = new Tv();           // Tv인스턴스를 생성한 후, 생성된 Tv인스턴스의 주소를 t에 저장

        Tv t = new Tv();


        2. 객체의 사용(변수와 메서드 사용 방법)
        t.channel = 7;          // Tv인스턴스의 멤버변수 channel의 값을 7로 한다.
        t.channelDown();        // Tv인스턴스의 메서드 channelDown()을 호출한다.

        system.out.println("현재 채널은" + t.channel + "입니다.");
        */
        
    }
class Tv {                  // 1. 클래스 작성
        String color;   // 색깔
        boolean power;  // 전원상태
        int channel;    // 채널

        void channel() {};
        void channelDown() {channel --;}

//        Tv t = new Tv();    // 2. 객체 생성

//        t.channel = 7;      // 3. 객체 사용(변수, 메서드)
//        t.channelDown()     // Tv인스턴스의 메서드 channelDown()을 호출한다.
//    System.out.println("현재 채널은" + t.channel + "입니다.")
//============================================================================

        // ch6-7 객체의 생성과 사용
        Tv t1 = new Tv();
        Tv t2 = new Tv();
//        t1.channel = 7;


        // (a) 하나의 인스턴스(객체)를 여러 개의 참조변수가 가리키는 경우(가능)
        //        t2 = t1;
        //        t1.channel = 7;   / t2는 t1이 가리키는 객체와 연결됨
        // (b) 여러 인스턴스를 하나의 참조변수가 가리키는 경우(불가능)
    }

}
