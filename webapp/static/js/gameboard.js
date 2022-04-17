var dataset_y_to_letter = {
  1: 'A',
  2: 'B',
  3: 'C',
  4: 'D',
  5: 'E',
  6: 'F',
  7: 'G',
  8: 'H',
  9: 'I',
  10: 'J'
}

var dataset_y_to_number = {
  'A': 1,
  'B': 2,
  'C': 3,
  'D': 4,
  'E': 5,
  'F': 6,
  'G': 7,
  'H': 8,
  'I': 9,
  'J': 10
}

window.onload = () => {
  setupListeners();
  document.querySelector('#rotate-button').classList.remove('hide');
}

const removeAllEventListeners = () => {
  allCells = document.querySelectorAll("#my-board td.table-cell");
  allCells.forEach((cell) => {
    let cellClone = cell.cloneNode(true);
    cell.parentNode.replaceChild(cellClone, cell);
  })
}

const toggleRotate = () => {
  rotate = !rotate;
}

const removeRotate = () => {
  document.querySelector('#my-board #rotate-button').remove();
}


// false for horizontal, true for vertical
let rotate = false;

let boardData = {
  'shipLengths': {
    'Battleship': 4,
    'Carrier': 5,
    'Destroyer': 3,
    'Patrol Boat': 2,
    'Submarine': 3
  },
  'aliveCells': [
    // 'Battleship': (x,y),
  ],
  'deadCells': [
    // 'Battleship': (x,y),
  ]
}


let currentShipIndex = 0;

// ship: str of ship name
const setupListeners = () => {
  let shipObject = boardData['shipLengths'];
  let shipKeys = Object.keys(shipObject);
  let shipName = shipKeys[currentShipIndex];
  let shipLength = boardData['shipLengths'][shipName];

  allCells = document.querySelectorAll("#my-board td.table-cell");
  allCells.forEach((cell) => {
    cell.addEventListener('mouseover', () => {highlightSpaces(cell, shipLength)})
    cell.addEventListener('mouseout', () => {unHighlightSpaces(cell, shipLength)})
    cell.addEventListener('click', () => {placeShip(cell, shipName, shipLength)})
  })

  document.querySelector('#command').innerHTML = "Place your: " + shipName;
}

const highlightSpaces = (cell, shipLength) => {
  if(!hasConflicts(cell, shipLength)) {
    cell.style.backgroundColor = '#dedede';
    if(rotate) {
      for (let i = 1; i < shipLength; i++) {
        let offset = parseInt(cell.dataset.y) + i
        let tmpCell = document.querySelector("#my-board [data-y='" + offset + "'][data-x='" + cell.dataset.x + "']");
        tmpCell.style.backgroundColor = "#dedede";
      }
    }
    else {
      for (let i = 1; i < shipLength; i++) {
        let offset = parseInt(cell.dataset.x) + i
        let tmpCell = document.querySelector("#my-board [data-x='" + offset + "'][data-y='" + cell.dataset.y + "']");
        tmpCell.style.backgroundColor = "#dedede";
      }
    }
  }
}

const unHighlightSpaces = (cell, shipLength) => {
  if(!hasConflicts(cell, shipLength)) {
    cell.style.backgroundColor = 'transparent';
    if(rotate) {
      for (let i = 1; i < shipLength; i++) {
        let offset = parseInt(cell.dataset.y) + i
        let tmpCell = document.querySelector("#my-board [data-y='" + offset + "'][data-x='" + cell.dataset.x + "']");
        tmpCell.style.backgroundColor = "transparent";
      }
    }
    else {
      for (let i = 1; i < shipLength; i++) {
        let offset = parseInt(cell.dataset.x) + i
        let tmpCell = document.querySelector("#my-board [data-x='" + offset + "'][data-y='" + cell.dataset.y + "']");
        tmpCell.style.backgroundColor = "transparent";
      }
    }
  }
}

const placeShip = (cell, shipName, shipLength) => {
  if(!hasConflicts(cell, shipLength)) {
    cell.style.backgroundColor = 'cyan';
    if(rotate) {
      for (let i = 1; i < shipLength; i++) {
        let offset = parseInt(cell.dataset.y) + i
        let tmpCell = document.querySelector("#my-board [data-y='" + offset + "'][data-x='" + cell.dataset.x + "']");
        tmpCell.style.backgroundColor = "cyan";
      }
    }
    else {
      for (let i = 1; i < shipLength; i++) {
        let offset = parseInt(cell.dataset.x) + i
        let tmpCell = document.querySelector("#my-board [data-x='" + offset + "'][data-y='" + cell.dataset.y + "']");
        tmpCell.style.backgroundColor = "cyan";
      }
    }
    removeAllEventListeners();
    pushShipToObject(cell, shipName, shipLength);
  }
}

