class MyPoint2  extends Object{
    int x;
    int y;
}

class Circle2  extends Object{      // 부모가 없으면 컴파일러할 때 자동적으로 Object를 상속
    MyPoint2 p; // = new MyPoint2();
    int r;

    Circle2() {
        p = new MyPoint2();
    }
}
public class _47_단일상속_예제 {
    public static void main(String[] args) {
        Circle2 c = new Circle2();
        System.out.println(c.toString());   // "Circle2@4f3f5b24"
        System.out.println(c);              // "Circle2@4f3f5b24"

    }
}
