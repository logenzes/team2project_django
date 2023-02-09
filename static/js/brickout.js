var canvas = document.getElementById("myCanvas");
console.log(canvas);
var ctx = canvas.getContext("2d");
var ballRadius = 10;//원 반지름 대입 변수
var x = canvas.width / 2; //공 최초 위치
var y = canvas.height - 30;
var dx = 6;// x y 이동속도
var dy = -6;
var paddleHeight = 15; //paddle의 높이
var paddleWidth = 85  ; //paddle의 넓이 원본75 인데 벽돌넓이와 맞춤
var paddleX = (canvas.width - paddleWidth) / 2; //패들의 x 축 시작지점
var rightPressed = false; //좌 혹은 우 키보드가 늘렸는지
var leftPressed = false;


var brickRowCount = 7;
var brickColumnCount = 12;

var brickHeight = 20;
var brickPadding = 1;  //원본은 10이지만 1로 하겠다.
var brickOffsetTop = 50; // 캔버스 탑에서 떨어진 정도
var brickOffsetLeft = 15; // 캔버스 좌측에서 떨어진 정도
var brickWidth = (canvas.width-(brickOffsetLeft*2)-(brickColumnCount*brickPadding))/brickColumnCount;
var score = 0;
var lives = 3; //남은 생명 수

var bricks = [];
var audio_clear = new Audio('002. Running Through the New World [Loop].mp3');
var audio_play = new Audio('1-02 The Star Festival.mp3');
var audio_gameover = new Audio('2-49 Sad Girl.mp3');
//var img = document.createElement("img");

//img.src = "./image/gameover.jpg";
//var x = document.images


for (var r = 0; r < brickRowCount; r++) {
    bricks[r] = [];
    for (var c = 0; c < brickColumnCount; c++) {
        bricks[r][c] = { x: 0, y: 0, status: 1 };
    }
}
document.addEventListener("keydown", keyDownHandler, false);
document.addEventListener("keyup", keyUpHandler, false);
//document.addEventListener("mousemove", mouseMoveHandler, false);
//키를 누르거나 손에서 떼면 알림

function keyDownHandler(e) {
    if (e.key == "Right" || e.key == "ArrowRight") { //키코드 39는 오른쪽
        rightPressed = true;
    }
    else if (e.key == "Left" || e.key == "ArrowLeft") { //키코드 37은 왼쪽
        leftPressed = true;
    }
}

function keyUpHandler(e) {
    if (e.key == "Right" || e.key == "ArrowRight") {
        rightPressed = false;
    }
    else if (e.key == "Left" || e.key == "ArrowLeft") {
        leftPressed = false;
    }
}
// 키를 누르면 변수가 true로 설정 손떼면 false로 되돌아감

function collisionDetection() { //공이 벽돌을 감지
    for (var c = 0; c < brickColumnCount; c++) {
        for (var r = 0; r < brickRowCount; r++) {
            var b = bricks[r][c];
            if (b.status == 1) {
                if (x > b.x && x < b.x + brickWidth && y > b.y && y < b.y + brickHeight) {
                    dy = -dy;
                    b.status = 0;
                    score++;
                    if (score == brickRowCount * brickColumnCount) {
                        audio_play.pause();
                        audio_clear.play();
                        alert("YOU WIN, CONGRATULATIONS!");
                        document.location.reload();
                    }
                    //승리메세지
                }
            }
        }
    }
}
//공의 x 좌표는 벽돌의 x 좌표보다 커야 한다.
//공의 x 좌표는 벽돌의 x 좌표 + 가로 길이보다 작아야 한다.
//공의 y 좌표는 벽돌의 y 좌표보다 커야 한다.
//공의 y 좌표는 벽돌의 y 좌표 + 높이보다 작아야 한다.

function drawScore() { //점수코드
    ctx.font ="bold 30px Arial";
    ctx.fillStyle = "#0095DD";
    ctx.fillText("Score: " + score, 8, 30);
}

function drawLives() { //생명 코드
    ctx.font = "bold 30px Arial";
    let color = "#0095DD";
    console.log(lives)
    if (lives<3&&lives>=2){
        console.log(lives)
        color = "#AC58FA";
    }
    else if (lives<2){
        console.log(lives)
        color = "#FE2E2E";
    }
    ctx.fillStyle = color;
    ctx.fillText("Lives: " + lives, canvas.width - 125, 30);
}
function drawBall() { //프레임 마다 공의 이동 구현
    ctx.beginPath();
    ctx.arc(x, y, ballRadius, 0, Math.PI * 2);
    ctx.fillStyle = "#D8D8D8"; //공색깔#0095DD
    ctx.fill();
    ctx.closePath();
}

