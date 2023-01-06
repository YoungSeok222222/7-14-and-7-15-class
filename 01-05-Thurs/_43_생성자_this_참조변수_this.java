public class _43_생성자_this_참조변수_this {
    public static void main(String[] args) {
// ch6-36 생성자 this()
        // - 생성자에서 다른 생성자 호출할 때 사용
        // - 다른 생성자 호출시 첫 줄에서만 사용가능!!!!!!!!   =>  두번째 줄에서 호출 시 에러 발생

// 생성자가 하는 일은 iv 초기화


/*
class Car {
    String color;
    String gearType;
    int door;

   *코드의 중복이 있는 나쁜 코드          *코드의 중복을 제거한 코드
    Car() {                             Car() {
        color = "white";                    // Car("white", "auto", 4);
        gearType = "auto";      =>          this("white", "auto", 4);
        door = 4;
    }

    Car (String c, String g, int d) {
         color = c;
         gearType = g;
         door = d;
    }
}
*/

//============================================================================================

// ch6-37 참조변수 this
        // - 인스턴스 자신을 가리키는 참조변수
        // - 인스턴스 메서드(생성자 포함)에서 사용가능
        // - 지역변수(lv)와 인스턴스 변수(iv)를 구별할 때 사용

        /*
        Car(String c, String g, int d) {             Car(String color, String gearType, int door) {
            // color는 iv, c는 lv                         // this.color는 iv, color는 lv
            color = c;                                   this.color = color;
            gearType = g;                        =>      this.gearType = gearType;
            door = d;                                    this.door = door;0
        }                                            }      (iv)     (lv)   this없으면 이름이 동일하기 때문에 둘다 lv로 인식
        */






/* <정리>
생성자 this()
-생성자에서 다른 생성자 호출할 때 사용
-다른생성자 호출 시 첫 줄에서만 사용가능
-코드중복 제거하기 위해 생성자들끼리 서로 호출을 많이함
이때 클래스 이름을 쓰지않고 this()를 사용하는 것.
-생성자들이 하는 일: iv초기화

참조변수 this
-인스턴스 자신을 가르키는 참조변수
-인스턴스 메서드(생성자 포함)에서만 선언없이 사용가능
-지역변수와 인스턴스를 구별할 때 사용
lv와 iv의 이름이 같을 시, this가 없으면 iv도 lv로 취급됨(lv가 가까우므로)
-lv와 iv의 이름이 다를경우 같은클래스 안이여서 참조변수 생략가능함
-단, static메서드에서는 사용불가. iv, this가 존재할 수 없음

참조변수 this VS 생성자 this() ...이 두개 연관짓지 마. 비슷하게 생겼을 뿐 완전 다른것
-this : 선언 없이 사용가능. 인스턴스 자신을 가르키는 참조변수. 객체 주소가 저장
-this() : 생성자(메서드). 같은 클래스의 다른 생성자를 호출할 때 사용. 클래스 이름대신 this()사용






*/




    }
}
