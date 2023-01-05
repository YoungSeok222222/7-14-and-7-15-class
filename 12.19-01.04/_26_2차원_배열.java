import java.util.Scanner;

public class _26_2차원_배열 {
    public static void main(String[] args) {
// 5-18 2차원 배열
        // 테이블 형태의 데이터를 저장하기 위한 배열

        //                     [y][x]
        int[][] score = new int[4][3];  // 4행(y) 3열(x)의 2차원 배열을 생성한다.

        score[0][0] = 100;              // 배열 score의 1행 1열에 100을 저장
        System.out.println(score[0][0]);// 배열 score의 1행 1열의 갑을 출력

//=====================================================================================

// 5-20 2차원 배열의 초기화

        int[][] arr = new int[][] { {1, 2, 3}, {4, 5, 6} };
        int[][] ar = { {1, 2, 3}, {4, 5, 6} };  // new int[][]가 생략됨

        int[][] a = {
                {1, 2, 3},
                {4, 5, 6}
        };
//========================================================================================

// 5-21 2차원 배열 예제

        int[][] score2 = {
                 { 100, 100, 100 }
                ,{ 20, 20, 20 }
                ,{ 30, 30, 30 }
                ,{ 40, 40, 40}
        };

        int sum = 0;

        for (int i = 0; i < score2.length; i++) {
            for (int j = 0; j < score2[i].length; j++) {
                System.out.printf("score[%d][%d]=%d%n", i, j, score2[i][j]);

                sum += score2[i][j];
            }
        }

        System.out.println("sum="+ sum);
//===============================================================================

// 예제

        int[][] score3 = {
                 { 100, 100, 100}
                ,{ 20, 20, 20}
                ,{ 30, 30, 30}
                ,{ 40, 40, 40}
                ,{ 50, 50, 50}
            };
        // 과목별 총점
        int korTotal = 0, engTotal = 0, mathTotal = 0;

        System.out.println(" 번호 국어 영어 수학 총점 평균");
        System.out.println("===============================");

        for (int i=0; i < score3.length; i++) {
            int sum3 = 0;   // 개인별 총점
            float avg = 0.0f;   // 개인별 평균

            korTotal += score3[i][0];
            engTotal += score3[i][1];
            mathTotal += score3[i][2];
            System.out.printf("%3d", i+1);

            for (int j = 0; j < score3[i].length; j++) {
                sum3 += score3[i][j];
                System.out.printf("%5d", score3[i][j]);
            }
            avg = sum3 / (float)score3[i].length; // 평균
            System.out.printf("%5d %5.1f%n", sum3, avg);
        }
        System.out.println("==================================");
        System.out.printf("총점: %3d %4d %4d%n", korTotal, engTotal, mathTotal);
// =========================================================================================================

// 예제
        String[][] words = {
                 {"chair" , "의자"}       // words[0][0], words[0][1]
                ,{"computer", "컴퓨터"}   // words[1][0], words[1][1]
                ,{"integer", "정수"}      // words[2][0], words[2][1]
        };

        Scanner scanner = new Scanner(System.in);

        for (int i=0; i<words.length; i++) {
            System.out.printf("Q%d. %s의 뜻은?", i+1, words[i][0] );   // %s는 문자열 출력할 때 쓰는 지시자

            String tmp = scanner.nextLine();

            if (tmp.equals(words[i][1])) {
                System.out.printf("정답입니다.%n%n");
            } else {
                System.out.printf("틀렸습니다. 정답은 %s 입니다. %n%n", words[i][1]);  // %n은 줄바꿈 문자 - printf에서 쓰임
            }
        } // for
    }   // main

}
