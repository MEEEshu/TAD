from flask import Flask, jsonify, request, send_from_directory
import sqlite3
import requests

#api pentru umiditate, temperatura, si temperatura resimtita
api_key = '5d3293c93dbdd7f72c412b81cc5a5259'
#api pentru determinarea locatiei
api_key_oras = '41ed48c0-9c02-4d7a-8e77-1cbfcfff1713'
#api pt populatie, este apelata cu cheia de mai sus 
api_key_populatie = 'A5oYGIf8UgK9vC0ZL0e12g==jZ8fdWw8jy7Guyrd'

def temperatura():
    try:
        #date latitudine
        dateLatitudine = latitudinea.get()
        #date longitudine
        dateLongitudine = longitudinea.get()
        #apelam api pentru temperaturi si umiditate
        api_call = f'https://api.openweathermap.org/data/3.0/onecall/timemachine?lat={dateLatitudine}&lon={dateLongitudine}&dt=1643803200&appid={api_key}'
        #apelam api pentru detectarea orasului
        api_call_oras = f'http://api.airvisual.com/v2/nearest_city?lat={dateLatitudine}&lon={dateLongitudine}&key=41ed48c0-9c02-4d7a-8e77-1cbfcfff1713'
        #primim request cu date meteorologice
        weather_data = requests.get(api_call).json()#['data']
        #primim request cu date legate de oras
        oras_data = requests.get(api_call_oras).json()['data']['city']
        #afisam orasul
        label_text0.set(oras_data)
        #apelam api pentru a determina populatia
        api_url = f'https://api.api-ninjas.com/v1/city?name={oras_data}&X-Api-Key={api_key_populatie}'
        #dam request la date pentru populatie
        populatie = requests.get(api_url).json()
        #afisam datele pt populatie apelate de la api api_call_oras
        prem = populatie[0]['population']
        label_textpop.set(prem)
        #conditiile pentru checkboxes - temperatura
        if checktemp.get():
            temp = int(weather_data['data'][0]['temp']) - 273
            label_text1.set("Temperatura: " + str(temp) + "°C")
        else:
            label_text1.set(" ")
        #conditiile pentru checkboxes - umiditate
        if checkhum.get():
            humidity = str(weather_data['data'][0]['humidity']) + "%"
            label_text2.set("Umiditate: " + humidity)
        else:
            label_text2.set(" ")
        #conditiile pentru checkboxes - temperatura resimtita
        if checktempresim.get():
            feels_like = int(weather_data['data'][0]['feels_like']) - 273
            label_text3.set("Temperatura resimțită: " + str(feels_like) + "°C")
        else:
            label_text3.set(" ")
    #lansam o exceptie in caz de try va esua
    except KeyError:
        message = 'A apărut o problemă, rezolva'

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


# Restul codului dvs. rămâne neschimbat...

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
