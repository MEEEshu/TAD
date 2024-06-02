import os
import datetime
import csv
import sys
import pandas as pd
import matplotlib.pyplot as plt
import serial
import time
import math


PPM = 0

# Valorile pentru variabilele din formulă
k = -0.464000  # Exemplu de valoare pentru k
RL = 4700.000  # Exemplu de valoare pentru RL
Ro = 100.000  # Exemplu de valoare pentru Ro
Va = 4096.000  # Exemplu de valoare pentru Va
#Vm = 2.5  # Exemplu de valoare pentru Vm
m = 0.433000  # Exemplu de valoare pentru m



#os.remove("date_meteo.csv")
#os.remove("date_meteo_temporare.csv")

with open("date_meteo.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Data","Temperatura","Umiditate","ValoareSenzorMq135","CalitateAer","IndiceConfort"])

with open("date_meteo_temporare.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Data","Temperatura","Umiditate","ValoareSenzorMq135","CalitateAer","IndiceConfort"])

def save_to_csv_temporary(data):
    with open('date_meteo_temporare.csv', mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        writer.writerow(data)


def save_to_csv(data):
    with open('date_meteo.csv', mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        writer.writerow(data)


try:
    while True:
        with serial.Serial('COM7', 9600) as ser:
            line = ser.readline().decode('latin1').strip()
            data = line.split(',')
            Vm = int(data[2])
            Rs = (4095 / int(data[2]) - 1)*RL
            R0 = Rs / 0.32
            PPM = (10 ** (1 / k * (math.log10(RL / R0 * ((Va / Vm) - 1)) - m))) * 1000000
            if len(data) == 5:
                date_meteo = {
                    'Data': time.strftime("%Y-%m-%d %H:%M:%S"),
                    'Temperatura': float(data[0]),
                    'Umiditate': float(data[1]),
                    'PPM': PPM,
                    'CalitateAer': data[4],
                    'IndiceConfort' : data[3]
                }
                save_to_csv(date_meteo)
                save_to_csv_temporary(date_meteo)
                print(10 ** (1 / k * (math.log10(RL / Ro * ((Va / int(data[2]) ) - 1)) - m))*1000000)
                
except KeyboardInterrupt:
    print("Oprirea memorarii")
