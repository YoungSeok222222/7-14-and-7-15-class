public class _16_for문 {
    public static void main(String[] args) {
        // for문: 조건을 만족하는 동안 블럭 {}을 반복 -> 반복횟수를 알 때 적합
        // while문: 반복횟수를 모를 때 적합

//            (1)    (2)    (4)
//      for (초기화; 조건식; 증감식;) {   조건식이 거짓이 될 때까지
//          (3). 수행될 문장
//      }

        for (int i = 1; i <=5; i++) {
            // 1부터     5까지   1씩 증가
            System.out.println("I can do it");
        }

        // 1부터 10보다 작은 동안 j*2씩 증가
        for (int j = 1; j <=10; j *= 2) {   // 1 2 4 8
            System.out.println(j);
        }

        for (int i = 10; i >= 1; i--) { // 10 9 8 7 6 5 4 3 2 1
            System.out.println(i);
        }

        for (int i = 1, j = 10; i <= 10; i++, j--){
            System.out.println("i="+i+",j="+j);
            /*
            i=1,j=10
            i=2,j=9
            i=3,j=8
            i=4,j=7
            i=5,j=6
            i=6,j=5
            i=7,j=4
            i=8,j=3
            i=9,j=2
            i=10,j=1
            */
        }

        // scope(범위) - 선언 위치부터 선언된 블록 끝까지
        int p = 8;                  // for문 바깥에서 선언된 p를 for문 변수로 사용하거나

        for (p = 3; p <=10; p++){   // for ( ; p <=10; p++){}도 가능
            System.out.println(p);
        }
        System.out.println(p);      // for문 바깥에서도 접근 가능 => 변수의 범위가 넓어짐(하지만 변수의 범위는 좁은게 좋음)


        int sum = 0;
        for (int i = 1; i<=5; i++) {
            sum += i;
            System.out.printf("1부터 %2d 까지의 합: %2d%n", i);
        }

    }
}
