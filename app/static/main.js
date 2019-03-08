$board = $('#board');

var cols = null;
var rows = null;
let userID = null;

function onSubmit(){
  const url='api/createBoard';
  //get user input
  rows = document.getElementById("num_rows").value;
  cols = document.getElementById("num_cols").value;
  const mines = document.getElementById('num_mines').value;

  if(rows < 2 || cols < 2){
    if(!alert('Poor size values!')){window.location.reload();}
  }
  if(mines >= (rows*cols) || mines == 0){
    if(!alert('Poor mine number value!')){window.location.reload();}
  }

  userID = createUniqueID();

  $.post(url, {
    json_string: JSON.stringify({rows: rows, cols: cols, mines: mines, userID: userID})
  });
  createBoard(rows, cols);
  let form = document.getElementById('board-def');
  form.style.display = 'none';
  return false;
}

function createUniqueID(){
  //create random number for userID
  let userID = Math.floor((Math.random() * 1000000) + 1);
  return(userID);
}

function createBoard(r, c){

  //board generation through div
  for(let i =0; i < r; i++){
    const $row = $('<div>').addClass('row');
    for(let j = 0; j < c; j++){
      const $col = $('<div>').addClass('col hidden').attr('data-row', i).attr('data-col', j);
      $row.append($col);
    }
    $board.append($row);
  }
}

function gameOver(isWon){
  if(isWon){
        var win = window.open('https://winner.info/');
        if (win) {
          win.focus();
        }
        else {
          alert('Allow popups for Minesweeper');
        }
  }
  else{
      var win = window.open('http://www.losers.org/');
      if (win) {
        win.focus();
      }
      else {
        alert('Allow popups for Minesweeper');
      }
  }
  window.location.reload();
}

$board.on('contextmenu', '.col.hidden',function(e){
      const url = 'api/selectSpace';
      //disable context menu if right-click on board and post data
      const $block = $(this);
      const rowVal = $block.data('row');
      const colVal = $block.data('col');

      if(e.which == 3){
        e.preventDefault();
        const $thisSpace = $(`.col.hidden[data-row=${rowVal}][data-col=${colVal}]`);
        //$('<p><|</p>').appendTo($thisSpace);
        $.ajax({
          type: "POST",
          url: url,
          data: {
            json_string: JSON.stringify({rows: rowVal, cols: colVal, rightClick: "true", userID: userID})
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
          else {
            renderBoard(data);
          }
        });
      }
});

$board.on('click', '.col.hidden', function(e){
    const url = 'api/selectSpace'
    //get index on grid of click location
    const $block = $(this);
    const rowVal = $block.data('row');
    const colVal = $block.data('col');
    let data;
    //send row and col value in a string with JSON to url
    $.ajax({
      type: "POST",
      url: url,
      data: {
        json_string: JSON.stringify({rows: rowVal, cols: colVal, rightClick: "false", userID: userID})
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
        renderBoard(data);
      }
    });

function renderBoard(data) {
  $board.empty();
  data = eval("data = " + data);
  var countRow = 0;
  var countCol = 0;
  for (let i = 0; i < rows; i++) {
    const $row = $('<div>').addClass('row');
    for (let j = 0; j < cols; j++) {
      const $col = $('<div>').addClass('col hidden').attr('data-row', i).attr('data-col', j);
      if (data[i * cols + j] == '_') {
        $col.css("background-color", "grey");
      }
      else if (data[i * cols + j] == 'f') {
        $('<p><|</p>').appendTo($col);
      }
      else {
        var numAdjacent = data[i * cols + j];
        $('<p>' + numAdjacent + '</p>').appendTo($col)
        $col.css("background-color", "white");
      }
      $row.append($col);
    }
    $board.append($row);
  }
}

})
