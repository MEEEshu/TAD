#tema 2
#am creat o lista cu informatii auto
#am accesat mai multe metode html : GET, POST, PATCH, PUT, DELETE, TRACE, HEAD
#02.04.2024 - prima modificare
#Isachi Mihai

from flask import Flask, jsonify, request

app = Flask(__name__)


#dictionar masini
cars = [
    { "id": 1, "brand": "Toyota", "model": "Corolla", "an": 2019 },
    { "id": 2, "brand": "Honda", "model": "Civic", "an": 2020 },
    { "id": 3, "brand": "Lancia", "model": "Delta", "an": 2006 },
    { "id": 4, "brand": "Skoda", "model": "Octavia", "an": 2007 },
    { "id": 5, "brand": "VW", "model": "Polo", "an": 2021 },
    { "id": 6, "brand": "Hyundai", "model": "I30", "an": 2018 },
    { "id": 7, "brand": "Opel", "model": "Astra", "an": 2012 },
    { "id": 8, "brand": "Daewoo", "model": "Cielo", "an": 1997 },
    { "id": 9, "brand": "Mitsubishi", "model": "Lancer", "an": 2003 }
]


@app.route('/')
#functie care initiaza conexiunea http
def home():
    print('A fost accesata pagina lui Isachi Mihai /')
    return "<h3>Bine ai venit pe pagina mea!</h3> Sper sa iti placa. Wish you well </br>"

@app.route('/<username>')
#functie care initiaza conexiunea http - putem accesa un anumit username pentru a primi un mesaj personalizat
def Username(username):
    print('primit:',username)
    return f"<h3>Bine ai venit pe pagina mea {username}!</h3> Sper sa iti placa. Wish you well </br>"

# Endpoint pentru obținerea tuturor mașinilor
@app.route('/api/cars', methods=['GET'])
#functie care primeste metoda http get
def get_cars():
    return jsonify(cars)

# Endpoint pentru obținerea unei mașini după ID
@app.route('/api/cars/<int:car_id>', methods=['GET'])
#functie care primeste metoda http get pentru fiecare index din cheia 'id'
def get_car(car_id):
    car = next((car for car in cars if car['id'] == car_id), None)
    if car is None:
        return jsonify({'error': 'Mașina nu a fost găsită'}), 404
    return jsonify(car)

# Endpoint pentru adăugarea unei noi mașini
@app.route('/api/cars', methods=['POST'])
#functie care primeste metoda http post
def add_car():
    #request de date prin http
    data = request.json
    if 'brand' not in data or 'model' not in data or 'an' not in data:
        #returnam mesaj la eroare
        return jsonify({'error': 'Toate câmpurile (brand, model, an) sunt obligatorii'}), 400
    car = {
        'id': len(cars) + 1,
        'brand': data['brand'],
        'model': data['model'],
        'an': data['an']
    }
    #adauga la dictionar o alta tupla cu chei si valori
    cars.append(car)
    return jsonify(car), 201

# Endpoint pentru actualizarea parțială a unei mașini după ID
@app.route('/api/cars/<int:car_id>', methods=['PATCH'])
#functie care primeste metoda http patch
def partial_update_car(car_id):
    #request de date prin http
    data = request.json
    #cautam masina pe baza id-ului
    car = next((car for car in cars if car['id'] == car_id), None)
    if car is None:
        #returnam mesaj la eroare
        return jsonify({'error': 'Mașina nu a fost găsită'}), 404
    #se updateaza partial dictionarul CARS
    car.update(data)
    return jsonify(car)

# Endpoint pentru actualizarea unei mașini după ID
@app.route('/api/cars/<int:car_id>', methods=['PUT'])
#functie care primeste metoda http patch
def update_car(car_id):
    #request de date prin http
    data = request.json
    car = next((car for car in cars if car['id'] == car_id), None)
    if car is None:
        #returnam mesaj la eroare
        return jsonify({'error': 'Mașina nu a fost găsită'}), 404
    #se updateaza complet dictionarul CARS
    car.update(data)
    return jsonify(car)

# Endpoint pentru ștergerea unei mașini după ID
@app.route('/api/cars/<int:car_id>', methods=['DELETE'])
#functie care primeste metoda http delete
def delete_car(car_id):
    global cars
    cars = [car for car in cars if car['id'] != car_id]
    return '', 204

# Endpoint pentru testarea căii de la client la server
@app.route('/api/cars', methods=['TRACE'])
#functie care primeste metoda http trace - testeaza conexiunea si primim un mesaj de confirmare
def trace():
    return jsonify({'message': 'Acesta este un test de tip TRACE. cod : 200'}), 200

# Endpoint pentru obținerea informațiilor despre o resursă fără a solicita corpul răspunsului
@app.route('/api/cars', methods=['HEAD'])
#functie care primeste metoda http head, daca nu primim nimic, inseamna ca totul este in regula.
def head():
    return '', 200

if __name__ == '__main__':
    app.run(debug=True, port = 5555)
