window.onload = () => {
  setupListeners();
}

const removeAllEventListeners = () => {
  allCells = document.querySelectorAll("td.table-cell");
  allCells.forEach((cell) => {
    let cellClone = cell.cloneNode(true);
    cell.parentNode.replaceChild(cellClone, cell);
  })
}


// let ships = {
//   'Battleship': 3,
//   'Carrier': 5,
//   'Destroyer': 4,
//   'Patrol Boat': 2,
//   'Submarine': 3
// }


let boardData = {
  'shipLengths': {
    'Battleship': 3,
    'Carrier': 5,
    'Destroyer': 4,
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

  allCells = document.querySelectorAll("td.table-cell");
  allCells.forEach((cell) => {
    cell.addEventListener('mouseover', () => {highlightSpaces(cell, shipLength)})
    cell.addEventListener('mouseout', () => {unHighlightSpaces(cell, shipLength)})
    cell.addEventListener('click', () => {placeShip(cell, shipName, shipLength)})
  })
}

const highlightSpaces = (cell, shipLength) => {
  console.log(cell)
  if(!hasConflicts(cell, shipLength)) {
    cell.style.backgroundColor = '#dedede';
    for (let i = 1; i < shipLength; i++) {
      let offset = parseInt(cell.dataset.x) + i
      let tmpCell = document.querySelector("[data-x='" + offset + "'][data-y='" + cell.dataset.y + "']");
      tmpCell.style.backgroundColor = "#dedede";
    }
  }
}

const unHighlightSpaces = (cell, shipLength) => {
  if(!hasConflicts(cell, shipLength)) {
    cell.style.backgroundColor = 'white';
    for (let i = 1; i < shipLength; i++) {
      let offset = parseInt(cell.dataset.x) + i
      let tmpCell = document.querySelector("[data-x='" + offset + "'][data-y='" + cell.dataset.y + "']");
      tmpCell.style.backgroundColor = "white";
    }
  }
}

const placeShip = (cell, shipName, shipLength) => {
  if(!hasConflicts(cell, shipLength)) {
    cell.style.backgroundColor = 'cyan';
    for (let i = 1; i < shipLength; i++) {
      let offset = parseInt(cell.dataset.x) + i
      let tmpCell = document.querySelector("[data-x='" + offset + "'][data-y='" + cell.dataset.y + "']");
      tmpCell.style.backgroundColor = "cyan";
    }
    removeAllEventListeners();
    pushShipToObject(cell, shipName, shipLength);
    if(currentShipIndex != 4){
      currentShipIndex++;
      setupListeners();
    }
  }
}

const pushShipToObject = (cell, shipName, shipLength) => {
  for (let i = 0; i < shipLength; i++) {
    let newObject = {
      [shipName]: [parseInt(cell.dataset.x)+i, parseInt(cell.dataset.y)]
    }
    boardData['aliveCells'].push(newObject);
  }
}

// returns bool if ship is in way
const hasConflicts = (cell, shipLength) => {
  for (let i = -1; i <= shipLength; i++) {
    let flag = (boardData['aliveCells'].some((ship) => {
      if((parseInt(cell.dataset.x) + i == ship[Object.keys(ship)[0]][0] && parseInt(cell.dataset.y) == ship[Object.keys(ship)[0]][1])) {
        return true;
      }
      return (false);
    }))
    if(flag || ((parseInt(cell.dataset.x) + i) > 11)) return true;
  }
  return false;
}
