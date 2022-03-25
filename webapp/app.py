from flask import Flask

from api.routes import api
from webapp.database import database_interface

app = Flask(__name__, template_folder='./views')
app.development = True
app.register_blueprint(api)

if __name__ == "__main__":
    battleship_game = database_interface.GameConnector()
    app.run(debug=True)
