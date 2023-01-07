class MyPoint3{
    int x;
    int y;

//    MyPoint3(int x, int y) {      (2)번 방법
//        this.x = x;
//        this.y = y;
//    }
    String getLocation() {
        return "x:" + x + ", y:" + y;
    }

    public String toString() {
        return "x:" + x + ", y:" + y;
    }
}

class MyPoint3D extends MyPoint3 {
    int z;

    // 조상의 getLocation()을 오버라이딩
    String getLocation() {return "x:" + x + ", y:" + y + ", z:" + z;}

    // Object클래스의 toString()을 오버라이딩

}
public class _48_오버로딩_vs_오버라이딩 {
    public static void main(String[] args) {
// ch7-7 오버라이딩(overriding)
        // - 상속받은 조상의 메서드를 자신에 맞게 변경하는 것

        MyPoint3D p  = new MyPoint3D();
        p.x = 3;
        p.y = 5;
        p.z = 7;

        System.out.println(p.getLocation());

        MyPoint3 p2 = new MyPoint3();
        p2.x = 33;
        p2.y = 55;
//      MyPoint3 p2  = new MyPoint3(33, 55); (2)번 방법
//      System.out.println(p);

//        System.out.println("p2.x = " + p2.x);
//        System.out.println("p2.y = " + p2.y);
        System.out.println(p2.toString());
        System.out.println(p2);     // 바로 위 출력 코드와 동일

//========================================================================================================================

//ch7-8 오버라이딩의 조건
    // 1. 선언부가 조상 클래스의 메서드와 일치해야 한다.
    // 2. 접근 제어자를 조상 클래스의 메서드보다 좋은 범위로 변경할 수 없다.  (public, protected, default, private)
    // 3. 예외는 조상 클래스의 메서드보다 많이 선언할 수 없다.



//ch7-9 오버로딩 vs 오버라이딩
        // 오버로딩(overloading) - 기존에 없는 새로운 메서드를 정의하는 것(new)
        // 오버라이딩(overriding) - 상속받은 메서드의 내용을 변경하는 것(change, modify)



/*
class Parent {
    void parentMethod() {}
}

class Child extends Parent {
     void parentMethod() {}         오버라이딩
     void parentMethod(int i) {}    오버로딩

     void childMethod() {}          메서드 정의
     void childMethod(int i) {}     오버로딩 - 이름만 같은 메서드를 새로 만듬
     void childMethod() {}          중복정의(에러)
}




*/


    }
}
