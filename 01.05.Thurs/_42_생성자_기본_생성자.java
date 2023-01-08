class _42_생성자_기본_생성자 {
    public static void main(String[] args) {
// ch6-32 생성자(constructor) == iv 초기화 메서드
        // - 인스턴스가 생성될 때마다 호출되는 '인스턴스 초기화 메서드'
        // 객체(iv 묶음) 즉, iv초기화 메서드

        /*
        Time t  = new Time();   (1). 객체 생성
        t.hour = 12;            (2).
        t.minute = 34;          (2). iv 초기화
        t.second = 56;          (2).
              ↓
        Time t = new Time(12, 34, 56);
                       생성자 호출
        */



        // 규칙:
                // - 이름이 클래스 이름과 같아야한다.
                // - 리턴값이 없다.(void 안 붙임)
                // - 모든 클래스는 반드시 생성자(1+)를 가져야한다.

        // Card c = new Card();
        //           기본생성자 + 생성자 호출
//============================================================================================================

// ch6-33 기본 생성자(default constructor)
        // 매개변수가 없는 생성자
        // 생성자가 하나도 없을 떄만, 컴파일러가 자동 추가

        // 클래스이름() {}        기본 생성자
        // point() {}           Point클래스의 기본 생성자
//============================================================================================================

// 예시
        Data_1 d1 = new Data_1();
//        Data_2 d2 = new Data_2();   // compile error 발생 => 참조(1) 넣어줘야 에러 사라짐

    }
}

class Data_1 {
    int value;
}

class Data_2{
    int value;

// 참조(1)   Data_2() {} // 기본 생성자
    Data_2(int x) {     // 매개변수가 있는 생성자.
        value = x;
    }
}

//============================================================================================================

// ch6-34 매개변수가 있는 생성자

class Car {
    String color;       // 색상
    String gearType;    // 변속기 종류 - auto(자동), manual(수동)
    int door;           // 문의 개수

    Car() {}            // 기본 생성자
    Car(String c, String g, int d) {    // 매개변수가 있는 생성자
        color = c;
        gearType = g;
        door = d;
    }
}

/*
Car c = new Car();                  대입
c.color = "white";                  (4)
c.gearType = "auto";    =>     Car c = new Car ("white", "auto", 4);
c.door = 4;                     (1)     (2)         (3)
                             참조변수 c  객체생성    객체 초기화(생성자 호출 == iv 초기화)
*/
