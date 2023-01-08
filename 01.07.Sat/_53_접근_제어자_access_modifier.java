class MyParent {
    private int prv;    // 같은 클래스
    int dft;            // 같은 패키지
    protected int prt;  // 같은 패키지 + 자손(다른 패키지)
    public int pub;     // 접근제한 없음

    public void printMembers() {
        System.out.println(prv);
        System.out.println(dft);
        System.out.println(prt);
        System.out.println(pub);
    }
}
public class _53_접근_제어자_access_modifier {
    public static void main(String[] args) {
//ch7-21 접근 제어자(access modifier) - 4개 중 한 개만 사용 가능하다.

/*
private - 같은 클래스 내에서만 접근 가능하다.
(default) - 같은 패키지 내에서만 접근 가능하다.
protected - 같은 패키지 내에서, 그리고 다른 패키지의 자손클래스에서 접근이 가능하다.
public - 접근 제한이 전혀 없다.


제어자         같은 클래스      같은 패키지      자손 클래스      전체
=========================================================================
public            O               O              O            O
protected         O               O              O            O
(default)         O               O
private           O

접근 제한 없음    같은패키지 + 자손   같은 패키지     같은 클래스
    public    >    protected    >  (default)  >   private
*/

// 예제 - 맨위의 MyParent 클래스의 변수들을 사용해보기
        MyParent p = new MyParent();
//        System.out.println(p.prv);      // 에러.
        System.out.println(p.dft);      // OK
        System.out.println(p.prt);      // OK
        System.out.println(p.pub);      // OK

    }
}







