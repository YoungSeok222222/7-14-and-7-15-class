import java.util.Arrays;

public class _28_Arrays로_배열_다루기 {
    public static void main(String[] args) {
// ch5-24 Arrays로 배열 다루기
        // 배열의 비교와 출력 - equals(), toString()

        int[] arr = {0,1,2,3,4};
        int[][] arr2D = { {11,12}, {21,22}};

        System.out.println(Arrays.toString(arr));   // [0,1,2,3,4]  문자열로 반환
        System.out.println(Arrays.deepToString(arr2D)); // [ [11, 12], [21, 22]]


        String[][] str2D = new String[][]  {{ "aaa", "bbb"}, { "AAA", "BBB"}};
        String[][] str2D2 = new  String[][] {{ "aaa", "bbb" }, {"AAA", "BBB"}};

        System.out.println(Arrays.equals(str2D, str2D2));       // false    1차원 배열은 equals
        System.out.println(Arrays.deepEquals(str2D, str2D2));   // true     2차원(혹은 그이상) 배열일 때는 deepEquals

        // 배열의 복사 - copyOf(), copyOfRange()

        int[] ar = {0,1,2,3,4}; //배열   복사할 배열의 개수
        int[] ar2 = Arrays.copyOf(ar, ar.length);   // ar2 = [0,1,2,3,4]
        int[] ar3 = Arrays.copyOf(ar, 3); //  ar3 = [0,1,2]
        int[] ar4 = Arrays.copyOf(ar, 7); //  ar4 = [0,1,2,3,4,0,0]
        int[] ar5 = Arrays.copyOfRange(ar,2, 4);  // ar5 = [2,3] <- 4는 불포함
        int[] ar6 = Arrays.copyOfRange(ar, 0, 7); // ar6 = [0,1,2,3,4,0,0]



// ch5-24 Arrays로 배열 다루기
        // 배열의 정렬 - sort()
        int[] arra = { 3, 2, 0, 1, 4 };
        Arrays.sort(arra);  // 배열 arr을 정렬한다.
        System.out.println(Arrays.toString(arr));   // [0, 1, 2, 3, 4]

//====================================================================================================================

// 예시
        int[] arrays = {0,1,2,3,4};   // 1차원 배열 arrays
        int[][] arrays2D = { {11,12}, {21, 22}};    // 2차원 배열

        System.out.println(Arrays.toString(arrays));
        System.out.println(Arrays.toString(arrays2D));  // [[I@4f3f5b24, [I@15aeb7ab]
        System.out.println(Arrays.deepToString(arrays2D));  // [[11, 12], [21, 22]]


        String[][] str2DD = {{ "aaa", "bbb"}, {"AAA", "BBB"}};
        String[][] str2D22 = {{"aaa", "bbb"}, {"AAA", "BBB"}};

        System.out.println(str2DD==str2D2); // 참조변수 값 비교 false
        System.out.println(Arrays.deepEquals(str2DD,str2D2)); // 참조변수 값 비교  true

        int[] arr2 = Arrays.copyOf(arrays, arrays.length);  //[0, 1, 2, 3, 4]   맨 앞부터 복사
//        int[] arr2 = Arrays.copyOf(arrays, 7);  // [0, 1, 2, 3, 4, 0, 0]
        System.out.println(Arrays.toString(arr2));

        int[] arr3 = Arrays.copyOfRange(arrays, 2, 4);  // [2, 3] 특정 범위부터 복사


        int[] arr4 = {4, 5, 1, 9, 3, 2};
        Arrays.sort(arr4);                          // 배열 arr을 오름차순으로 정렬
        System.out.println(Arrays.toString(arr4));  //[1, 2, 3, 4, 5, 9]











    }
}
