document.getElementById('start-web').addEventListener('click', (e) => {
  document.getElementById('start-game-prompt').classList.add('hide');
  document.getElementById('my-board').classList.remove('hide');
  startGame()
})

document.getElementById('join-game').addEventListener('click', (e) => {
  joinGame()
})

const startGame = () => {
  document.getElementById('player-name').value == "" ? document.getElementById('player-name').value = "Bingus" : ""
  let name = document.getElementById('player-name').value == "" ? "Bingus" : document.getElementById('player-name').value
  document.getElementById('name-area').classList.add('hide');

  postData('/api/start_game', {"name": name}).then(data => {
    document.getElementById('header-text').innerHTML = "Game Code: " + data
    document.getElementById('game-code').value = data
  })
}

const joinGame = async () => {
  document.getElementById('player-name').value == "" ? document.getElementById('player-name').value = "Bingus" : ""
  let name = document.getElementById('player-name').value == "" ? "Bingus" : document.getElementById('player-name').value
  let code = document.getElementById('game-code-input').value
  document.getElementById('header-text').innerHTML = "Game Code: " + code
  document.getElementById('game-code').value = code

  postData('/api/join_from_web', {"name": name, "code": code}).then(data => {
    document.getElementById('start-game-prompt').classList.add('hide');
    document.getElementById('my-board').classList.remove('hide');
    document.getElementById('name-area').classList.add('hide');
    if(data) {
      if(!data['ready']) {
        console.log(data);
        document.getElementById('header-text').innerHTML = "Game Code: " + code
        document.getElementById('game-code').value = code

      }
      else {
        buildBoard("my-board", data['player-board']['occupied-spaces'])
        buildBoard("enemy-board", data['enemy-board']['attack-spaces'])
        confirmSetup()
      }
    }
    else {
      document.getElementById('header-text').innerHTML = "An Error Occurred"
    }

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


const checkGameStatus = (loop=true) => {
  let name = document.getElementById('player-name').value
  let code = document.getElementById('game-code').value
  postData('/api/check_game_status', {"name": name, "code": code}).then(data => {
    console.log(data);
    buildBoard("my-board", data['player-board']['occupied-spaces'])
    buildBoard("enemy-board", data['enemy-board']['attack-spaces'])


    setTimeout(checkGameStatus, 1000);
  })
}
