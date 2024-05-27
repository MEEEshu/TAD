import json 
from flask import Flask, request, Response

myfile = open('in.json','r')
datein = myfile.read()
#print(datein)

date = json.loads(datein)
#print(date)'

app = Flask(__name__)
#'/' inseamna home
#daca nu se pune nimic este acceptat implicit doar get
@app.route('/')
def f1():
    return json.dumps(date)

@app.route('/valori/<int:id>')
def f2():
    for d in date:
        if id == d['id']:
            return json.dumps(d)
    return Response(f'Parametrul cu id-ul {id} nu exista!', status = '204')

app.run(debug = True, port = 5555)