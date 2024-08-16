let batsman = document.getElementById("batsman");
let ball = document.getElementById("ball");
let scoreDisplay = document.getElementById("score");
let gameOverScreen = document.getElementById("game-over");
let finalScore = document.getElementById("final-score");

let batsmanPosition = 135;
let ballPositionX = Math.floor(Math.random() * 290);
let ballPositionY = 0;
let ballSpeed = 2;
let score = 0;
let gameInterval;

function moveBatsman(direction) {
    if (direction === 'left' && batsmanPosition > 0) {
        batsmanPosition -= 10;
    } else if (direction === 'right' && batsmanPosition < 270) {
        batsmanPosition += 10;
    }
    batsman.style.left = batsmanPosition + "px";
}

function startGame() {
    score = 0;
    ballSpeed = 2;
    ballPositionY = 0;
    ballPositionX = Math.floor(Math.random() * 290);
    scoreDisplay.textContent = score;
    gameOverScreen.classList.add("hidden");
    gameInterval = setInterval(updateGame, 20);
}

function updateGame() {
    ballPositionY += ballSpeed;
    ball.style.top = ballPositionY + "px";
    ball.style.left = ballPositionX + "px";

    if (ballPositionY > 480) {
        if (ballPositionX > batsmanPosition && ballPositionX < batsmanPosition + 30) {
            score++;
            scoreDisplay.textContent = score;
            ballPositionY = 0;
            ballPositionX = Math.floor(Math.random() * 290);
            ballSpeed += 0.2;
        } else {
            endGame();
        }
    }
}

function endGame() {
    clearInterval(gameInterval);
    finalScore.textContent = score;
    gameOverScreen.classList.remove("hidden");
}

document.addEventListener('DOMContentLoaded', (event) => {
    startGame();
});
