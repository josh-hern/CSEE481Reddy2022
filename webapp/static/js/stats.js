// // essentially this will take whatever username the person enters, run the
// // check_stats function in GameController.py, and then output it in a table view
// window.onload = () => {
//   setupListeners();
//   getGameStats();
// }
//
// const setupListeners = () => {
//   allCells = document.querySelectorAll("#old_stats td.table-cell");
// }
//
// const createTable = (gameStats) => {
//   let table = document.getElementById("stats-table");
//   let i = 0
//   for (let dict_key in gameStats){
//     i = i + 1
//     let row = table.insertRow(i)
//     let cell1 = row.insertCell(0);
//     let cell2 = row.insertCell(1);
//     let cell3 = row.insertCell(2);
//     cell2.innerHTML = dict_key;
//     cell3.innerHTML = dict_key.0;
//     cell4.innerHTML = dict_key.1;
//   })
// }
