public class _25_커맨드라인입력받기 {
    public static void main(String[] args) {

// ch-5-16,17 커맨드라인 입력받기
        // 커맨드 라인(cmd)에 입력한 값이 문자열 배열에 담겨서 전달된다.

        // cmd 에서 java 클래스명 abc 123 "Hello world" 입력하면
        // 문자열로써 "abc" | "123 | "Hello world"가 args에 들어온다.
        // args[0] = "abc"
        // args[1] = "123"
        // args[2] = "Hello world"
        // 길이가 3인 배열 생성

// ======================================================================================

// 예제
        System.out.println("매개변수의 개수:" + args.length);
        for (int i =0; i < args.length; i++) {
            System.out.println("args[" + i + "] = \"" + args[i] + "\"" );
        }

    }
}
