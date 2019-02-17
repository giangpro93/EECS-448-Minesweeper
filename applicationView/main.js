$board = $('#board');

function onSubmit(){
  const rows = document.getElementById("num_rows").value;
  const cols = document.getElementById("num_cols").value;
  let form = document.getElementById("board-def");
  form.style.display = 'none';
  createUniqueID();
  createBoard(rows, cols);
  return false;
}

function createUniqueID(){
  let userID = Math.floor((Math.random() * 1000000) + 1);
}

function createBoard(r, c){
  for(let i =0; i < r; i++){
    const $row = $('<div>').addClass('row');
    for(let j = 0; j < c; j++){
      const $col = $('<div>').addClass('col hidden').attr('data-row', i).attr('data-col', j);
      $row.append($col);
    }
    $board.append($row);
  }
}

$board.on('click', '.col.hidden', function(){
    const $block = $(this);
    const rowVal = $block.data('row');
    const colVal = $block.data('col');

    console.log(rowVal, colVal);

    
})
