public class _17_중첩for문 {
    public static void main(String[] args) {
        System.out.println("예제 1");
        for (int i = 2; i <=9; i++) {
            for (int j = 1; j<=9; j++) {
                Object fdidiednisn;
                System.out.println(i+"*"+j+"="+(i*j));
            }
        }

        System.out.println("=======================");
        System.out.println("예제 2");


        for (int i = 0; i <= 4; i++) {
            for (int j = 0; j <=4; j++) {
                System.out.print("*");
            }
            System.out.println();   // 줄바꿈
        }

        System.out.println("=======================");
        System.out.println("예제 3");

        for (int i = 1; i <= 5; i++) {
            for (int j = 1; j <= i; j++ ) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
