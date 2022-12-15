public class _06_타입간의_변환방법 {
    public static void main(String[] args) {
        // 타입간의 변환방법

        String str = "3";

        // (1). 문자와 숫자간의 변환: '0'을 더하거나 뺀다.
        // 3숫자 -> '3'문자
        // '3'문자 -> 3숫자


        // (2). 문자열로의 변환:  빈 문자열""을 더하거나 뺸다.
        // 3숫자 -> "3"문자열
        // '3'문자 -> "3"문자열

        // (3). 문자열을 숫자로 변환:  Integer.parseInt("3")을 써서 숫자로 변환
        // "3"문자열 -> 3숫자
        // "3.4" -> 3.4: Double.parseDouble("3.4")

        // (4). 문자열을 문자로 변환: CharAt(0)
        // "3" -> '3'
        System.out.println(str.charAt(0) - '0'); // '3' - '0' -> 3
        System.out.println('3'-'0'+1); // '3'-'0'+1 -> 4
        System.out.println(Integer.parseInt("3") + 1); // "3"+ 1 -> 4
        System.out.println("3" + 1); // "3"+1 -> 31
        System.out.println(3+'0'); // 3+'0' -> 51 '0'은 숫자로 48
        System.out.println((char) (3+'0')); //
    }
}
