function parseJSON(jsonStr) {
    try {
        const parsedData = JSON.parse(jsonStr);
        console.log(parsedData);
    } catch (error) {
        console.error("Invalid JSON format");
    }
}

let nums = [10, 15, 20, 25, 30]

let sum = 0;

for (let num of nums) {
    console.log("Current number:", num);
    if (num % 2 === 0) {
        sum += num;
    }
}

console.log("Total sum:", sum);

const users = [
    { name: "Alice", age: 25 },
    { name: "Bob", age: 30 },
    { name: "Charlie", age: 22 }
];

console.table(users);

function divide(a, b){
  try {
    if(b===0){
      throw new Error("Can not divide by zero")
    }

    return a / b;
  }
  catch(error) {
    console.error(error.message)
  }
}
console.log(divide(25, 0))

try {
  console.log(somevar)
} catch(error){
  console.error("Var is not defined")
}