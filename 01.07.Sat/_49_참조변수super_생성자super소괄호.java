public class _49_참조변수super_생성자super소괄호 {
    public static void main(String[] args) {
//ch7-10 참조변수 super
        // - 객체 자신을 가리키는 참조변수. 인스턴스 메서드(생성자)내에만 존재
        // - 조상의 멤버를 자신의 멤버와 구별할 때 사용

        Child c = new Child();      // 예제 1
        c.method();

        Child2 c2 = new Child2();   // 예제 2
        c2.method();
    }
}

// 예제 1
class Parent {int x = 10;}  // super.x (조상멤버)
class Child extends Parent {
    int x = 20;             // this.x (자기 멤버)

    void method() {
        System.out.println("x= " + x);              // 20
        System.out.println("this.x= " + this.x);    // 20
        System.out.println("super.x= " + super.x);  // 10
    }
}

// 예제 2
class Parent2 { int x = 10; }   // super.x와 this.x 둘 다 가능

class Child2 extends Parent2 {
    void method() {
        System.out.println("x= " + x);              // 10
        System.out.println("this.x= " + this.x);    // 10
        System.out.println("super.x= " + super.x);  // 10
    }
}

//ch7-11 super() - 조상의 생성자
    // - 조상의 생성자를 호출 할 때 사용
    // - 조상의 멤버는 조상의 생성자를 호출해서 초기화 - 생성자, 초기화블럭은 상속이 안 된다.


class Point {
    int x, y;

    Point (int x, int y) {
        this.x = x;
        this.y = y;
    }
}


//class Point3D extends Point {
//    int z;
//
//    Point3D(int x, int y, int z) {
//        this.x = x;     // 조상의 멤버를 초기화
//        this.y = y;     // 조상의 멤버를 초기화
//        this.z = z;
//
//        super(x,y);     // 조상클래스의 생성자 Point(int x, int y)를 호출
//        this.z = z;     // 자신의 멤버를 초기화
//    }
//}

//7-11 super() - 조상의 생성자
    // - 생성자의 첫 줄에 반드시 생성자를 호출해야 한다.
    // 그렇지 않으면 컴파일러가 생성자의 첫줄에 super()을 삽입.

//class Point2 {                            class Point extends Object {
//    int x;                                    int x;
//    int y;                                    int y;
//
//    Point2() {                  // =>         Point() {
//        this(0,0);                                this(0,0);
//    }                                         }
//    Point2 (int x, int y) {                   Point(int x, int y) {
//        this.x = x;                               super() // Object();
//        this.y = y;                               this.x = x;
//    }                                             this.y = y;
//}                                             }


//=======================================================================================================================
/*

 super : 객체 자신을 가리키는 참조변수, 인스턴스 메서드 내에만 존재, 조상의 멤버를 자신의 멤버와 구분시 사용
- super() : 조상의 생성자, 조상의 생성자 호출 시 사용(조상의 멤버는 조상의 생성자를 호출해서 초기화)
* 생성자의 첫 줄에 반드시 생성자를 호출해야 함
* 그렇지 않으면 컴파일러가 자동으로 첫 줄에 super() 삽입

*/