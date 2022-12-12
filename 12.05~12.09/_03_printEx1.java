
public class _03_printEx1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

// 1. 형식화된 출력 - printf()
	// ▶ println()의 단점 - 출력형식 지정불가
		
	// (1) 실수의 자리수 조절불가 - 소수점 n자리만 출력하려면?
		System.out.println(10/3); // 정수 / 정수하면 정수가 나온다.
		System.out.println(10.0/3); // 두 수 중 한 쪽을 실수로 바꾸면 실수 출력
	
	// (2) 10진수로만 출력된다. - 8진수, 16진수로 출력하려면?
		System.out.println(0x1A); // 26(10진수)
		System.out.println("==============");
		
	// ▶ printf()로 출력형식 지정가능
		System.out.println("printf()로 출력형식 지정가능");
		System.out.printf("%.2f%n", 10.0/3); // 소수점 둘째자리까지 출력
		System.out.printf("%d%n", 0x1A); // 26 %n으로 혹은 \n으로 출력 후 줄바꿈
		System.out.printf("%X\n", 0x1A); // 1A
		System.out.println("=================");
		
// 2. printf()의 지시자
	/*
	(1)
	 %b - 불리언(boolean)형식으로 출력
	 $d - 10진(decimal) 정수의 형식으로 출력
	 %o - 8진(octal) 정수의 형식으로 출력
	 %f - 부동 소수점(floating-point)의 형식으로 출력
	 %c - 문자(character)로 출력
	 %s - 문자열(string)로 출력
	 %x, %X - 16진(hexa-decimal) 정수의 형식으로 출력
	 $e, %E - 지수(exponent) 표현식의 형식으로 출력
	*/
		System.out.println("2진수 표현");
		System.out.printf("%s", Integer.toBinaryString(15)); // 2진수로 표현
		System.out.println();
		System.out.println("===========");
		
//  (2) 8진수와 16진수에 접두사 붙이기
		System.out.println("8진수와 16진수에 접두사 붙이기");
		System.out.printf("%#o", 15); // 접두사를 붙여서 출려갛려면 #을 넣는다.
		System.out.println();
		System.out.printf("%#x", 15); // 소문자 x는 소문자로
		System.out.println();
		System.out.printf("%#X", 15); // 대문자 x는 대문자로 출력됨
		System.out.println();
		System.out.println("=========");
		
//  (3) 실수 출력을 위한 지시자 %f - 지수형식 %e, 간략한 형식(%g)
		System.out.println("실수 출력을 위한 지시자 %f - 지수형식 %e, 간략한 형식(%g)");
		float f = 123.4567890f;
		System.out.printf("%f", f); // 소수점 아래 6자리 (정밀도는 7자리까지 즉, 7자리까지만 값이 정확)
		System.out.println();
		System.out.printf("%e", f); // 지수형식, e+02는 10의 제곱을 의미
		System.out.println();
		System.out.printf("%g", 123.456789); // 123.457 실수를 소수점 포함하여 7자리로 표현
		System.out.println();
		System.out.printf("%g%n", 0.00000001); // = 1.00000e-8  
		System.out.println("===========");
// 
		System.out.printf("[%5d]%n", 10);	// [    5]
		System.out.printf("[%-5d]%n", 10);	// [5    ]
		System.out.printf("[%05d]%n", 10);	// [00010]
		System.out.println("==========");
		
		double d = 1.23456789;
		System.out.printf("%14.10f%n", d); //   1.2345678900
		System.out.println("========");
		
		System.out.printf("[%s]%n", "www.naver.com"); // [www.naver.com]
		System.out.printf("[%20s]%n", "www.naver.com"); // [       www.naver.com]
		System.out.printf("[%-20s]%n", "www.naver.com"); // [www.naver.com       ]
		System.out.printf("[%.8s]%n", "www.naver.com"); // [www.nave]
		 
	}

}
