import java.util.Arrays;

public class _23_배열의_활용2 {
    public static void main(String[] args) {
// 배열의 활용(3)
        // 섞기(shuffle) - 배열의 요소의 순서를 반복해서 바꾼다. (숫자 섞기, 로또 번호 생성)

        int[] numArr = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
        System.out.println(Arrays.toString(numArr));

        for (int i=0; i < 100; i++) {
            int n = (int)(Math.random() * 10);  //0~9 중의 한 값을 임의로 얻는다.
            int tmp  = numArr[0];
            numArr[0] = numArr[n];
            numArr[n] = tmp;    // numArr[0]과 numArr[n]의 값을 서로 바꾼다.

        }
        System.out.println(Arrays.toString(numArr));
// =================================================================================================

// 예제)
        // index : 0~44
        int[] ball  = new int[45];  // 45개의 정수값을 저장하

        // 배열의 각 요소에 1~45의 값을 저장한다.
        for (int i=0; i < ball.length; i++)
            ball[i] = i+1;      // ball[0]에 1이 저장된다.


        int tmp = 0;    // 두 값을 바꾸는데 사용할 임시변수
        int j  = 0;     // 임의의 값을 얻어서 저장할 변수


        // 배열의 i번째 요소와 임의의 요소에 저장된 값을 서로 바꿔서
        // 0번째 부터 5번째 요소까지 모두 6개만 바꾼다.
        for (int i=0; i < 6; i++) {
            j = (int)(Math.random() * 45);  // 0~44범위의 숫자
            tmp = ball[i];
            ball[i] = ball[j];
            ball[j] = tmp;
            System.out.println(Arrays.toString(ball));
        }

        // 배열 ball의 앞에서부터 6개의 요소를 출력한다.

        for (int i = 0; i < 6; i++)
            System.out.printf("ball["+i+"] = " + ball[i]+"%n");





    }
}
