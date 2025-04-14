let fruits = []

fruits.push("apple","banana","cherry")

let fruits2 = fruits.pop()

console.log(fruits)

let nums = [10, 20, 30, 40, 50]

let nums2 = nums.slice(1, 3)

console.log(nums2)

let numbers = [1, 2, 3];

let a = numbers.map(num => num * num);

console.log(numbers)
console.log(a)

let ages = [12, 18, 25, 30, 15];

console.log(ages.filter(age => age >=18))

let user = {
  name:"Alice",
  age: 30,
  city:"Developer"
}

console.log(user.name)

user.age = 26;

console.log(user.age)

let car = {
  brand:"Tesla",
  model: "Model S",
  year: 2023
}

console.log(Object.keys(car))


console.log(Object.values(car))