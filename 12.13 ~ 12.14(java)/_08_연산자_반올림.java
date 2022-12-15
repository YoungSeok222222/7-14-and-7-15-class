public class _08_연산자_반올림 {
    public static void main(String[] args) {
        // 반올림 - Math.round() : 실수를 소수점 첫째자리에서 반올림한 정수를 반환
        long result = Math.round(4.52); // result에 5가 저장된다.
        double pi = 3.141592;

        System.out.println(pi);
        System.out.println(pi*1000);
        System.out.println(Math.round(pi*1000) / 1000); //3
        System.out.println(Math.round(pi*1000) / 1000.0); //3.142
        System.out.println((double)Math.round(pi*1000) / 1000); //3.142

        // double pi = 3.141592 3.141로 바꾸려면?

        System.out.println(pi*1000); // 3141.592
        System.out.println((int)(pi*1000)); // 3141
        System.out.println((int)(pi*1000) / 1000); // 3
        System.out.println((int)(pi*1000) / 1000.0); // 3.141
    }
}
