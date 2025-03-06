// Lab 1: for Loop
function forLoop() {
    for (let i = 1; i <= 10; i++) {
        console.log(i);
    }
}

// Lab 2: while Loop
function whileLoop() {
    let num = 10;
    while (num >= 1) {
        console.log(num);
        num--;
    }
}

// Lab 3: do...while Loop
function doWhileLoop() {
    let userInput;
    do {
        userInput = parseInt(prompt("Enter a number greater than 10:"));
    } while (userInput <= 10);
    console.log(`You entered: ${userInput}`);
}

// Lab 4: Array with for Loop
function forLoopArray() {
    let fruits = ["Apple", "Banana", "Cherry", "Grapes", "Orange"];
    for (let i = 0; i < fruits.length; i++) {
        console.log(fruits[i]);
    }
}

// Lab 5: Array with while Loop
function whileLoopArray() {
    let fruits = ["Apple", "Banana", "Cherry", "Grapes", "Orange"];
    let i = 0;
    while (i < fruits.length) {
        console.log(fruits[i]);
        i++;
    }
}

// Lab 6: break
function breakLoop() {
    let numbers = [3, 7, 12, 5, 9];
    for (let num of numbers) {
        if (num === 12) {
            console.log("Number 12 found, stopping loop.");
            break;
        }
        console.log(num);
    }
}

// Lab 7: continue
function continueLoop() {
    let numbers = [1, 2, 3, 4, 5, 6, 7];
    for (let num of numbers) {
        if (num === 5) continue;
        console.log(num);
    }
}