const pushShipToObject = (cell, shipName, shipLength) => {
  if(rotate) {
    for (let i = 0; i < shipLength; i++) {
      let newObject = {
        [shipName]: [parseInt(cell.dataset.x), parseInt(cell.dataset.y)+i]
      }
      boardData['aliveCells'].push(newObject);
    }
  }
  else {
    for (let i = 0; i < shipLength; i++) {
      let newObject = {
        [shipName]: [parseInt(cell.dataset.x)+i, parseInt(cell.dataset.y)]
      }
      boardData['aliveCells'].push(newObject);
    }
  }
  const s = JSON.stringify({
    'position': dataset_y_to_letter[parseInt(cell.dataset.y)] + parseInt(cell.dataset.x),
    'ship_type': shipName,
    'rotate': rotate,
    'player': document.querySelector('#player-name').value,
    'code': document.querySelector('#game-code').value});

  postData('/api/place_ship', s).then(data => {
    buildBoard("my-board", data);
    confirmSetup()
  })
}

// returns bool if ship is in way
const hasConflicts = (cell, shipLength) => {
  if(rotate) {
    for (let i = -1; i <= shipLength; i++) {
      let flag = (boardData['aliveCells'].some((ship) => {
        if((parseInt(cell.dataset.y) + i == ship[Object.keys(ship)[0]][1] && parseInt(cell.dataset.x) == ship[Object.keys(ship)[0]][0]) || (parseInt(cell.dataset.y) + i == ship[Object.keys(ship)[0]][1] && parseInt(cell.dataset.x) + 1 == ship[Object.keys(ship)[0]][0]) || (parseInt(cell.dataset.y) + i == ship[Object.keys(ship)[0]][1] && parseInt(cell.dataset.x) - 1 == ship[Object.keys(ship)[0]][0])) {
          return true;
        }
        return (false);
      }))
      if(flag || ((parseInt(cell.dataset.y) + i) > 11)) return true;
    }
  }
  else {
    for (let i = -1; i <= shipLength; i++) {
      let flag = (boardData['aliveCells'].some((ship) => {
        if((parseInt(cell.dataset.x) + i == ship[Object.keys(ship)[0]][0] && parseInt(cell.dataset.y) == ship[Object.keys(ship)[0]][1]) || (parseInt(cell.dataset.x) + i == ship[Object.keys(ship)[0]][0] && parseInt(cell.dataset.y) + 1 == ship[Object.keys(ship)[0]][1]) || (parseInt(cell.dataset.x) + i == ship[Object.keys(ship)[0]][0] && parseInt(cell.dataset.y) - 1 == ship[Object.keys(ship)[0]][1])) {
          return true;
        }
        return (false);
      }))
      if(flag || ((parseInt(cell.dataset.x) + i) > 11)) return true;
    }
  }
  return false;
}

const buildBoard = (board, spaces) => {
  wipeBoard(board);
  spaces.forEach((space, i) => {
    let y = dataset_y_to_number[space['Position'][0]]
    let x = space['Position'].substring(1);
    let tmpCell = document.querySelector("#" + board + " [data-y='" + y + "'][data-x='" + x + "']");
    tmpCell.style.backgroundColor = "green";
  });

}

const wipeBoard = (board) => {
  for (let i = 1; i < 11; i++) {
    for (let j = 1; j < 11; j++) {
      let tmpCell = document.querySelector("#" + board + " [data-y='" + i + "'][data-x='" + j + "']");
      tmpCell.style.backgroundColor = "transparent";
    }
  }
}

const confirmSetup = (game, player) => {
  postData('/api/confirm_setup', {"name": document.querySelector('#player-name').value, "code": document.querySelector('#game-code').value}).then(data => {
    if(!data){
      currentShipIndex++;
      setupListeners();
    } else {
      removeAllEventListeners();
      removeRotate();
      document.querySelector("#enemy-board").classList.remove("hide");
      document.querySelector('#command').innerHTML = "Starting Game...";
      setTimeout(checkGameStatus, 1000)
    }
  })
}
