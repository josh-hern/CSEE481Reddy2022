window.onload = () => {
  setupListeners();
}

let ships = {
  'Battleship': 3,
  'Carrier': 5,
  'Destroyer': 4,
  'Patrol Boat': 2,
  'Submarine': 3
}
let currentShipIndex = 0;

// ship: str of ship name
const setupListeners = () => {
  let shipKeys = Object.keys(ships);
  let shipName = shipKeys[currentShipIndex];
  let shipLength = ships[shipKeys[currentShipIndex]];

  allCells = document.querySelectorAll("td.table-cell");
  allCells.forEach((cell) => {
    cell.addEventListener('mouseover', ()=> {
      cell.style.backgroundColor = '#dedede';
      for (let i = 1; i < shipLength; i++) {
        let offset = parseInt(cell.dataset.x) + i
        let tmpCell = document.querySelector("[data-x='" + offset + "'][data-y='" + cell.dataset.y + "']");
        tmpCell.style.backgroundColor = "#dedede";
      }
    })
    cell.addEventListener('mouseout', ()=> {
      cell.style.backgroundColor = 'white';
      for (let i = 1; i < shipLength; i++) {
        let offset = parseInt(cell.dataset.x) + i
        let tmpCell = document.querySelector("[data-x='" + offset + "'][data-y='" + cell.dataset.y + "']");
        tmpCell.style.backgroundColor = "white";
      }
    })
    cell.addEventListener('click', ()=> {
      cell.style.backgroundColor = 'white';
      for (let i = 1; i < shipLength; i++) {
        let offset = parseInt(cell.dataset.x) + i
        let tmpCell = document.querySelector("[data-x='" + offset + "'][data-y='" + cell.dataset.y + "']");
        tmpCell.style.backgroundColor = "white";
      }
    })
  })
}

// ship: object containing str key and int length
const placeShip = (ship) => {

}

// carrier 5
// destroyer 4
// battleship 3
// submarine 3
// patrol boat 2
