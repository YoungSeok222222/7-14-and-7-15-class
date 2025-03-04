const products = [
    { name : 'cucumber', type : 'vegetable' },
    {name : 'banana', type : 'fruit'},
    {name : 'carrot', type : 'vegetable'},
    {name : 'apple', type : 'fruit'}
]

const fruitFilter = function(product) {
    return product.type === 'fruit'
}

const newArray = products.filter(fruitFilter)

console.log(newArray)


// 2.
const newArray = products.filter(function(product) {
    return product.type === 'fruit'
}
)

// 3.
const newArray = products.filter((product) => {
    return product.type === 'fruit'
}
)
