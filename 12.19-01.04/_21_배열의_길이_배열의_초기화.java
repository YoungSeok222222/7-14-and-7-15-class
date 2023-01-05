import java.util.Arrays;    // ctrl + shift + o 자동으로 import문 추가

public class _21_배열의_길이_배열의_초기화 {
    public static void main(String[] args) {
// ch5-4 배열의 길이
        // 배열 이름.length - 배열의 길이(int형 상수)

        int[] arr = new int[5]; // 길이가 5인 int 배열
        int tmp = arr.length;   // arr.length의 값은 5이고 tmp에 5가 저장된다.

        // "배열은 한번 생성하면 (실행 동안 컴파일하면)그 길이를 바꿀 수 없다"

// =========================================================================================
        // index범위 : 0~9
        int[] ar = new int[10];  // 길이가 5인 int 배열 ar 생성
        System.out.println("ar.length = " + ar.length);

        for (int i = 0; i < ar.length; i++) {   // index범위를 벗어나서 에러
            System.out.println("ar["+i+"]="+ar[i]);
        }
//===========================================================================================

// ch5-5 배열의 초기화
        // 배열의 각 요소에 처음으로 값을 저장하는 것 (자동 초기화: int 0)
        int[] sc = new int[5];  // 길이가 5인 int형 배열을 생성한다.
        sc[0] = 50;             // 각 요소에 직접 값을 저장한다.
        sc[1] = 60;
        sc[2] = 70;
        sc[3] = 80;
        sc[4] = 90;

        /*
         <<< for문으로 만드는 경우 >>>

         for(int i=0; i < score.length; i++) {
            score[i] = i * 10 + 50;



        <<< 괄호를 이용한 방법 >>>

// 1번 방법)
        int[] score = new int[] { 50, 60, 70, 80, 90};
// 2번 방법) new int[]를 생략할 수 있음: 99% 쓰임
        int[] score = { 50, 60, 70, 80, 90};

// 두 줄로 쓰는 경우
        int[] score;
        score = { 50, 60 ,70, 80, 90};          // 에러. new int[]를 생략할 수 없음
        score = new int[] { 50, 60, 70, 80, 90};    // Ok
         */
//=====================================================================================================

// ch5-6 배열의 출력
        int[] iArr = { 100, 95, 80, 70, 60 };

        // 배열을 가리키는 참조변수 iArr의 값을 출력한다.
        System.out.println(iArr);   // [I@5b6f7412 문자열이 출력된다.

        // 배열의 요소를 순서대로 하나씩 출력
        for (int i=0; i < iArr.length; i++) {
            System.out.println(iArr[i]);
        }

        char[] chArr = { 'a', 'b', 'c', 'd'};
        System.out.println(chArr); // abcd가 출력된다.

        // 배열 iArr의 모든 요소를 출력한다. [ 100, 95, 80, 70, 60]이 출력된다.
        System.out.println(Arrays.toString(iArr));

// ============================================================================
// 예제)
        int[] iArr1 = new int[10];
        int[] iArr2 = new int[10];
        int[] iArr3 = { 100, 95, 80, 70, 60};
        char[] chArr2 = { 'a', 'b', 'c', 'd'};

        for (int i=0; i<iArr1.length; i++) {
            iArr1[i] = i+1;     // 1~10의 숫자를 순서대로 배열
        }

        for (int i=0; i<iArr2.length; i++) {
            iArr2[i] = (int)(Math.random()*10)+1;   //1~10의 값을 배열에 저장
        }

        // 배열에 저장된 값들을 출력한다.
        for (int i=0; i<iArr1.length; i++) {
            System.out.print(iArr1[i]+",");
        }
        System.out.println();

        System.out.println(Arrays.toString(iArr2));
        System.out.println(Arrays.toString(iArr3));
        System.out.println(Arrays.toString(chArr));
        System.out.println(iArr3);
        System.out.println(chArr2);







    }
}
