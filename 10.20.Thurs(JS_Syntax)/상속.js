class Person {
    // 생성할 때 호출되는 함수 (생성자)
    constructor(p_name, p_age) {
      // 인스턴스 변수 구간
      this.name = p_name
      this.age = p_age
    }
    // 인스턴스 함수(메서드)
    speak() {
      console.log(`내 이름은 ${this.name} 이다.`)
    }
  }
  
  class MBTI extends Person {
    constructor(p_name, p_age, p_mbti) {
      super(p_name, p_age)
      this.mbti = p_mbti
    }
    tell_mbti() {
      console.log(`내 MBTI 는 ${this.mbti} 입니다.`)
    }
    // speak() {
    //   console.log('자식의 speak !!!!')
    // }
  }
  
  // 인스턴스 생성 (new 연산자)
  const david = new Person('David')
  const ingu = new Person('Ingu', 40)
  
  // console.log(david.name)
  // console.log(david.age)
  // david.speak()
  
  const mbti_person = new MBTI('mbti', 30, 'intj')
  console.log(mbti_person.name)
  console.log(mbti_person.age)
  console.log(mbti_person.mbti)
  // 1. 먼저, MBTI 클래스에서 함수 탐색
  // 2. MBTI 클래스에 함수가 없다면, 부모인 Person 클래스에서 함수 탐색
  mbti_person.speak()
  mbti_person.tell_mbti()
  
  // Person 클래스에서는 tell_mbti 함수가 없으므로 에러남
  // david.tell_mbti()