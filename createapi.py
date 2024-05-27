from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    print('s-a accesat /')
    return "<h3>salut </h3>bine ai venit pe pagina"

@app.route('/<valoare>')
def newRoute(valoare):
    print('am primit', valoare)
    return f"<h3>salut{valoare}! , mergem pe pagina mea si salut aici"

app.run(port = 5555, debug=True)