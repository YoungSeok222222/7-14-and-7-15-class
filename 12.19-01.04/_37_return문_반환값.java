public class _37_return문_반환값 {
    public static void main(String[] args) {
// ch6-20 return문
        // 실행 중인 메서드를 종료하고 호출한 곳으로 되돌아간다.

        // 반환타입이 void인 경우

//        void printGugudan(int dan)
//            if (!(2<=dan && dan<=9))
//                return; // dan의 값이 2~9가 아니라면, 호출한 곳으로 그냥 되돌아간다.
//            for (int i=1; i <= 9; i++) {
//                System.out.printf("%d * %d = %d%n", dan, i, dan*i);
//            }
//            return; // 반환 타입이 void이므로 생략가능. 컴파일러가 자동추가
//
//        // 반환타입이 void가 아닌 경우, 반드시 return문 필요
//        int multiply(int x, int y){
//            int result = x * y;
//            return result;  // 반환 타입이 void가 아니므로 생략불가
//        }
//        int max(int a, int b) {
//            if(a > b)
//                return a;   // 조건식이 참일 때만 실행된다. => 에러 발생 - return문이 참일 때만 실행되기 때문
//            else
//                return b;   // 조건식이 거짓일 때 실행된다.
//        }

        MyMath mm = new MyMath();
        mm.printGugudan(8);    // 구구단 3단을 출력


    }

static class MyMath{
        void printGugudan(int dan) {
            if ( !(2<= dan && dan <= 9))
                return;     // 입력받은 단(dan)이 2~9가 아니면, 메서드 종료하고 돌아가기

            for (int i=1; i <= 9; i++){
                System.out.printf("%d * %d = %d%n", dan, i, dan * i);
            }
            return;     // void면 생략 가능
        }
        long max(long a, long b){
            if (a > b)
                return a;   // 조건식이 참일때만 실행
            else
                return b;   // 조건식이 거짓일 때 실행
        }
}
}
