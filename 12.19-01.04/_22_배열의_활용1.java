public class _22_배열의_활용1 {
    public static void main(String[] args) {
// ch5-8 배열의 활용(1)
        // 총합과 평균: 배열의 모든 요소를 더해서 총합과 평균을 구한다.


// 예제)
        int sum = 0;    // 총점을 저장하기 위한 변수
        float average = 0f; // 평균을 저장하기 위한 변수

        int[] score = {100, 88, 100, 100, 90};

        for (int i=0; i < score.length; i++) {
            sum += score[i];
        }
        average = sum / (float)score.length;    // 계산결과를 float로 얻기 위해서 형변환

        System.out.println("총점:" + sum);
        System.out.println("평균:" + average);
//==========================================================================

// ch5-9 배열의 활용(2)
        // 최대값과 최소값: 배열의 요소 중에서 제일 큰 값과 제일 작은 값을 찾는다.
        int[] scores = { 79, 88, 91, 33, 100, 55, 95};

        int max = score[0]; // 배열의 첫번째 값으로 최대값을 초기화한다.
        int min = score[0]; // 배열의 첫번째 값으로 최소값을 초기화한다.

        for (int i = 1; i < scores.length; i++) {
            if (scores[i] > max) {
                max = scores[i];
            } else if (scores[i] < min) {
                min = scores[i];
            }
        } // end of for

        System.out.println("최대값 : "+ max);
        System.out.println("최소값 : " + min);
    }   // end of main
}
