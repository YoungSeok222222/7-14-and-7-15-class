import java.util.Scanner;

public class _14_조건문과_반복문_switch문 {
    public static void main(String[] args) {


// switch문: 처리해야 하는 경우의 수가 많을 때 유용한 조건문
            // 1. 조건식을 계산한다.
            // 2. 조건식의 결가와 일치하는 case문으로 이동한다.
            // 3. 이후의 문장들을 수행한다.
            // 4. break문이나 switch문의 끝을 만나면 switch문 전체를 빠져나간다.


            // default: 조건식의 결과와 일치하는 case문이 없을 때 수행될 문장들 / 생략가능


            // switch문의 제약 조건
                // 1. switch문의 조건식 결과는 정수 또는 문자열이어야 한다.
                // 2. case문의 값은 정수 상수(문자 포함), 문자열만 가능하며, 중복되지 않아야 한다. / 변수는 안 됨

        /*
        int num, result;

        final int ONE = 1;
        result = 0 + ONE;

        switch (result) {
            case '1':   OK. 문자 리터럴(정수 49와 동일)
            case ONE:   OK. 정수 상수
            case "YES": OK. 문자 리터럴. JDK 1.7부터 허용
            case num:   에러. 변수는 불가
            case 1.0:   에러. 실수도 불가
        }
        */

        System.out.println("현재 월을 입력하세요->");

        Scanner scanner = new Scanner(System.in);
        int month = scanner.nextInt(); // 화면을 통해 입력받은 숫자를 month에 저장

        switch (month) {
            case 3:
            case 4:
            case 5:
                System.out.println("현재 계절은 봄입니다.");
                break;
            case 6: case 7: case 8:
                System.out.println("현재의 계절은 여름입니다.");
                break;
            case 9: case 10: case 11:
                System.out.println("현재의 계절은 가을입니다.");
                break;
            default:
//            case 12: case 1: case 2:
                System.out.println("현재의 계절은 겨울입니다.");
        }










    }
}
