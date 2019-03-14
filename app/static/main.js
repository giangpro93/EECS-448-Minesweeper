var $_id = id => document.getElementById(id);

var skullSymbol = "&#x1F480;";
var starSymbol = "&#x2b50;";
var flagSymbol = "&#9873;";
var spaceSymbol = "&nbsp;";
var bombSymbol = "&#x1F4A3;";

var rows = 0;
var cols = 0;
var mines = 0;
var userID = "";
var ended = 0;

window.onload=function()
{
    resetBoard();
}

// *** Refined by Giang ***
function resetBoard(){
  const url='api/createBoard';

  rows = $_id("rows").value;
  cols = $_id("cols").value;
  mines = $_id('mines').value;
  userID = $_id("userID").value;
  ended = 0;

  message = $_id("message");
  message.innerHTML="&nbsp";
  if(rows < 2 || cols < 2){
    message.innerHTML='The board must have at least 2 rows and 2 columns.';
    message.style.color="red";
    return;
  }

  if (mines < 1) {
    message.innerHTML='The board must have at least one mine!';
    message.style.color="red";
    return;
  }

  if(mines >= (rows*cols)){
    message.innerHTML="Too many mines!!! The maximum number of mines for this board is "+(rows*cols-1);
    message.style.color="red";
    return;
  }

  $.post(url, {
    json_string: JSON.stringify({rows: rows, cols: cols, mines: mines, userID: userID})
  });
  createBoard(rows, cols);
}

// *** Refined by Giang ***
function createBoard(rows, cols){
  board.innerHTML="";
  for (let row=0;row<rows;row++) {
    $_id('board').innerHTML+='<br>';
    for (let col=0;col<cols;col++) {
        var id = 'id="cell-'+ row +'-'+ col +'"';
        var classname = 'class="cell" ';
        var onclick = 'onclick="leftClick('+ row +','+ col +')" ';
        var oncontext = 'oncontextmenu="rightClick('+ row +','+ col +'); return false"';
        var button = '<button '+ id + classname + onclick + oncontext + '>&nbsp;</button>';
        $_id('board').innerHTML += button;
    }
  }
}

// *** refined by Giang ***
function updateBoard(data) {
    for(let i =0; i < rows; i++){
      for(let j = 0; j < cols; j++){
        var id = 'cell-' + i + '-' + j;
        if(data[i*cols+j] == '_'){
            //do nothing
            $_id(id).innerHTML = spaceSymbol;
            $_id(id).style.color = "black";
        }
        else if(data[i*cols+j] == 'f'){
            $_id(id).innerHTML = flagSymbol;
            $_id(id).style.color = "red";
        }
        else if(data[i*cols+j] == 'b'){
            $_id(id).innerHTML = bombSymbol;
            //$_id(id).style.color = 'red';
        }
        else {
            var numAdjacent = data[i*cols+j];
            switch (numAdjacent) {
                case 0:
                    $_id(id).style.color = 'white'; break;
                case 1:
                    $_id(id).style.color = 'blue'; break;
                case 2:
                    $_id(id).style.color = 'green'; break;
                case 3:
                    $_id(id).style.color = 'red'; break;
                case 4:
                    $_id(id).style.color = 'purple'; break;
                case 5:
                    $_id(id).style.color = 'maroon'; break;
                case 6:
                    $_id(id).style.color = 'turquoise'; break;
                case 7:
                    $_id(id).style.color = 'black'; break;
                case 8:
                    $_id(id).style.color = 'black'; break;
            }
            $_id(id).style.background = '#EEE';
            if (numAdjacent!=0)
                $_id(id).innerHTML=numAdjacent;
        }
      }
    }
}

// *** refined by Giang ***
function leftClick(row,col) {
    const url = 'api/selectSpace'
    if (ended) {
        ended++;
        if (ended>3) alert("C'mon, the game ended. There's nothing you can do.");
        return;
    }

    let data;
    //send row and col value in a string with JSON to url
    $.ajax({
      type: "POST",
      url: url,
      data: {
        json_string: JSON.stringify({rows: row, cols: col, rightClick: "false", userID: userID})
      },
      success: function(response){
        data = response;
      },
      dataType: 'text'
    }).done(function() {
        data = data.replace(/'/g, "\"");
        data = JSON.parse(data);
        if (data["status"] != "None") updateBoard(data);
        if (data["status"] == "Win") {
            gameOver(true);
        }
        if (data["status"] == "Lose") {
            gameOver(false);
        }
    });
}

// *** refined by Giang ***
function rightClick(row,col) {
    const url = 'api/selectSpace';
    if (ended) {
        ended++;
        if (ended>3) alert("C'mon, the game ended. There's nothing you can do.");
        return;
    }

    let data;
    $.ajax({
      type: "POST",
      url: url,
      data: {
        json_string: JSON.stringify({rows: row, cols: col, rightClick: "true", userID: userID})
      },
      success: function(response){
        data = response;
      },
      dataType: 'text'
    }).done(function() {
      data = data.replace(/'/g, "\"");
      data = JSON.parse(data);
      if (data["status"] == "DoneF"){
        var id = 'cell-' + row + '-' + col;
        if ($_id(id).innerHTML == spaceSymbol) {
            $_id(id).innerHTML = flagSymbol;
            $_id(id).style.color = "red";
        }
        else {
            $_id(id).innerHTML = spaceSymbol;
            $_id(id).style.color = "black";
        }
      }
    });
}

// *** refined by Giang ***
function gameOver(isWon){
  ended=1;
  message = $_id("message");
  if(isWon){
    message.innerHTML="You've won $1B prize!!";
    message.style.color="green";
    for (let row=0;row<rows;row++)
    for (let col=0;col<cols;col++) {
        var id = 'cell-' + row + '-' + col;
        if ($_id(id).innerHTML == spaceSymbol) {
            if ($_id(id).style.color == 'white')
                $_id(id).innerHTML = starSymbol;
            else {
                $_id(id).innerHTML = bombSymbol;
                $_id(id).style.color = 'black';
                $_id(id).style.backgroundColor = 'green';
            }
        }
    }
  }
  else{
    message.innerHTML="You've lost :(";
    message.style.color="red";
    for (let row=0;row<rows;row++)
    for (let col=0;col<cols;col++) {
        var id = 'cell-' + row + '-' + col;
        if ($_id(id).innerHTML == '&nbsp;')
        if ($_id(id).style.color != 'white') {
            $_id(id).innerHTML = skullSymbol;
            $_id(id).style.color = 'black';
            $_id(id).style.backgroundColor = 'red';
        }

    }
  }
}
