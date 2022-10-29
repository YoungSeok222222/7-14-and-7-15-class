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
console.log('===========================')

// Switch statment - break 및 default문은 [선택적], break 없으면 default만날 때까지 다음 조건문 실행
// 조건이 많은 경우 switch문을 통해 가독성 향상을 기대할 수 있음
// 일반적으로 중첩 else if문은 유지보수하기 힘들다는 문제도 있음
console.log('Switch Statement')
let name4 = '탑건'
switch (name4) {
  case 'iceman':
      console.log("Now.. Who's the best pilot?")
      break
  case '탑건':
      console.log('Maverick: Talk to me Goose...')
      break;

  default:
      console.log(`${name4}님 환영합니다.`)
      break;
}
console.log('===========================')


// 반복문 - while, for, for... in, for... of
console.log('반복문')

// while
console.log('While') // 조건이 참이기만 하면 문장을 계속해서 수행
let num1 = 0
while (num1 <6) {
  console.log(num1)
  num1 += 1
}
console.log()
console.log('===========================')

// for  최초 정의한 i를 재할당 하면서 사용하기 때문에 const를 사용하면 error 발생
console.log('for') // 특정한 조건이 거짓으로 판별될 떄까지 반복

for (let i = 0; i<6; i++){ // for ([초기문]; [조건문]; [증감문]){}
  console.log(i)              // 1. 반복문 진입 및 변수 i 선언 => 2. 조건문 평가 후 코드 블럭 실행(여기서는 console.log(i)) =>
    // 3. 코드 블럭 실행 이후 i 값 증가
    
}
console.log()
console.log('===========================')

// for ... in "속성 이름"을 통해 반복

// 객체의 속성을 순회할 때 사용
// 배열도 순회 가능하지만 인덱스 순으로 순회한다는 보장이 없으므로 권장하지 않음
console.log('for... in') 
const fruits = {a : 'apple', b: 'banana'}

for (const key in fruits) {
  console.log(key)
  console.log(fruits[key])
}
console.log()
console.log('===========================')

// for ... of " 속성 값"을 통해 반복

// 반복 가능한 객체를 순회할 때 사용
// 반복 가능한(iterable) 객체의 종류: Array, Set, String 등
console.log('for...of')
const ar = [3, 5, 7, 9]

for (const i of ar){    // for ... of =>  속성 값
  console.log(i)
}

console.log('for in 으로 하는 경우')
for (const j in ar){    // for ... in => 속성 이름
  console.log(j)
}                       // const쓰는 이유: 재할당이 아니라, 매 반복시 해당 변수를 새로 정의하여 사용하므로 에러가 발생하지 않음
console.log()
console.log('===========================')


// 함수
console.log('함수')
console.log()

console.log('함수 선언식')
// 함수 선언식(function declaration)  호이스팅 발생(함수 선언 이전에 호출해도 동작)
function add(num1, num2){
  return num1 + num2  
}
console.log(add(2,9))
console.log()

// 함수 표현식(function expression)
console.log('함수 표현식')
const sub  = function(num1,num2){   // 함수 이름 생략한 익명함수인 경우
  return num1 - num2
}
console.log(sub(9,3))
console.log()

console.log('함수 이름 명시하는 경우')
const mySub = function namedSub(num1,num2){ // 함수 이름을 명시하는 것도 가능, 다만 이 경우 함수 이름은 호출에 사용되지 못하고 디버깅 용도로 사용
  return num1 - num2
}
console.log(mySub(1,9))
console.log()

console.log('기본 인자(Default arguments)') // 인자 작성 시 '=' 문자 뒤 기본 인자 선언 가능
const greeting = function (name='Anonymous'){
  return `Hi ${name}`
}
console.log(greeting())
console.log()

console.log('매개변수와 인자의 개수 불일치 허용(매개변수보다 인자의 개수가 많을 경우)')
const twoArgs = function (arg1,arg2){
  return [arg1, arg2]
}
console.log(twoArgs(1,2,3,4))
console.log()

console.log('매개변수보다 인자의 개수가 적을 경우')
const threeArgs = function(arg1,arg2,arg3){
  return[arg1,arg2,arg3]
}
console.log(threeArgs())
console.log(threeArgs(1))
console.log(threeArgs(1,2))
console.log()
console.log('===========================')

// Spread syntax
console.log('Spread syntax')

