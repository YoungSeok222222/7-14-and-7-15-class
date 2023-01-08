public class _56_참조변수의_형변환_1 {
    public static void main(String[] args) {
//ch7-24 참조변수의 형변환
        // - 사용할 수 있는 멤버의 갯수를 조절하는 것
        // - 조상 자손 관계의 참조변수는 서로 형변환 가능

/*
class Car {                                         class FireEngine extends Car {  // 소방차
    String color;                                       void water() {  // 물을 뿌리는 기능
    int door;                                               System.out.println("water!!!");
                                                        }
    void drive() {                                  }
        System.out.println("drive, Brrr~");
    }

    void stop () {
        System.out.println("Stop!");
    }
}

FireEngine f = new FireEngine();

Car c = (Car)f;                 // OK. 조상인 Car 타입으로 형변환(생략가능)
FireEngine f2 = (FireEngine)c;  // OK. 자손인 FireEngine타입으로 형변환(생략불가)
Ambulance a = (Ambulance)f;     // 에러. 상속관계가 아닌 클래스 간의 형변환 불가

5개 -> 4개  감소(안전)
4개 -> 5개  증가(안전X)

*/

    }
}
