const a = 13
const b = -5
const c = 3.14
const d = 2.998e8
const e = Infinity
const f = -Infinity
const g = NaN // Not a number
console.log(g)
console.log(Number.isNaN(37))
console.log('===========================')
// ===================================================

// 문자열을 표현하는 자료형
console.log('문자열을 표현하는 자료형')
const name1 = 'Tony'
const name2 = 'Stark'
const fullName = name1 + name2
console.log('곱셈, 나눗셈, 뺄셈은 안되지만 덧셈을 통해 문자열을 붙일 수 있음')
console.log(name1+name2, fullName)
console.log('===========================')

console.log('escape sequence')
const word1 = '안녕\n하세요'
console.log(word1)
console.log('===========================')

console.log('Template Literal == Backtick(``)')
const word2 = `안녕들   
하세요`         // template literal (``) 혹은 Backtick으로 부름
console.log(word2)
console.log('===========================')

const age = 10
const message = `금쪽이는 ${age}세 입니다.`
console.log(message)
console.log('===========================')

// Empty Value 값이 존재하지 않음을 표현하는 값 == null / undefined 2개 존재 이유는 단순 설계 실수
let nullName = null
console.log(nullName)

let undefinedName
console.log(undefinedName)
console.log('===========================')

// 할당 연산자
console.log('할당 연산자')
let c2 = 5
c2 += 10
console.log(c2)

c2 -=9
console.log(c2)

c2 *= 10
console.log(c2)

c2++
console.log(c2)

c2--
console.log(c2)
console.log('===========================')

// 비교 연산자
console.log('비교 연산자')
console.log(3 > 2)
console.log(3 < 2)
console.log('A' < 'B')
console.log('Z' < 'a')
console.log('가'< '나')
console.log('===========================')

// 동등 연산자(==)
console.log('동등 연산자==')
const a1 = 1
const b1 = '1'
console.log(a1 == b1)
console.log(a1 == true)
console.log(8*null) // 0, null은 0
console.log('5'- 1)
console.log('5'+ 1)
console.log('five'*2)
console.log('===========================')

// 일치 연산자(===) 값과 타입이 같으면 true 반환 / 엄격한 비교가 이뤄지며 암묵적 타입 변환이 발생하지 않음
console.log('일치 연산자(===)')
const a3 = 1
const b3 = '1'
console.log(a3===b3)
console.log(a3===Number(b3))
console.log('===========================')

// 논리 연산자(세 가지 논리 연산자로 구성)
console.log('논리 연산자(&&는 and, ||는 or, !는 not')
console.log('&&', true && false)
console.log('&&', true && true)
console.log('||', true || false)
console.log('||', true || true)
console.log('!',! true)
// 단축 평가 지원 ex) false && true => false
console.log('단축 평가 지원 && / ||')
console.log('&&', 4 && 7)
console.log('||', 4 || 7)
console.log('===========================')

// 삼항 연산자(Ternary Operator) / 조건이 참이면 :(콜론) 앞의 값 반환, 반대의 경우 뒤의 값 반환되는 연산자
// ? 앞까지가 조건, 그 뒤가 참, 거짓일 경우 반환되는 값
console.log('삼항 연산자')
console.log(true ? 1:3)
console.log(false ? 1:3)
console.log('===========================')

// 조건문(if, switch)
console.log('조건문-if/ else if/ esle')
const name3 = 'manager'
if (name3==='admin') {
    console.log('관리자님 환영합니다.')
} else if (name3==='manager'){
    console.log('매니저님 환영합니다.')   
} else {
    console.log(`${name3}님 환영합니다.`)
}


