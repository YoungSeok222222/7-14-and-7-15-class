const myInfo = {
    name : 'jack',
    phoneNumber : '123456',
    'samsung product' : {
        buds : 'Buds pro',
        galaxy : 'S99',
    }
}


console.log(myInfo.name)
console.log(myInfo['name'])

console.log(myInfo['samsung product'])
console.log(myInfo['samsung product'].galaxy)




const obj = {
    name : 'jack',
    greeting() {
        console.log('hi!')
    }
}

console.log(obj.name)
console.log(obj.greeting())



const key = 'country'
const value = ['한국', '미국', '일본', '중국']

const myObj = {
    [key] : value,
}

console.log(myObj)
console.log(myObj)







const jsonData = {
    coffee : 'Americano',
    iceCream : 'Min Choco',

}

// Object -> json
const objToJson = JSON.stringify(jsonData)
console.log(objToJson)


// json -> Object
const jsonToObj = JSON.parse(objToJson)
console.log(jsonToObj)              
console.log(typeof jsonToObj)       // object



