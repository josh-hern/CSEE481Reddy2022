from flask import Flask

from api.routes import api

app = Flask(__name__, template_folder='./views')
app.development = True
app.register_blueprint(api)

if __name__ == "__main__":
    app.run(debug=True)
