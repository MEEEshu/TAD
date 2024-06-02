from flask import Flask, jsonify, render_template
import serial
import csv
import schedule
import apscheduler
import math

PPM = 0

# Valorile pentru variabilele din formulă
k = -0.464000  # Exemplu de valoare pentru k
RL = 4700.000  # Exemplu de valoare pentru RL
Va = 4096.000  # Exemplu de valoare pentru Va
#Vm = 2.5  # Exemplu de valoare pentru Vm
m = 0.433000  # Exemplu de valoare pentru m

app = Flask(__name__)

# Funcție pentru citirea datelor de la portul serial și returnarea acestora sub formă de dictionar
def read_serial_data():
    # Configurați portul serial
    ser = serial.Serial('COM5', 9600)  # Schimbați 'COM5' cu portul serial corect și 9600 cu viteza corectă de transmisie
    
    # Așteptați ca portul serial să fie deschis
    if not ser.is_open:
        ser.open()
    line = ser.readline().decode('latin1').strip()
    data = line.split(',')
    Vm = int(data[2])
    Rs = (4095 / int(data[2]) - 1)*RL
    R0 = Rs / 0.32
    PPM = (10 ** (1 / k * (math.log10(RL / R0 * ((Va / Vm) - 1)) - m))) * 1000000
    if len(data) == 5:
        car_data = {
            'temperatura': float(data[0]),
            'umiditate': float(data[1]),
            'PPM': PPM,
            'calitate_aer': data[4],
            'indiceConfort' : data[3]
        }
        return car_data



# Endpoint pentru pagina principală
@app.route('/')
def home():
    return render_template('interfata_clientv2.html')

# Endpoint pentru obținerea datelor meteorologice
@app.route('/meteo/date', methods=['GET'])
def get_weather_data():
    car_data = read_serial_data()
    return jsonify(car_data)

# Endpoint pentru obținerea datelor meteorologice - temperatura
@app.route('/meteo/temperatura', methods=['GET'])
def get_temperature_data():
    car_data = read_serial_data()
    return jsonify({'temperatura': car_data['temperatura']})

# Endpoint pentru obținerea datelor meteorologice - umiditate
@app.route('/meteo/umiditate', methods=['GET'])
def get_humidity_data():
    car_data = read_serial_data()
    return jsonify({'umiditate': car_data['umiditate']})

# Endpoint pentru obținerea datelor meteorologice - calitate aer
@app.route('/meteo/calitateaer', methods=['GET'])
def get_air_quality_data():
    car_data = read_serial_data()
    return jsonify({'calitate_aer': car_data['calitate_aer']})

# Endpoint pentru obținerea datelor meteorologice - senzor
@app.route('/meteo/senzor', methods=['GET'])
def get_sensor_data():
    car_data = read_serial_data()
    return jsonify({'PPM': int (car_data['PPM'])})

# Endpoint pentru obținerea datelor meteorologice - senzor
@app.route('/meteo/indice', methods=['GET'])
def get_ITU():
    car_data = read_serial_data()
    return jsonify({'indiceConfort': car_data['indiceConfort']})

@app.route('/client')
def client_interface():
    return app.send_static_file('interfata_client.html')


if __name__ == '__main__':
    app.run(debug=True,host='192.168.1.146', port=5123)
