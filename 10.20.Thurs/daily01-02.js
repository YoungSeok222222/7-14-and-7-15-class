




function palindrome(str) {
  const reversed = str.split('').reverse().join('');
  return reversed === str ? true : false
}
    


function palinderome(str) {
  return str.split('').every((element, idx) => element === str[str.length - 1 - idx])

}


console.log(palindrome('level'))
console.log(palindrome('hi'))
// palindrome('hi')
  // 출력
  // palindrome('level') => true
  // palindrome('hi') => falses