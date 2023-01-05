import java.util.Arrays;

public class _24_String배열 {
    public static void main(String[] args) {
// ch5-12 String배열의 선언과 생성

        String[] name  = new String[3]; // 3개의 문자열을 담을 수 있는 배열을 생성한다.

        // 1)
        name[0] = "Kim";
        name[1] = "Park";
        name[2] = "Yi";

        // 2)
        String[] name2 = { "Kim", "Park", "Yi"};
//=======================================================================

// 예제
        // index:            0      1      2
        String[] strArr = {"가위", "바위", "보"};
        System.out.println(Arrays.toString(strArr));;

        System.out.println((int)(Math.random()*3));

        for (int i = 0; i<10; i++){
            int tmp = (int)(Math.random()*3);
            // 0~2
            System.out.println(strArr[tmp]);
        }






    }
}
