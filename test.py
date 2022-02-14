import flask


app = flask.Flask(__name__)


@app.route('/')
def index():
    return "nice"


@app.route('/gettocken')
def gettocken():
    return "tocken"


@app.route('/notgettocken')
def notgettocken():
    return "nottocken"


@app.route('/deletdata')
def deletdata():
    return "deletdata"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
