class MyPoint {
    int x;
    int y;
}

// 1. 상속으로 하는 경우
//class Circle extends MyPoint {  // 상속
//    int r;
//}

// 2. 포함으로 하는 경우
class Circle {
//    MyPoint p;  // 틀린 예시 - 참조변수 선언만 해놓고 초기화를 안 한 경우
    MyPoint p = new MyPoint();      // 참조변수의 초기화
    int r;
}
public class _46_클래스_간의_관계_상속과_포함_예제 {
    public static void main(String[] args) {
        Circle c = new Circle();
//        c.x = 1;    // 상속
//        c.y = 2;    // 상속
//        c.r = 3;
//        System.out.println("c.x = "+c.x);
//        System.out.println("c.y = "+c.y);
//        System.out.println("c.r = "+c.r);

        c.p.x = 1;  // 포함
        c.p.y = 2;  // 포함
        c.r = 3;
        System.out.println("c.p.x = "+c.p.x);
        System.out.println("c.p.y = "+c.p.y);
        System.out.println("c.r = "+c.r);


    }
}
