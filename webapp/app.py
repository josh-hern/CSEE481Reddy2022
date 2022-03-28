from flask import Flask

import initialize_game as game
from api.routes import api

app = Flask(__name__, template_folder='./views')
app.development = True
app.register_blueprint(api)

if __name__ == "__main__":
    game.initialize_game()
    # print('got here')
    app.run(debug=True)
