public class _12_조건_연산자와_대입_연산자 {
    public static void main(String[] args) {
// 조건 연산자 ?: 조건식의 결과에 따라 연산결과를 달리한다.

        // 조건식 ? 식1 : 식2
        // 조건이    t     f

        int x = 3, y = 5;
        int result = (x > y) ? x : y;
        System.out.println(result);

// 대입 연산자
        // 오른쪽 피연산자를 왼쪽 피연산자에게 저장 후 저장된 값을 반환
        System.out.println(x = 3); // 변수 x에 3이 저장되고
        System.out.println(x); // 연산결과인 3이 출력된다.

        System.out.println(x = y = 3); // 연산결과인 3이 출력된다.

        int xxx = 15;
        // lvalue  rvalue

        // lvalue - 대입 연산자의 왼쪽 피연산자 / 저장 공간(변수, 배열)
        // rvalue - 대입 연산자의 오른쪽 피연산자 /

        int i = 0;
        // 3 = i+3; 에러. lvalue가 값을 저장할 수 있는 공간이 아님
        // i + 3 = i; 에러. lvalue의 연산결과가 리터럴(i+3 -> 0+3 -> 3)

        final int Max = 3;  // 변수 앞에 키워드 final을 붙이면 상수가 된다.
        // Max = 10;    에러. 상수(Max)에 새로운 값을 저장할 수 없다.


// 복합 대입 연산자
        // 대입 연산자와 다른 연산자를 하나로 축약

        /*
           i += 3;    ==   i = i + 3;

           i *= (10+j); ==  i = i*(10+j);

        */



    }
}
