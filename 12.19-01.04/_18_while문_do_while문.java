import java.util.Scanner;

public class _18_while문_do_while문 {
    public static void main(String[] args) {
        // while문: 조건을 만족시키는 동안 블럭 {}을 반복 - 반복횟수 모를 때
        // while문 -> do-while문

        int i = 5;      // 반복할 횟수를 넣는다.

        while (i-- != 0) {
            System.out.println(i + "- I can do it.");
        }
        System.out.println("=========================");

        // while(i != 0) {     위에 식과 동일
        //  i--;
        //  System.out.println(i + "- I can do it.");
        // }

        int sum = 0;
        int j = 0;
        // j를 1씩 증가시켜서 sum에 계속 더해나간다.
        while (sum <= 100) {
            System.out.printf("%d - %d%n", j, sum);
            sum += ++j;
        }

        System.out.println("=================================================");
        System.out.println("예제: 각 자리수를 더한 값을 구하기");

        int num2 = 0, sum2 = 0;
        System.out.print("숫자를 입력하세요.(예: 123456)");

        Scanner scanner = new Scanner(System.in);
        String tmp = scanner.nextLine();    // 화면을 통해 입력받은 문자열      String tmp = "12345"
        num2 = Integer.parseInt(tmp);       // 입력받은 문자열(tmp)을 정수로?   12345 = Integer.parseInt("12345")

        while(num2 !=0) {
            // num2를 10으로 나눈 나머지를 sum에 더함
            sum2 += num2 % 10;   // sum = sum + num2 % 10;
            System.out.println("sum=" + sum2 + ",num="+num2 + ",num %10="+ num2%10);
//            System.out.printf("sum=%3d num2=%d%n", sum2, num2 );
            num2 /= 10; // num2 = num2 / 10; num2를 10으로 나눈 값
        }

        // 12345, 1234, 123, 12, 1
        int re = 0;
        for (int number = 12345; number >0; number /= 10) {
            System.out.println(number % 10);
            re += number % 10;
        }
        System.out.println(re);

System.out.println("====================================================================================");

// do-while문
        // 블럭 {}을 최소한 한 번 이상 반복 - 사용자 입력받을 때 유용
        /*
        do {
            //조건식의 연산결과가 참일 때 수행될 문장들을 적는다. (처음 한 번은 무조건 실행)
            System.out.println("Good!");
        } while (조건식); // 끝에 ';'을 잊지 않도록 주의
         */

        System.out.println("=================");
        int input = 0, answer = 0;

        answer = (int)(Math.random()*100) + 1; // 1~100 사이의 랜덤한 숫자
        Scanner scanner2 = new Scanner(System.in);
//        System.out.println(answer);

        do{
            System.out.print("1과 100사이의 정수를 입력하세요.>");
            input = scanner2.nextInt();

            if (input > answer) {
                System.out.println("더 작은 수로 다시 시도해");
            } else if (input < answer) {
                System.out.println("더 큰수로 다시 시도해");
            }
        }   while (input != answer);
        System.out.println("정답입니다.");









    }
}
