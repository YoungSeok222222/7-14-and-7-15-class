// 다형성
    // 1. Tv t = new SmartTv(); 조상 - 자손
    // 2. 참조변수의 형변환 - 리모콘 바꾸기(사용가능한 멤버 갯수 조절)
    // 3. instanceof 연산자 - 형변환 가능여부 확인

public class _59_매개변수다형성 {
    public static void main(String[] args) {
//ch7-27 매개변수의 다형성
        // - 참조형 매개변수는 메서드 호출시, 자신과 같은 타입 또는 자손타입의 인스턴스를 넘겨줄 수 있다.



// 매개변수 다형성의 장점:
        // 1. 다형적 매개변수
        // 2. 하나의 배열로 여러 종류 객체 다루기

        Buyer b = new Buyer();

        b.buy(new Tv1());
        b.buy(new Computer());

        System.out.println("현재 남은 돈은" + b.money + "만원입니다.");
        System.out.println("현재 보너스점수는" + b.bonusPoint + "점입니다.");

    }
}

class Product {
    int price;      // 제품의 가격

    int bonusPoint; // 제품구매 시 제공하는 보너스점수

    Product(int price) {
        this.price = price;
        bonusPoint = (int)(price/10.0); // 보너스점수는 제품가격의 10%
    }
}

class Tv1 extends Product {
    Tv1() {
        // 조상 클래스의 생성자 Product(int price)를 호출한다.
        super(100);     // Tv의 가격을 100만원으로 한다.
    }

    // Object클래스의 toString()을 오버라이딩한다.
    public String toString() { return "Tv"; }
}

class Computer extends Product {
    Computer() { super(200); }

    public String toString() { return "Computer"; }
}
class Buyer {   // 고객, 물건을 사는 사람
    int money = 1000;       // 소유금액
    int bonusPoint = 0;     // 보너스 점수

    void buy(Product p) {
        if (money < p.price) {
            System.out.println("잔액이 부족하여 물건을 살 수 없습니다.");
            return;
        }
        money -= p.price;   // 가진 돈에서 구입한 제품의 가격을 뺀다.
        bonusPoint += p.bonusPoint; // 제품의 보너스 점수를 추가한다.
        System.out.println(p+"을/를 구입하셨습니다.");

    }

}