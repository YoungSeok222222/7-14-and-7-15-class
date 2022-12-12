
public class _02_VarEx1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
// 4. 변수란? 변수의 선언 + 변수의 타입
		
		// 변수 = 하나의 값을 저장하기 위한 메모리 공간
		// 저장할 값의 타입과 일치하는 타입으로 변수를 선언
		// 정수(byte/short/int/long), 실수(float/double), 문자(char/string)
		
		// int(정수타입), double(실수 타입), char(문자형 타입 = ''), string(문자열 타입 = "")  
		
		
//  변수의 타입
		
/* 
● 기본형 (Primitive type) 
	 오직 8개 (boolean, char, byte, short, int, long, float, double)
	 1 bit = 2진수 1자리
	 
	 1 byte = 8 bit 
	 2 byte = 16 bit
	 4 byte = 32 bit
	 8 byte = 64 bit
	 
	 1 bit -> 0과 1 2가지 / 2 bit -> 00, 01, 10, 11 4가지
	 
	 n비트로 표현할 수 있는 값의 개수: 2^n개
	 n비트로 표현할 수 있는 부호없는 정수의 범위 0 ~ 2^n-1
	 n비트로 효현할 수 있는 부호있는 정수의 범위 -2^n-1 ~ (2^n-1) -1 
	 
	 즉 부호 없는 정수 8비트(2^8)는 0~255까지 256개임 / 8 bit = 1byte
	 반면에 부호 있는 8비트(2^7 ~ 2^7 -1) 즉, -128 ~ 127까지 256개임
	 
	 
	 ▶ 논리형(1 byte) - true 와 false 중 하나를 값으로 가지며, 조건식과 논리적 계산에 사용된다.
	 ▶ 문자형(2 byte) - 문자를 저장하는데 사용되며, 변수 당 하나의 문자만을 저장할 수 있다.
	 ▶ 정수형 - 정수 값을 저장하는데 사용된다. 주로 사용하는 것은 int(4 byte)와 long(8 byte)이며, 
	 			byte(1 byte)는 이진 데이터를 다루는데 사용된다.
	 			short(2 byte)은 c언어와의 호환을 위해 추가되었다.(잘 안 쓰
	 ▶ 실수형 - 실수 값을 저장하는데 사용된다. float(4 byte)와 double(8 byte)이 있다.
	 ▶

● 참조형(Reference type) / 참조변수 = 객체의 주소를 저장
	 기본형을 제외한 나머지(String, System(무한개) 등)
	 메모리 주소를 저장(4 byte(최대값은 40억 바이트 즉, 4G의 메모리를 다룸) 또는 8 byte(1600만TB))
*/
		
		int x = 4, y = 2;
		char ch = '가';
		double pi = 3.14;
		System.out.println(x+y);
		System.out.println(x-y);
		System.out.println(x*y);
		System.out.println(x/y);
//===========================================================
		
// 5. 변수, 상수, 리터럴 
		
		// 변수(variable) - 하나의 값을 저장하기 위한 공간
		// 상수(constant) - 한 번만 값을 저장 가능한 변수(ex. final int ~) / final을 변수타입 앞에 적어준다.
		// 리터럴(literal) - 그 자체로 값을 의미하는 것(==기존의 상수)
		
		final int score = 100;
//		score = 200;
		System.out.println(score);
		
		
		// byte b = 127; 가능 byte 타입은 -128부터 127까지 가능
		// byte b = 128; 불가능
		
		// int i = 100; 10진수 
		// int i = 0100; 8진수  접두사 0이 앞에 붙었기 때문
		// int i = 0x100; 16진수 접두사 0x가 붙었기 때문
		// int i = 0b100; 2진수 접두사 0b가 붙었기 때문
		
		
		// integer 타입의 최대값은 약 20억이므로 그 이상은 long 사용
		long uil = 100; // integer는 20억 이내이므로 L 생략가능
		long ui = 10_000_000_000L; // integer(20억)이상이면 L을 붙여야한다. 
		System.out.println(ui);
		
		float f = 3.14f;
		double d = 3.14d; // d는 생략 가능
		
		// 10.  = 10.0
		// .10 = 0.10 
		// 10f = 10.0f
		// 1e3.  = 1000.0(d)
//======================================================================
		
// 7. 변수와 리터럴의 타입 불일치 
		// (1) 범위가 '변수(그릇) > 리터럴(물건)'인 경우, ok
		int ii = 'A'; 	// int > char
		long iii = 123; // long > int 
		double dd = 3.14f; // double > float
		
		// (2) 범위가 '변수(그릇) < 리터럴(물건)'인 경우, error
//		int ig = 30_000_000_000; // int의 범위(20억) 벗어남②
//		long ll = 3.14f;		 // long < float
//		float f = 3.14; 		 // float < double
		
		// (3) byte, short 변수에 int 리터럴 저장가능
		byte b = -100; // 가능, byte의 범위(-128 ~ 127)에 속함
//		byte b = 128;  // error, byte의 범위를 벗어남
		
//실습==============================================================
		boolean power = true;
		System.out.println(power);
		
		byte bb = 127; // -128 ~ 127
		
		int oct = 010; // 8진수, 10진수로 8
		int hex = 0x10; // 16진수, 10진수로 16
		System.out.println(oct); // println은 무조건 10진수로 출력
		System.out.println(hex);
//		System.out.printf(hex); // printf는 16진수로 출력
		
		long sample = 10_000_000_000L;
		
		float ff = 3.14f; // f생략 불가능
		double ddd = 3.14; // d 생략 가능
		System.out.println("=================");
		System.out.println(10.);
		System.out.println(.10);
		System.out.println(10f);
		System.out.println(1e3);
//==============================================================		
		
// 8. 문자와 문자열
		char al = 'A';
//		char al2 = 'AB'; // error
		String s = "ABC";
		
		String s1 = ""; // 빈 문자열
//		char ch1 = ''; // error
		
		String s2 = "A" + "B"; // "AB"
		System.out.println(s2);
		
		String s3 = "" + 7; // 숫자 -> 문자열
		System.out.println(s3); // "7"
		
//		!!!!!! 문자열 + any type -> 문자열 / any type + 문자열 -> 문자열
// 		"" + 7 + 7 -> "7" + 7 -> "77"
//		7 + 7 +"" -> 14 + "" -> "14"	
		
// 실습 ====================================================
		System.out.println("실습================");
		char ch111 = 'A';
		System.out.println(ch111);
		
		int num = 'A';
		System.out.println(num);	// 문자 A의 문자코드(65)가 저장
		
		String str11 = "";	// 빈문자열(empty string)
		String str22 = "ABCD"; 
		String str33 = "123";
		String str44 = str22 + str33;
		System.out.println(str44);
		
		System.out.println(""+7+7);
		System.out.println(7+7+"");
		System.out.println("==============");
//==============================================================
		
// 9. 변수의 값 교환하기
		int x1 = 10, y1 = 20;
		int tmp;
		System.out.println(x1);
		System.out.println(y1);
		
		tmp = x1;
		x1 = y1;
		y1 = tmp;
		System.out.println("x=" + x1);
		System.out.println("y=" + y1);
//====================================================
		
		
		
		
		
		
		
		
		
		
		
		
	}

}
