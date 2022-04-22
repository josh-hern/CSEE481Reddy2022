document.getElementById('search_gamer_tag').addEventListener('click', (e) => {
  document.getElementById('old_stats').classList.remove('hide');
  statsTable.innerHTML = originalTable
  getGameStats();
})
statsTable = document.getElementById("stats-table");
let originalTable = statsTable.innerHTML

const getGameStats = () => {
  let name = document.getElementById('player-name').value == "" ? "testName" : document.getElementById('player-name').value
  postData('/api/check_stats', {"name": name}).then(data => {
    console.log(data);
    createTable(data)
  })
}

async function postData(url = '', data = {}) {
  // Default options are marked with *
  const response = await fetch(url, {
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
    mode: 'cors', // no-cors, *cors, same-origin
    cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
    credentials: 'same-origin', // include, *same-origin, omit
    headers: {
      'Content-Type': 'application/json'
      // 'Content-Type': 'application/x-www-form-urlencoded',
    },
    redirect: 'follow', // manual, *follow, error
    referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
    body: JSON.stringify(data) // body data type must match "Content-Type" header
  });
  return response.json(); // parses JSON response into native JavaScript objects
}

const createTable = (gameStats) => {
  let table = document.getElementById("stats-table");
  let i = 0
  for (let dict_key in gameStats){
    i = i + 1
    let row = table.insertRow(i)
    let cell1 = row.insertCell(0);
    let cell2 = row.insertCell(1);
    let cell3 = row.insertCell(2);
    let cell4 = row.insertCell(3);
    let cell5 = row.insertCell(4);
    cell1.innerHTML = dict_key;
    cell2.innerHTML = "     "
    cell3.innerHTML = gameStats[dict_key][0];
    cell4.innerHTML = "     "
    cell5.innerHTML = gameStats[dict_key][1];
  }
}
