// essentially this will take whatever username the person enters, run the
// check_stats function in GameController.py, and then output it in a table view
window.onload = () => {
  setupListeners();
}

const setupListeners = () => {
  allCells = document.querySelectorAll("#old_stats td.table-cell");
}

var gameStats = {}  // This will be from the check_stats function,
//I just don't know how to call it

const createTable = () => {
  let table = document.getElementById("stats-table");
  let i = 0
  gameStats.forEach((dict_key){
    i = i + 1
    let row = table.insertRow(i)
    let cell1 = row.insertCell(0);
    let cell2 = row.insertCell(1);
    let cell3 = row.insertCell(2);
    cell2.innerHTML = dict_key;
    cell3.innerHTML = "gameStats[dict_key][0]";  // I don't know how to do this in js
    cell4.innerHTML = "gameStats[dict_key][1]";  // I don't know how to do this in js
  })
}
