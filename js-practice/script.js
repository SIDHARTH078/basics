//script.js
function sayhello(){
    alert("welcome to javascript practice");
}

function what(){
    alert("what is javascript?");
}

// ...existing code...

// Simple car game function
function startCarGame() {
    let carPosition = 0;
    let roadLength = 20;
    let gameInterval = setInterval(() => {
        carPosition++;
        let road = "-".repeat(carPosition) + "🚗" + "-".repeat(roadLength - carPosition);
        console.clear();
        console.log(road);
        if (carPosition >= roadLength) {
            clearInterval(gameInterval);
            alert("You reached the finish line!");
        }
    }, 200);
}

// Call startCarGame() to play in the browser console
// ...existing code...
    
