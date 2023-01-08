public class _57_참조변수의_형변환_2 {
    public static void main(String[] args) {
        Car2 car = null;
        FireEngine fe = new FireEngine();
        FireEngine fe2 = null;      // 실제 인스턴스가 무엇인지가 중요.

        fe.water();
        car = fe;   // car = (Car2)fe; 형변환이 생략됨
//        car.water();
        fe2 = (FireEngine)car;  // 자손타입 ← 조상타입. 형변환 생략불가 - 작은거에서 큰거로
        fe2.water();

        Car2 car2 = (Car2)fe2;  // 자손 → 조상
        car2.drive();   // NullPointerException 발생
    }
}

class Car2 {    // 멤버 4
    String color;
    int door;

    void drive() {  // 운전하는 기능
        System.out.println("drive, Brrr~");
    }

    void stop() {   // 멈추는 기능
        System.out.println("stop!!!");
    }
}

class FireEngine extends Car2 { //멤버 5(부모4 + 1)
    void water() {System.out.println("water!!!");}
}

