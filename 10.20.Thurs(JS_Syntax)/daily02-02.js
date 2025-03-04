const users = [
  { name: "John", age: 31, isMarried: true, balance: 100 },
  { name: "Sarah", age: 22, isMarried: false, balance: 200 },
  { name: "Ashley", age: 25, isMarried: true, balance: 300 },
  { name: "Robert", age: 27, isMarried: false, balance: 400 },
  { name: "Tom", age: 35, isMarried: true, balance: 500 },
];


// 1. forEach 메서드를 활용해 모든 사용자들의 이름을 출력하시오.
users.forEach((user) => console.log(user.name)) 


// 2. filter 메서드를 활용해 결혼한 사람들만 모아 married 상수에 할당하시오.
// filter에 적용될 함수 = return을 포함한 하나의 표현식
// const married = users.filter((user) => {return user.isMarried})

const married = users.filter((user) => user.isMarried)
console.log(married)

// 3. find 메서드를 활용해 이름이 Tom인 사람만 tom 상수에 할당하시오.
const tom = users.find((user) => user.name === 'Tom')
console.log(tom)

// 4. map 메서드를 활용해 모든 사용자에게 isAlive 키를 추가하고 true로 설정한 뒤, newUsers 상수에 할당하시오.
const newUsers = users.map((user) => {
  user.isAlive = true
  return user
})
console.log(newUsers)

// 5. reduce 메서드를 활용해 모든 사용자들의 계좌잔액을 totalBalance 상수에 할당하시오.
// 원래 식 const totalBalance = users.reduce((total, user) => {return total + user.balance},0)
const totalBalance = users.reduce((total, user) =>  total + user.balance,0)
console.log(totalBalance)








