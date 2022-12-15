import com.sun.org.apache.xpath.internal.objects.XString;

public class _10_비교_연산자와_문자열의_비교 {
    public static void main(String[] args) {
// 비교 연산자 > < >= <= == !=
        // 두 피연산자를 비교해서 true(참) 또는 false(거짓)을 반환

        /*
        비교 연산자              연산결과
            >         좌변 값이 크면, true 아니면 false
            <         좌변 값이 작으면, true 아니면 false
           >=         좌변 값이 크거나 같으면, true 아니면 false
           <=         좌변 값이 작거나 같으면, true 아니면 false
           ==         두 값이 같으면, true 아니면 false
           !=         두 값이 다르면, true 아니면 false

        */


// 문자열의 비교
        // 문자열 비교에는 == 대신 equals()를 사용해야 한다.

        String str1 = "abc";
        String str2 = "abc";
        System.out.println(str1 == str2);   // true
        System.out.println(str1.equals(str2)); // true


        String str3 = new String("abc");
        String str4 = new String("abc");
        System.out.println(str3 == str4);   // false
        System.out.println(str1.equals(str4));  // true





    }
}
