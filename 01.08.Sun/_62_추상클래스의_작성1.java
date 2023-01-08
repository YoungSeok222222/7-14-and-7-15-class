public class _62_추상클래스의_작성1 {
    public static void main(String[] args) {
//ch7-34 추상클래스의 작성
        // - 여러 클래스에 공통적으로 사용될 수 있는 추상클래스를 바로 작성하거나 기존클래스의 공통 부분을 뽑아서 추상클래스를 만든다.
        // 객체배열이란? 참조변수를 묶어놓은것

        Unit[] group = { new Marine(), new Tank(), new Dropship()}; // 배열의 생성과 초기화를 한 번에
//        Unit[] group = new Unit[3];   // 바로 위 1줄짜리 코드와 동일
//        group[0] = new Marine();
//        group[1] = new Tank();
//        group[2] = new Dropship();
//        Object[] group = new Object[3]; // 에러

        for (int i = 0; i < group.length; i++)
            group[i].move(100, 200);
    }
}
abstract class Unit {
    int x,y;
    abstract void move(int x, int y);
    void stop() {/* 현재 위치에 정지 */}
}

class Marine extends Unit { // 보병
    void move(int x, int y) { System.out.println("Marine[x=" + x + ", y=" + y + "]"); }
    void stimPack() {/* 스팀팩을 상ㅇ한다. */}
}

class Tank extends Unit {   // 탱크
    void move (int x, int y) { System.out.println("Tank[x=" + x + ", y=" + y + "]"); }
    void changeMode() {/* 공격모드를 변환한다. */}
}

class Dropship extends Unit {
    void move(int x, int y) { System.out.println("Dropship[x=" +x + ", y=" + y + "]"); }
    void load() {/**/}
    void unload() {/**/}
}