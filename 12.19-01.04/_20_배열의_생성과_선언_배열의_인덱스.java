public class _20_배열의_생성과_선언_배열의_인덱스 {
    public static void main(String[] args) {
// ch5-1 배열

// 배열이란?: "배열은 같은 타입의 여러 변수를 하나의 묶음으로 다루는 것"


// ch5-2 배열의 선언과 생성
        // 배열의 선언 - 배열을 다루기 위한 참조변수의 선언

        /*
                선언방법                 선언 예
       Java   타입[] 변수이름;            int[] score;
                                        String[] name;

       C언어   타입 변수이름[]:            int score[];
                                        String name[];
        */

        // 타입 [] 변수이름; 배열을 선언(배열을 다루기 위한 참조변수 선언)
        // 변수이름 = new 타입[길이]; 배열을 생성(실제 저장공간을 생성)

        int[] score;    // int타입의 배열을 다루기 위한 참조변수 score 선언
        score = new int[5]; // int타입의 값 5개를 저장할 수 있는 배열 생성
//======================================================================================

// ch5-3 배열의 인덱스
        // 배열의 인덱스 - 각 요소(저장공간)에 자동으로 붙는 (일련)번호
        // 인덱스(index)의 범위는 0부터 '배열길이 -1까지." ex). 5개면 인덱스는 0부터 4까지

        int[] score2 = new int[5];  // 길이가 5인 int배열
        // score2 = 1   2   3   4   5    <- 배열의 요소(element)
        //         score[0] ... score[4] <- 배열의 인덱스(index)

        score2[3] = 100; // score2 = 1  2   3   100 5

        int value = score[3]; // value = 100

// ========================================================================================

// 실습).

        int[] score3;             // 1. 배열 socre3 선언(참조변수)
        score3 =  new int[5];     // 2. 배열의 생성(int저장공간 x 5 )

         // int[] score3 = new int[5]; 배열의 선언과 생성을 동시에
        score3[3] = 100;
        System.out.println("score3[0]="+score3[0]);
        System.out.println("score3[1]="+score3[1]);
        System.out.println("score3[2]="+score3[2]);
        System.out.println("score3[3]="+score3[3]);
        System.out.println("score3[4]="+score3[4]);

        int value2 = score3[3];
        System.out.println("value2="+value2);











    }
}
