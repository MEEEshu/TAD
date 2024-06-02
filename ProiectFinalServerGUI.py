from flask import Flask, jsonify, request, send_from_directory
import sqlite3
import requests



# Inițializarea aplicației Flask
app = Flask(__name__)

# Endpoint pentru pagina principală a aplicației
@app.route('/')
def home():
    print('A fost accesată pagina lui Isachi Mihai /')
    return "<h3>Bine ai venit pe pagina mea!</h3> Sper să-ți placă. Wish you well </br>"

# Endpoint pentru pagina personalizată a utilizatorului
@app.route('/<username>')
def Username(username):
    print('primit:', username)
    return f"<h3>Bine ai venit pe pagina mea {username}!</h3> Sper să-ți placă. Wish you well </br>"


# Endpoint pentru a servi fișierul HTML pentru cele doua interfete
@app.route('/ProiectTAD')
def serve_ProiectTAD():
    return send_from_directory('.', 'interfataPROIECT.html')

# Endpoint pentru a servi fișierul HTML pentru interfața mașinilor
@app.route('/Masinute')
def serve_interface_masini():
    return send_from_directory('.', 'interfata_client.html')

# Endpoint pentru a servi fișierul HTML pentru interfața API-ului
@app.route('/API')
def serve_interface_api():
    return send_from_directory('.', 'interfata_clientv2.html')


# Endpoint pentru obținerea tuturor mașinilor din baza de date
@app.route('/api/cars', methods=['GET'])
def get_cars():
    conn = sqlite3.connect('cardata.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cars")
    cars = cursor.fetchall()
    conn.close()
    return jsonify(cars)

# Endpoint pentru obținerea unei mașini după ID din baza de date
@app.route('/api/cars/<int:car_id>', methods=['GET'])
def get_car(car_id):
    conn = sqlite3.connect('cardata.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cars WHERE id=?", (car_id,))
    car = cursor.fetchone()
    conn.close()
    if car is None:
        return jsonify({'error': 'Mașina nu a fost găsită'}), 404
    return jsonify(car)

# Endpoint pentru adăugarea unei noi mașini în baza de date
@app.route('/api/cars', methods=['POST'])
def add_car():
    data = request.json
    if 'brand' not in data or 'model' not in data or 'an' not in data:
        return jsonify({'error': 'Toate câmpurile (brand, model, an) sunt obligatorii'}), 400
    conn = sqlite3.connect('cardata.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO cars (brand, model, an) VALUES (?, ?, ?)", (data['brand'], data['model'], data['an']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Mașina a fost adăugată cu succes!'}), 201

# Endpoint pentru adăugarea unei mașini cu un anumit ID în baza de date
@app.route('/api/cars/<int:car_id>', methods=['POST'])
def add_car_with_id(car_id):
    data = request.json
    if 'brand' not in data or 'model' not in data or 'an' not in data:
        return jsonify({'error': 'Toate câmpurile (brand, model, an) sunt obligatorii'}), 400
    conn = sqlite3.connect('cardata.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO cars (id, brand, model, an) VALUES (?, ?, ?, ?)", (car_id, data['brand'], data['model'], data['an']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': f'Mașina cu ID-ul {car_id} a fost adăugată cu succes!'}), 201

# Endpoint pentru actualizarea parțială a unei mașini după ID în baza de date
@app.route('/api/cars/<int:car_id>', methods=['PATCH'])
def partial_update_car(car_id):
    data = request.json
    conn = sqlite3.connect('cardata.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE cars SET brand=?, model=?, an=? WHERE id=?", (data.get('brand'), data.get('model'), data.get('an'), car_id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Mașina a fost actualizată cu succes!'})

# Endpoint pentru actualizarea parțială a întregii colecții de mașini în baza de date
@app.route('/api/cars', methods=['PATCH'])
def partial_update_all_cars():
    data = request.json
    if not data:
        return jsonify({'error': 'Nu s-au furnizat date pentru actualizare'}), 400
    
    conn = sqlite3.connect('cardata.db')
    cursor = conn.cursor()

    for car_id, update_data in data.items():
        if 'brand' in update_data or 'model' in update_data or 'an' in update_data:
            cursor.execute("UPDATE cars SET brand=?, model=?, an=? WHERE id=?", (update_data.get('brand'), update_data.get('model'), update_data.get('an'), car_id))
    
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Actualizare parțială a mașinilor efectuată cu succes!'})

# Endpoint pentru actualizarea completă a unei mașini după ID în baza de date
@app.route('/api/cars/<int:car_id>', methods=['PUT'])
def update_car(car_id):
    data = request.json
    conn = sqlite3.connect('cardata.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE cars SET brand=?, model=?, an=? WHERE id=?", (data['brand'], data['model'], data['an'], car_id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Mașina a fost actualizată cu succes!'})

# Endpoint pentru actualizarea completă a întregii colecții de mașini în baza de date
@app.route('/api/cars', methods=['PUT'])
def update_all_cars():
    data = request.json
    if not data:
        return jsonify({'error': 'Nu s-au furnizat date pentru actualizare'}), 400
    
    conn = sqlite3.connect('cardata.db')
    cursor = conn.cursor()

    for car_id, update_data in data.items():
        cursor.execute("UPDATE cars SET brand=?, model=?, an=? WHERE id=?", (update_data['brand'], update_data['model'], update_data['an'], car_id))
    
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Actualizare completă a mașinilor efectuată cu succes!'})

# Endpoint pentru ștergerea unei mașini după ID din baza de date
@app.route('/api/cars/<int:car_id>', methods=['DELETE'])
def delete_car(car_id):
    conn = sqlite3.connect('cardata.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cars WHERE id=?", (car_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Mașina a fost ștearsă cu succes!'})

# Endpoint pentru ștergerea întregii colecții de mașini din baza de date
@app.route('/api/cars', methods=['DELETE'])
def delete_all_cars():
    confirmation = request.args.get('confirm')

    conn = sqlite3.connect('cardata.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cars")
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Toate mașinile au fost șterse cu succes!'})

# Endpoint pentru testarea metodei TRACE
@app.route('/api/cars', methods=['TRACE'])
def trace():
    return jsonify({'message': 'Acesta este un test de tip TRACE. cod : 200'}), 200

# Endpoint pentru testarea metodei HEAD
@app.route('/api/cars', methods=['HEAD'])
def head():
    return '', 200

# Rularea aplicației Flask
if __name__ == '__main__':
    app.run(debug=True, port=5555)
