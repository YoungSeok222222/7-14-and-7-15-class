public class _66_인터페이스의장점2 {
    public static void main(String[] args) {
//ch7-39 인터페이스의 장점
        // - 개발 시간을 단축할 수 있다.
        // - 변경에 유리한 유연한 설계가 가능하다.
        // - 표준화가 가능하다. (JDBC 인터페이스 집합)
        // - 서로 관계없는 클래스들을 관계를 맺어줄 수 있다.

        /*
(1)
void repair(Tank t) {
        // Tank를 수리한다.
}
(2)
void repair(Dropship d) {
        // Dropship을 수리한다.                      (1)과 (2)는 오버로딩(같은 이름의 메서드)
}

void repair(GroundUnit gu) {
        // 매개변수로 넘겨진 지상 유닛(GroundUnit)을 수리한다.
}

==============================================================================================================

interface Repairable {}
class SCV extends GroundUnit implement Repairable {
        ...
}

class Tank extends GroundUnit implement Repairable {
        ...
}

class Dropship extends AirUnit implement Repairable {
        ...
}
======================================================================================================================

void repair (Repairalbe r) {    // Repairalbe을 구현한 넘들(객체)만 가능
    if (r instanceof Unit) {
        Unit u = (Unit) r;
        while (u.hitPoint != u.Max_HP) {
                u.hitPoint++;   // Unit의 HP를 증가시킨다.
        }
    }
} // repair(Repairable r)


        */



    }
}
