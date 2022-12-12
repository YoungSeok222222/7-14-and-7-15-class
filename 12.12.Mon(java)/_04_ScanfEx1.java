// 화면으로부터 입력받기

import java.util.*;	 // 1. import문 추가
//import java.util.Scanner;

public class _04_ScanfEx1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// 2. Scanner 클래스의 객체 생성
		Scanner scanner = new Scanner(System.in);
		
//		int num = scanner.nextInt();	// 하나의 값을 입력받기
//		int num2 = scanner.nextInt();
//		System.out.println(num);
//		System.out.println(num2);
		
		String input = scanner.nextLine(); // 라인 단위로 입력 받기
		int num3 = Integer.parseInt(input);
		
		System.out.println(num3);
	}

}
