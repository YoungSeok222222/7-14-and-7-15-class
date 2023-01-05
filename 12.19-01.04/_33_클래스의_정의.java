public class _33_클래스의_정의 {
    public static void main(String[] args) {
        // 클래스 = 1). 설계도 2). 데이터 + 함수 3). 사용자 정의 타입

        // 클래스 == 데이터 + 함수

        // 1.변수: 하나의 데이터를 저장할 수 있는 공간
        // 2.배열: 같은 종류의 여러 데이터를 하나로 저장할 수 있는 공간
        // 3.구조체: 서로 관련된 여러 데이터(종류 관계X)를 하나로 저장할 수 있는 공간
        // 4.클래스: 데이터와 함수의 결합(구조체 + 함수)


//ch6-10 클래스의 정의(2)
        // 사용자 정의 타입 - 원하는 타입을 직접 만들 수 있다.

        /*
        (1) 시,분,초 하나씩 만드는 경우
        int hour;
        int minute;
        int second;

        (2)시,분,초 각 3개씩 만드는 경우
        int hour1, hour2, hour3;
        int minute1, minute2, minute3;
        int second1, second2, second3;

        (3) 각 객체배열로 만드는?
        int[] hour = new int[3];
        int[] minute = new int[3];
        int[] second = new int[3];

                    ↓

        클래스로 선언해서 하는 경우
        class Time {
            int hour;
            int minute;
            int second;
        }
        (1-1)
        Time t = new Time();

        (2-1)
        Time t1 = new Time();
        Time t2 = new Time():
        Time t3 = new Time();

        (3-1)
        Time[] t = new Time[3];
        t[0] = new TIme();
        t[1] = new TIme();
        t[2] = new TIme();
        */

    }
}
