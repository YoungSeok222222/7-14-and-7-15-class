public class _15_임의의_정수_만들기 {
    public static void main(String[] args) {
        // 난수: 게임, 섞기
        // Math.random() - 0.0과 1.0 사이의 임의의 double 값을 반환
        // 0.0 <= Math.random() < 1.0

        /*
        1 ~ 3 사이의 정수 구하기
            (1) 각 변에 3을 곱한다.
                0.0 *3 <= Math.random() * 3 < 1.0 * 3

            (2)  각 변을 int형으로 변환한다.
                (int) 0.0 <= (int) (Math.random() * 3) < (int)3.0
                        0 <= (int) (Math.random() * 3) < 3          / 0 ~ 2

            (3) 각 변에 1을 더한다.
                0+1 <= (int) (Math.random() *3) + 1 < 3 + 1
                  1 <= (int) (Math.random() *3) + 1 < 4             / 1 ~ 3
         */

        // 예제 1
        int num = 0;

        // Quiz. 1~10사이의 난수를 20개 출력하시오.
        for (int i = 1; i <=20; i++) {          // 괄호 {} 안의 내용을 20번 반복한다.
//            System.out.println(Math.random());  // 0.0 <= x < 1.0
//            System.out.println(Math.random() * 10);  // 0.0 <= x < 10.0
            System.out.println((int) (Math.random() * 10));  // 0 <= x < 10
            System.out.println((int) (Math.random() * 10) + 1);  // 1 <= x < 11
        }


        // Quiz 2. -5 ~ 5 사이의 난수를 20개 출력하시오.
        // -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5 => 11개
        for (int i = 1; i <= 20; i++) {
//            System.out.println((int) (Math.random() * 11));     // 0 <= x < 11, 0 ~ 10
            System.out.println((int) (Math.random() * 11) - 5);     // -5 <= x < 6, -5 ~ 5
        }

    }
}
