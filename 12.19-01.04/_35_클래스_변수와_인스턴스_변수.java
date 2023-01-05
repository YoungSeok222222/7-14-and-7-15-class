public class _35_클래스_변수와_인스턴스_변수 {
    public static void main(String[] args) {
// ch6-12 클래스 변수와 인스턴스 변수

// 선언위치
        // 영역: 1) 클래스 영역: iv(인스턴스 변수), cv(클래스 변수)
        //      2) 메서드 영역: lv

        /*
        포커 카드를 예시로 들면

        속성
        ---------------------------------------------------------------
        무늬          개별적 - 객체마다 다르게 유지되어야 함  => iv(인스턴스 변수)
        숫자          개별적

        폭           공통적 - 모든 객체가 공통으로 가져야하는 경우=> cv(클래스 변수)
        높이          공통적
        */

class Card{
    String kind;        // 무늬 (개별 속성) iv
    int number;         // 숫자 (개별 속성) iv

    static int width = 100; // 폭 (공통 속성) cv
    static int height = 250; // 높이 (공통 속성) cv
}

        Card c = new Card();    // 객체 생성
        c.kind = "HEART";       // iv, 객체 사용
        c.number = 5;           // iv, 객체 사용
        c.width = 200;          // cv, 객체 사용
        c.height = 300;         // cv, 객체 사용, 사용은 가능하지만 아래와 같이 클래스이름이 붙어야함

        Card.width = 200;       // cv,
        Card.height = 300;

        System.out.println("Card.width = " + Card.width);
        System.out.println("Card.height = " + Card.height);

        Card c1 = new Card();
        c1.kind  = "Heart";
        c1.number = 7;

        Card c2 = new Card();
        c2.kind = "Spade";
        c2.number = 4;

        System.out.println("c1은" + c1.kind + ", " + c1.number + "이며, 크기는 ("+ c1.width + ","+ c1.height + ")");
        System.out.println("c2는" + c2.kind + ", " + c2.number + "이며, 크기는 (" + c2.width + "," + c2.height + ")");
        System.out.println("c1의 width와 height를 각각 50, 80으로 변경합니다.");

//        c1.width = 50;  // c1 것만 바꿔도 cv가 변경된다. 따라서 다음과 같이 Card.width와 Card.height로 작성해야 함
//        c1.height = 80;

        Card.width = 50;
        Card.height =80;

        System.out.println("c1은" + c1.kind + "," + c1.number + "이며, 크기는 (" + c1.width + "," + c1.height + ")");
        System.out.println("c2은" + c2.kind + "," + c2.number + "이며, 크기는 (" + c2.width + "," + c2.height + ")");








    }
}
