abstract class Unit2 {
    int x, y;
    abstract void move(int x, int y);
    void stop(){
        System.out.println("멈춥니다.");
    }
}

interface Fightable {       // 인터페이스의 모든 메서드는 public abstract. 예외없이
    void move(int x, int y);    // public abstract가 생략됨
    void attack(Fightable f);   // public abstract가 생략됨
}

class Fighter extends Unit2 implements Fightable {
    // 오버라이딩 규칙: 조상(public)보다 접근제어자가 좁으면 안 된다.
    public void move(int x, int y) {
        System.out.println("[" + x + "," + y + "]로 이동");
    }
    public void attack(Fightable f) {
        System.out.println(f + "를 공격");
    }

    // 싸울 수 있는 상대를 불러온다.
    Fightable getFightable() {
        // (1)
        Fighter f = new Fighter();    // Fighter를 생성해서 반환
        return (Fightable)f;

        // (2)
//        Fightable f = new Fighter();
//        return f
    }
}

public class _65_인터페이스와_다형성_예제 {
    public static void main(String[] args) {
        Fighter f = new Fighter();
        f.move(100, 200);
        f.attack(new Fighter());

    }
}
