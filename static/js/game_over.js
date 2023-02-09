var Game_Over = {
    preload : function() {
        game.load.image('gameover','/static/img/gameover.png');
    },

    create : function() {
        this.add.button(0, 0, 'gameover', this.startGame, this);

        game.add.text(235, 350, "LAST SCORE", {font: "bold 16px sans-serif", fill: "#46c0f9", align: "center"});
        game.add.text(350, 348, score.toString(), {font: "bold 20px sans-serif", fill: "#fff", align: "center"});
        let data = {'score':score};
        data = JSON.stringify(data);
        console.log(data);
        document.getElementById("score_value").value = data;
        document.getElementById("submit_button").click();
    },
    
    startGame: function() {
        this.startGame.start('Game');
    }
};