// 1. 배열과의 사용(배열 복사)
let parts = ['shoulders', 'knees']
let lyrics = ['head', ...parts, 'and', 'toes']
console.log(lyrics)
console.log()

// 2. 함수와의 사용(Rest parameters) - 정해지지 않은 수의 매개변수를 배열로 받을 수 있음
const restOpr = function (arg1,arg2,...restArgs){
  return [arg1, arg2, restArgs]
}
console.log(restOpr(1, 2, 3, 4, 5))
console.log()
console.log('===========================')

// 화살표 함수(Arrow Function)
console.log('화살표 함수')

const arrow_func = function (name){
  return `hello ${name}`
}

// 1. function 키워드 삭제
const arrow1 = (name) => {return `hello ${name}`}

// 2. 인자가 1개일 경우에만 () 생략 가능
const arrow2 = name => {return `hello ${name}`}

// 3. 함수 바디가 return을 포함한 표현식 1개일 경우에 {} & return 삭제 가능
const arrow3 = name => `hello ${name}`

// 화살표 함수 응용
// 1. 인자가 없다면? () or _로 표시 가능
let noArgs = () => 'No args'
noArgs = _ => 'No args'

// 2-1. object를 return 한다면
let returnObject = () => {return {key : 'value'}} // return을 명시적으로 적어준다.

// 2-2. return을 적지 않으려면 괄호를 붙여야 함
returnObject = () => ({key:'value'})
console.log('===========================')

// 즉시 실행 함수(IIFE, Immediately Invoked Function Expression)
// 선언과 동시에 실행되는 함수, 함수의 선언 끝에 '()'를 추가하여 선언되자 마자 실행하는 형태
console.log((function(num){return num**3})(2))
// (num5 => num5**3)(2)
console.log('===========================')

// Array와 Object - JavaScript의 데이터 타입 중 참조 타입(reference)에 해당, 객체는 속성들의 모음(collection)

// 배열  
// 순서 보장, 주로 대괄호[] 이용하여 생성, 0을 포함한 양의 정수 인덱스로 특정 값에 접근, 배열의 길이는 array.length, 배열 마지막 원소는 array.length - 1
console.log('배열')
const numbers2 = [1,2,3,4,5]
console.log(numbers2[0])
console.log(numbers2[-1])
console.log(numbers2.length)
console.log(numbers2[numbers2.length-3])
console.log()
console.log('===========================')

// 배열 메서드 기초
console.log('배열 메서드 기초')
console.log()

console.log('.reverse()')
const n5 = [2,5,8,9,3,4]
n5.reverse()
console.log(n5)
console.log()

console.log('push, pop')
const n6 = [9,6,2,5,4,1]
n6.push(100)
console.log(n6)

n6.pop()
console.log(n6)
console.log()

console.log('.includes(value)')
const n7 = [4,5,6,7,8,9]
console.log(n7.includes(1)) // false
console.log()

console.log('.indexOf(value')
const n8 = [1,3,5,7,9]
let re

re = n8.indexOf(5)  // 가장 첫 번째로 찾은 요소의 인덱스 반환, 없으면 -1 반환
console.log(re) // 2
console.log(n8.indexOf(100)) // -1
console.log()

console.log('join([separator])')  // 생략 시 쉼표를 기본 값으로 사용
const n9 = [2,4,6,8]
let re2

re2 = n9.join()
console.log(re2)

re2 = n9.join('')
console.log(re2)

re2 = n9.join(' ')
console.log(re2)

re2 = n9.join('-')
console.log(re2)
console.log('===========================')

// 배열 메서드 심화 - 메서드 호출 시 인자로 callback 함수를 받는 것이 특징
console.log('배열 메서드 심화')
console.log()

console.log('forEach')  // 인자로 주어지는 함수(콜백 함수)를 배열의 각 요소에 대해 한 번씩 실행, 반환 값 없음

// 1. 기본형
const colors = ['red', 'blue', 'green']

printFunc = function (color){
  console.log(color)
}
colors.forEach(printFunc)
console.log()

// 2. 함수 정의를 인자로 넣어보기
colors.forEach(function (color){
  console.log(color)
})
console.log()

// 3. 화살표 함수 적용하기  (반환값 없어서 화살표 함수는 return 넣는 듯)
colors.forEach((color) => {
  return console.log(color)
})
console.log()

console.log('map')  // 콜백 함수의 반환 값을 요소로 하는 새로운 배열 반환 (forEach + return)

const n10 = [3,4,5]

