public class _39_기본형매개변수_참조형매개변수_참조형_반환타입 {
    public static void main(String[] args) {
//ch6-23 기본형 매개변수
        // ▶ 기본형 매개변수 - 변수의 값을 읽기만 할 수 있다.(read only)
        // ▶ 참조형 매개변수 - 변수의 값을 읽고 변경할 수 있다.(read & write)


        /*
        기본형 매개변수

        class Data { int x; }

        class Ex6_6 {
            public static void main(String[] args) {
            Data d = new Data();
            d.x = 10;
            System.out.println("main(): x=" + d.x);     // (1). main() : x = 10

            change(d.x);
            System.out.println("After change(d.x)");    // (3). After change(d.x)
            System.out.println("main() : x = " + d.x);  // (4). main() : x = 10
        }

        static void change(int x) { // !!!기본형 매개변수!!!
            x = 1000;
            System.out.println("change() : x = " + x);  // (2). change() : x = 1000
        }
    }
        */

//============================================================================================
        /*
        참조형 매개변수 - 객체를 다룰 수 있는 리모컨을 통째로 준 것

        class Data2 { int x; }

        class Ex6_7 {
            public static void main(String[] args) {
                Data2 d = new Data2();
                d.x = 10;
                System.out.println("main() : x = " + d.x);      // (1). main() : x = 10

                change(d);
                System.out.println("After change(d)");          // (3). After change(d.x)
                System.out.println("main(0 : x = " + d.x);      // (4). main() : x = 1000
            }

            static void change(Data2 d) {   // !!!!!참조형 개매변수!!!!!!!
                d.x = 1000;
                System.out.println("change() : x = " + d.x);`   // (2). change() : x = 1000
            }
        }
        */
//====================================================================================================

// ch6-25 참조형 반환타입

        /*
        참조형 반환 타입

        class Data3 { int x; }

        class Ex6_8 {
            public static void main(String[] args)
                Data3 d = new Data3();
                d.x = 10;

                Data3 d2 = copy(d);
                System.out.println("d.x = " + d.x);     // (1). d.x = 10
                System.out.println("d2.x = " + d2.x);   // (2). d2.x = 10
            }

            static Data3 copy(Data3 d) {    // 같은 클래스 내부인 경우 참조변수 생략가능  / static 메서드는 객체 생성 없이 호출 가능
                Data3 tmp = new Data3();    // 새로운 객체 tmp를 생성한다.

                tmp.x  = d.x;               // d.x의 값을 tmp.x에 복사한다.

                return tmp;                 // 복사한 객체의 주소를 반환한다.
            }
        }
        */




    }
}
