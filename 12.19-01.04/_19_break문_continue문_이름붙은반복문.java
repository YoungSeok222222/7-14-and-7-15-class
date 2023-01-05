import java.util.Scanner;

public class _19_break문_continue문_이름붙은반복문 {
    public static void main(String[] args) {
// break문
        // 자신이 포함된 하나의 반복문을 벗어난다.

        int sum = 0;
        int i = 0;

        // while(생략불가)
        while (true) {  //무한 반복문 for(;true;) {}
            if (sum>100)
                break;  // 자신이 속한 하나의 반복문을 벗어난다.
            ++i;
            sum += i;
            }   // end of while
        System.out.println("i = " + i);
        System.out.println("sum = " + sum);

        int sum2 = 0;
        int j = 0;


        for (;true;) {
            if (sum2 > 100)
                break;
            ++j;
            sum2 += j;
        }
        System.out.println("j = "+j);
        System.out.println("sum2 = "+sum2);
// ==================================================================================================

// continue문
        // 자신이 포함된 반복문의 끝으로 이동 - 다음 반복으로 넘어감. 전체 반복 중에서 특정 조건시 반복을 건너뛸 때 유용

        //     (1)         (2)    (4)
        for (int ii = 0; ii <=10; ii++) {
            //  (3)
            if (ii%2==0)
                continue;
            System.out.println(ii); // 여기가 생략됨
        }
// ==========================================================================================================

        // 예제
        int menu = 0;
        int number =0;

        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("(1) square");
            System.out.println("(2) square root");
            System.out.println("(3) log");
            System.out.println("원하는 메뉴(1~3)를 선택하세요.");

            String tmp = scanner.nextLine();    // 화면에서 입력받은 내용을 tmp에 저장
            menu = Integer.parseInt(tmp);       // 입력받은 문자열 (tmp)을 숫자로 변환

            if (menu==0) {
                System.out.println("프로그램을 종료합니다.");
                break;
            } else if (!( 1 <= menu && menu <= 3)) {
                System.out.println("메뉴를 잘못 선택하셨습니다. (종료는 0)");
                continue;
            }
            System.out.println("선택하신 메뉴는 " + menu + "번입니다.");
            System.out.println();
        }
//=======================================================================================
        System.out.println("========================");
// 이름 붙은 반복문
        // 반복문에 이름을 붙여서 하나 이상의 반복문을 벗어날 수 있다.

        Loop1 : for (int a = 2; a <= 9; a++) {
            for (int b = 1; b <= 9; b++){
                if (b==5)
                    break Loop1;
//                    break;
//                    continue Loop1;
//                    continue;
                System.out.println(a + "*" + b + "=" + a*b);
            }   // end of for b
            System.out.println();
        }   // end of Loop1
        System.out.println("========================");
//==================================================================================================

// 예제 1

        int option = 0;
        int number2 = 0;
        Scanner scanner2 = new Scanner(System.in);

        outer:  // while문에 outer라는 이름을 붙인다.
        while (true) {
            System.out.println("(1) square");
            System.out.println("(2) square root");
            System.out.println("(3) log");
            System.out.println("원하는 메뉴(1~3)를 정하세요");

            String tmp2 = scanner2.nextLine();
            option = Integer.parseInt(tmp2);

            if (option == 0) {
                System.out.println("프로그램을 종료합니다.");
                break;
            } else if (!(1 <= option && option <= 3)) {
                System.out.println("메뉴를 잘못선택하셨습니다. (종료는 0)");
                continue;
            }
//            System.out.println("선택하신 메뉴는 " +  + "번입니다.");
//            System.out.println();
            for (;;) {
                System.out.println("계산할 값을 입력하세요. (계산 종료:0, 전체 종료: 99)");

//                Scanner scanner3 = new Scanner(System.in);
                String tmp3 = scanner2.nextLine();  // 화면에서 입력받은 내용을 tmp에 저장
                number2 = Integer.parseInt(tmp3);   // 입력받은 문자열(tmp3)을 숫자로 변환

                if (number2==0)
                    break;           // 계산 종료. for문을 벗어난다.
                if (number2==99)
                    break outer;     // 전체 종료. for문과 while문을 모두 벗어난다.

                switch (option){
                    case 1:
                        System.out.println("result="+number2*number2);
                        break;
                    case 2:
                        System.out.println("result="+Math.sqrt(number2));
                        break;
                    case 3:
                        System.out.println("result="+Math.log(number2));
                        break;
                }
            }   // for(;;)
        }   // while의 끝
        System.out.println("프로그램이 종료되었습니다.");
    }   // main의 끝
}
