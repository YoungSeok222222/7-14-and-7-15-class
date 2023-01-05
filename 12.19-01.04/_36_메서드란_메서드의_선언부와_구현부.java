public class _36_메서드란_메서드의_선언부와_구현부 {
    public static void main(String[] args) {
//ch6-14 메서드(black box)란?
        // 1. 문장들을 작업단위로 묶어놓은 것
        // - 작업단위로 문장들을 묶어서 이름 붙인 것

        // 2. 값(입력)을 받아서 처리하고, 결과를 반환(출력)

        // ▶ 메서드의 장점
        // - 코드의 중복을 줄일 수 있다.
        // - 코드의 관리가 쉽다.
        // - 코드를 재사용할 수 있다.
        // - 코드가 간결해서 이해하기 쉬워진다.

        // ▶ 메서드의 작성
        // - 반복적으로 수행되는 여러 문장을 메서드로 작성
        // - 하나의 메서드는 한 가지 기능만 수행하도록 작성


        // 메서드 = 선언부 + 구현부
        /*

        반환타입 메서드 이름 (타입 변수명, 타입 변수명, ...)   선언부
        {                                                구현부
            // 메서드 호출 시 수행될 코드                     ''
        }

               ↓

     (void)int add(int a, int b)
        {
            int result = a + b;
            return result;      // 호출한 메서드로 결과를 반환한다.
                                // 만약 반환 값이 없다면, 반환타입에 void를 작성한다.
        }

                                                    ''
        */


// ch6-15 메서드의 구현부
        // 지역 변수(lv): 메서드 내에 선언된 변수


// ch6-17 메서드의 호출
        // 메서드 이름(값1, 값2, .....);  메서드를 호출하는 방법
        // int result = add(3,5);
        // 출력, 변수   =  메서드(매개변수 3, 매개변수 5)


// 예시
        MyMath mm = new MyMath();
        long result0 = mm.min(5,3);
        long result = mm.max(5,3);      // 둘 중에 큰 값을 반환하는 메서드
        long result1 = mm.add(5L, 3L);  // add 메서드 호출
        long result2 = mm.subtract(5L, 3L);
        long result3 =  mm.multiply(5L, 3L);
        double result4 = mm.divide(5L, 3L);

        System.out.println("min(5L, 3L) = " + result0);
        System.out.println("max(5L, 3L) = " + result);
        System.out.println("add(5L, 3L) = " + result1);
        System.out.println("subtract(5L, 3L) = " + result2);
        System.out.println("multiply(5L, 3L) = " + result3);
        System.out.println("divide(5L, 3L) = " + result4);

    }

static class MyMath {
        // 메서드는 클래스 영역에만 정의 가능

        // 두 값을 받아서 줄 중에 큰 값을 반환하는 메서드를 작성하시오.
        long max(long a, long b) {
            long result = 0;

            // (1) if문을 이용한 방법
//            if (a > b) {
//                result = a;
//            } else {
//                result = b;
//            }

            // (2) 위의 if문과 else문을 삼항 연산자로 바꾸면
//            result = a > b ? a : b;
//            return result;

            // (3) 한 줄로 바꾸기
            return a > b ? a: b;
        }

        long min(long a, long b){
            return a < b? a:b;
        }
        long add(long a, long b) {
            long result = a + b;
            return result;
        //  return a + b;   // 위의 두 줄을 이와 같이 한 줄로 간단히 할 수 있다.
        }

        long subtract(long a, long b) {
            long result = a - b;
            return result;
        }

        long multiply(long a, long b) {
            return a * b;
        }

        double divide(double a, double b) {
            return a / b;
        }

// ch6-18 메서드의 실행 흐름
    // (1) main메서드에서 메서드 add를 호출한다. 인수 1L과 2L이 메서드 add의 매개변수 a, b에 각각 복사(대입)된다.
    // (2) 메서드 add의 괄호{}안에 있는 문장들이 순서대로 수행된다.
    // (3) 메서드 add의 모든 문장이 실행되거나 return문을 만나면, 호출한 메서드(main메서드)로 되돌아와서 이후의 문장들을 실행한다.




}
}
