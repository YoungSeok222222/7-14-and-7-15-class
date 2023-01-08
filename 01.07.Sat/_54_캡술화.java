//예제 1
class Time {
    private int hour;   // 0~23사이의 값을 가져야 함
    private int minute;
    private int second;

    public void setHour(int hour) {
        if (isNotValidHour(hour)) return;  // alt + shift + m: 메서드 추출
        this.hour = hour;
    }

    // 매개변수로 넘겨진 hour가 유효한지 확인해서 알려주는 메서드
    private  boolean isNotValidHour(int hour) {
        return hour < 0 || hour > 23;
    }

    public int getHour() { return hour; }
}
public class _54_캡술화 {
    public static void main(String[] args) {
//ch7-22 캡슐화와 접근 제어자
        // 접근 제어자를 사용하는 이유
            // - 외부로부터 데이터를 보호하기 위해서
                // 직접 접근은 막고, method를 통한 간접접근은 허용
            // - 외부에는 불필요한, 내부적으로만 사용되는, 부분을 감추기 위해서


//예제 1
        Time t = new Time();
//        t.hour = 25;
        t.setHour(21);  // hour의 값을 21로 변경
        System.out.println(t.getHour());
        t.setHour(100); // hour의 범위를 벗어나기 때문에 if문에 걸려 변경되지 않음
        System.out.println(t.getHour());








    }
}
