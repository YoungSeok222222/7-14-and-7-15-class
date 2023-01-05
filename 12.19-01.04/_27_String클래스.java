public class _27_String클래스 {
    public static void main(String[] args) {
// ch5-14 String클래스
        // 1.String 클래스는 char[]와 메서드(기능)를 결합한 것

            // String 클래스  = char[] + 메서드(기능)
            //                 문자배열 + 메서드

        // 2.String 클래스는 내용을 변경할 수 없다.(read only)

            String a = "a";
            String b = "b";
            a = a + b;
// ==================================================================

// ch5-15 String클래스의 주요 메서드

        /*
        메서드                                              설명
       ==========================================================================================================================
       char charAt(int index)               |   문자열에서 해당 위치(index)에 있는 문자를 반환한다.
       int length()                         |   문자열의 길이를 반환한다.
       String substring(int from, int to)   |   문자열에서 해당 범위(from~to)의 문자열을 반환한다. (to는 포함 안 됨)
       boolean equals(Object obj)           |   문자열의 내용이 같은지 확인한다. 같으면 결과는 true, 다르면 false
       char[] toCharArray()                 |   문자열을 문자배열(char[])로 변환해서 반환한다.
        */


        String str1 = "ABCDE";
        char ch1 = str1.charAt(3);  // 문자열 str1의 4번쨰 문자 'D'를 ch에 저장

        String tmp = str1.substring(1,4);   // str에서 index범위 1~4의 문자들을 반환
        System.out.println(tmp);            // "123"이 출력된다.

//===================================================================================================================

// 예제
        //            01234
        String str = "ABCDE";
        char ch = str.charAt(2);
        System.out.println(ch);

        String str2 = str.substring(1,4);   // 4가 안 들어가므로 BCD만
        System.out.println(str2);

        String str3 = str.substring(1); // BCDE
        System.out.println(str3);
        // String str3 = str.substring(1, str.length());  위 코드와 동일



    }
}
