document.getElementById('start-web').addEventListener('click', (e) => {
  document.getElementById('start-game-prompt').classList.add('hide');
  document.getElementById('my-board').classList.remove('hide');
  startGame()
})

document.getElementById('join-game').addEventListener('click', (e) => {
  document.getElementById('start-game-prompt').classList.add('hide');
  document.getElementById('my-board').classList.remove('hide');
  joinGame()
})

const startGame = () => {
  document.getElementById('player-name').value == "" ? document.getElementById('player-name').value = "Bingus" : ""
  name = document.getElementById('player-name').value == "" ? "Bingus" : document.getElementById('player-name').value
  document.getElementById('name-area').classList.add('hide');

  postData('/api/start_game', {"name": name}).then(data => {
    document.getElementById('header-text').innerHTML = "Game Code: " + data
    document.getElementById('game-code').value = data
  })
}

const joinGame = () => {
  document.getElementById('player-name').value == "" ? document.getElementById('player-name').value = "Bingus" : ""
  name = document.getElementById('player-name').value == "" ? "Bingus" : document.getElementById('player-name').value
  document.getElementById('name-area').classList.add('hide');
  code = document.getElementById('game-code-input').value

  postData('/api/join_from_web', {"name": name, "code": code}).then(data => {
    document.getElementById('header-text').innerHTML = "Game Code: " + data
    document.getElementById('game-code').value = code
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
