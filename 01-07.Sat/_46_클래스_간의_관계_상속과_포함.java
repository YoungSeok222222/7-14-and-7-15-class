 class _46_클래스_간의_관계_상속과_포함 {
    public static void main(String[] args) {
//ch7-3 포함 관계
        // ▶ 포함(composite)이란?
            // - 클래스의 멤버로 참조변수를 선언하는 것
            // 작은 단위의 클래스를 만들고, 이 둘을 조합해서 클래스를 만든다.

/*
class Point {
    int x;
    int y;
}

(1)번 방법                                   (2)번 방법 - Circle이 Point를 포함(관계)
class Circle {                              class Circle {
    int x;  // 원점의 x좌표                      Point c = new Point();  // 원점
    int y;  // 원점의 y좌표            =>        int r;  // 반지름(radius)
    int r;  // 반지름(radius)                }
}
*/

//================================================================================================

// ch7-4 클래스 간의 관계 결정하기

        // 상속관계 '~은 ~이다.(is-a)'
        // 포함관계 '~은 ~을 가지고 있다.(has-a)'

/*
class Point {
    int x;
    int y;
}

(포함관계 - 90%이상)                              (상속관계)
class Circle {                                  class Circle extends Point {
Point C = new Point();                               int r;
    int r;                                      }
}

원(Circle)은 점(Point)이다. - Circle is a Point (X)
원(Circle)은 점(Point)을 가지고 있다. - Circle has a Point (O)
*/

    }
}


