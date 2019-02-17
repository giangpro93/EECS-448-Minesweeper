$board = $('#board');

function onSubmit(){
  //get user input
  const rows = document.getElementById("num_rows").value;
  const cols = document.getElementById("num_cols").value;
  const mines = document.getElementById('num_mines').value;

  createUniqueID();
  createBoard(rows, cols);

  let form = document.getElementById('board-def');
  form.style.display = 'none';

  return false;
}

function createUniqueID(){
  //create random number for userID
  let userID = Math.floor((Math.random() * 1000000) + 1);
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

$board.bind('contextmenu', function(e){

      //disable context menu if right-click on board
      if(e.which == 3){
        event.preventDefault();
        $(this).click();
      }
});

$board.on('click', '.col.hidden', function(){

    //get index on grid of click
    const $block = $(this);
    const rowVal = $block.data('row');
    const colVal = $block.data('col');

    console.log(rowVal, colVal);

})
