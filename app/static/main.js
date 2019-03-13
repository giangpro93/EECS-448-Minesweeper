var $_id = id => document.getElementById(id);

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

function updateBoard(data) {
    for(let i =0; i < rows; i++){
      for(let j = 0; j < cols; j++){
        var id = 'cell-' + i + '-' + j;
        if(data[i*cols+j] == '_'){
            //do nothing
            $_id(id).innerHTML = '&nbsp;';
            $_id(id).style.color = '#000000';
        }
        else if(data[i*cols+j] == 'f'){
            $_id(id).innerHTML = '&#9873';
            $_id(id).style.color = '#ff0000';
        }
        else{
            var numAdjacent = data[i*cols+j];
            switch (numAdjacent) {
                case 1:
                    $_id(id).style.color = 'blue'; break;
                case 2:
                    $_id(id).style.color = 'green'; break;
                case 3:
                    $_id(id).style.color = 'red'; break;
                case 4:
                    $_id(id).style.color = 'purple'; break;
                default:
                    $_id(id).style.color = 'black'; break;
            }
            $_id(id).style.background = '#EEE';
            if (numAdjacent!=0)
                $_id(id).innerHTML=numAdjacent;
        }
      }
    }
}

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
      if (data == "WINNER"){
        gameOver(true);
      }
      else if (data == "LOSER") {
        gameOver(false);
      }
      else{
        data = eval("data = " + data);
        updateBoard(data);
      }
    });
}

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
      if (data == "WINNER"){
        gameOver(true);
      }
      else if (data == "LOSER") {
        gameOver(false);
      }
      else{
        data = eval("data = " + data);
        updateBoard(data);
      }
    });
}

function gameOver(isWon){
  ended=1;
  message = $_id("message");
  if(isWon){
    message.innerHTML="You've won $1B prize!!";
    message.style.color="green";
  }
  else{
    message.innerHTML="You've lost :(";
    message.style.color="red";
  }
}
