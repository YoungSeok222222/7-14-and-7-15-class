public class _58_instanceof_연산자 {
    public static void main(String[] args) {
//ch7-26 instanceof 연산자
        // - 참조변수의 형변환 가능여부 확인에 사용, 가능하면 true 반환 (조상 ↔ 자손)
        // - 형변환 전에 반드시 instanceof로 확인해야 함

        // 1. 형변환이 가능한지 확인
        // 2. 형변환

        /*
        FireEngine fe = new FireEngine();
        System.out.println(fe instanceof Object);       // true
        System.out.println(fe instanceof Car);          // true
        System.out.println(fe instanceof FireEngine);   // true

        Object obj = (Object)fe;        // OK
        Car     c  = (Car)fe;           // Ok
        */

// Q. 참조변수의 형변환은 왜 하나요?
// A. 참조변수(리모콘)을 변경함으로써 사용할 수 있는 멤버의 갯수를 조절하기 위해서

// Q. instanceof 연산자는 언제 사용하나요?
// A. 참조변수를 형변환하기 전에 형변환 가능여부를 확인할 때



    }
}