function drawPaddle() { //패들을 스크린에 그리기
    ctx.beginPath();
    ctx.rect(paddleX, canvas.height - paddleHeight, paddleWidth, paddleHeight);
    ctx.fillStyle = "#8181F7";
    ctx.fill();
    ctx.closePath();
}

function drawBricks() {
    color1 = ['#FE2E2E', '#FE9A2E', '#F7FE2E','#9AFE2E','#2EFE2E', '#2EFE9A', '#2EFEF7', '#2E9AFE', '#2E2EFE', '#9A2EFE', '#FE2EF7', '#FE2E9A']
    color2 = ['#FF0000', '#FF8000', '#FFFF00','80FF00','#00FF00', '#00FF80', '#00FFFF', '#0080FF', '#0000FF', '#8000FF', '#FF00FF', '#FF0080']
    //color2 = ['']
    for (var c = 0; c < brickColumnCount; c++) {
        for (var r = 0; r < brickRowCount; r++) {
            if (bricks[r][c].status == 1) {
                var brickX = (c * (brickWidth + brickPadding)) + brickOffsetLeft;
                var brickY = (r * (brickHeight + brickPadding)) + brickOffsetTop;
                //모든 벽돌이 (0,0)에 있지 않도록 하기 위해(벽돌크기+오프셋+패딩)
                bricks[r][c].x = brickX; //각 리스트의 벽돌을 해당위치에 할당
                bricks[r][c].y = brickY;
                ctx.beginPath();
                ctx.rect(brickX, brickY, brickWidth, brickHeight);
                ctx.fillStyle = color1[c];
                //ctx.fillStyle = document.getElementByID(color1[0][c]);
                //ctx.fillStyle = 'rgb(' + Math.floor(255 - 36.4 * r) + ', ' + Math.floor(255 - 21.25 * c) + ', 100)';

                //ctx.fillStyle = "#5F4C0B";
                ctx.strokeStyle = 'rgba(255, 0, 0, 0.5)';
                 //벽돌색깔#0095DD
                 bricks[1][1].fillStyle="#0095DD";
                ctx.fill();
                ctx.closePath();
            }
        }
    }
}
function draw() {


    ctx.clearRect(0, 0, canvas.width, canvas.height);// 공의 흔적 지우기
    drawBricks();
    drawBall();
    drawPaddle();
    drawScore();
    drawLives();
    collisionDetection(); //충돌감지 활성화
    audio_play.play();


    if (x + dx > canvas.width - ballRadius || x + dx < ballRadius) {
        dx = -dx;
    }// 공 좌우 튕기기 & 원의 중심이 아닌 경계선(반지름 더하면 됨)에 닿으면 튕김

    if (y + dy < ballRadius) {// 공 위아래 튕기기
        dy = -dy;
    }
    else if (y + dy > canvas.height - ballRadius) {
        if (x > paddleX && x < paddleX + paddleWidth) {
            dy = -dy;
        }
        //살고 밑에는 목숨차감
        else {
            lives--;
            if (!lives) {
                //src.appendChild(img);
                audio_play.pause();
                audio_gameover.play();
                console.log(score)
                alert("GAME OVER");

                document.location.reload();

            }
            else { // 재시작위치

                x = canvas.width / 2;
                y = canvas.height - 30;
                dx = 6;
                dy = -6;
                paddleX = (canvas.width - paddleWidth) / 2;
            }
            //  break;
        }
    }
    //공이 상좌우 외에 하면에 닿을 경우 게임오버라는 알림 생성

    if (rightPressed && paddleX < canvas.width - paddleWidth) {
        //패들이 캔버스 오른쪽 끝과 왼쪽 끝을 벗어나지 않도록 && 조건설정
        paddleX += 7;
    }
    else if (leftPressed && paddleX > 0) {
        paddleX -= 7;
    }
    // 패들을 좌 우로 움직일때 7픽셀씩 움직임.
    x += dx;
    y += dy;
    requestAnimationFrame(draw);
}

function drawcheck(){
    let conf  = confirm("게임을 시작하겠습니까?")
    console.log('draw')
    console.log(conf)
    if (!conf){
        console.log("돌아갑니다.")
    }else{
        draw();
    }
}

drawcheck();

// JavaScript 코드가 여기에 들어갈 것입니다.
function score1(){
    var textbox=document.getElementById(score).value;
}

