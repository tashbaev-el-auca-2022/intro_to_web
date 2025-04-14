function delayedMessage(message, delay) {
    setTimeout(() => {
        console.log(message);
    }, delay);
}

delayedMessage("Hello, after 3 seconds!", 3000);

console.log("Start");

setTimeout(() => {
    console.log("Inside setTimeout");
}, 2000);

console.log("End");

function startCounter() {
    let counter = 1;
    const intervalId = setInterval(() => {
        console.log("Counter:", counter);
        if (counter === 5) {
            clearInterval(intervalId);
        }
        counter++;
    }, 1000);
}

startCounter();

function fetchData() {
    return new Promise((resolve) => {
        setTimeout(() => resolve("Data received"), 2000);
    });
}

fetchData()
    .then((data) => console.log(data))
    .finally(() => console.log("Request completed"));

function fetchData1() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (Math.random() > 0.5) {
                resolve("Data received");
            } else {
                reject("Error: Failed to fetch data");
            }
        }, 2000);
    });
}

fetchData1()
    .then((data) => console.log(data))
    .catch((error) => console.error(error))
    .finally(() => console.log("Request completed"));