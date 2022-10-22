console.log('hello, javascript')



//  함수 선언해서 합계 return (함수 선언식은 호이스팅(정의 되기 전에 함수 호출해도 가능))
function add(num1, num2) {
  return num1 + num2
}

console.log(add(2,7))
// ==============================================================================


// 변수 안에 함수 선언(표현식)
const sub = function (num1, num2) {
  return num1 - num2
}

console.log(sub(2,7))
// =============================================================================


// // 화살표 함수 (익명 함수이므로 함수 표현식에서만 사용 가능)
// // 원본
// const greeting = function (name) {
//   return `Hi ${name}`
// }

// // 1단계(function 키워드 생략 가능)   / 보통 1단계로 많이 표현
// const greeting = (name) => {
//   return `Hi ${name}`
// }

// // 2단계(함수의 매개 변수가 하나면 소괄호'()' 생략)
// const greeting = name => {
//   return `Hi ${name}`
// }

// // 3단계(함수의 내용(표현식)이 한 줄이면, '중괄호{}'와 'return' 생략)
// const greeting = name => `Hi ${name}`


// // 1. 인자가 없다면? () or _로 표현

// // 2-1. object를 return 한다면 
// let returnObject = () => {return { key: 'value' }} // return을 명시적으로 적어준다.

// // 2-2. return을 적지 않으려면 괄호를 붙여야 한다.






const numbers = [1, 2, 3, 4, 5]

console.log(numbers[0])
console.log(numbers[-1])
console.log(numbers[numbers.length-1])

numbers.reverse()
console.log(numbers)

numbers.push(100)
console.log(numbers)

numbers.pop()
console.log(numbers)


console.log(numbers.includes(1))
console.log(numbers.includes(100))

console.log(numbers.indexOf(3))
console.log(numbers.indexOf(100))


console.log(numbers.join())
console.log(numbers.join(''))
console.log(numbers.join(' '))
console.log(numbers.join('-'))

