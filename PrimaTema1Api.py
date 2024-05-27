#setam mai intai latitudinea longitudinea
#dupa setam ce vrem sa ne afiseze
#api pentru numarul de locuitori este apelat de api de detectie a orasului
#in functie de lat si long
#11.03.2024 - prima modificare
#Isachi Mihai

import tkinter as tk
from tkinter import *
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

# Initializare fereastra
root = tk.Tk()
root.title('Valori meteorologice Iasi')
root.geometry('450x200')

# Etichetă pentru Latitudine
latitudine_label = tk.Label(root, text='Latitudine:')
latitudine_label.grid(row=0, column=0)

# Input pentru Latitudine
latitudinea = tk.StringVar()
latitudine_entry = tk.Entry(root, textvariable=latitudinea)
latitudine_entry.grid(row=0, column=1)

# Etichetă pentru Longitudine
longitudine_label = tk.Label(root, text='Longitudine:')
longitudine_label.grid(row=1, column=0)

# Input pentru Longitudine
longitudinea = tk.StringVar()
longitudine_entry = tk.Entry(root, textvariable=longitudinea)
longitudine_entry.grid(row=1, column=1)

# Buton pentru a afișa datele meteo
submit_button = tk.Button(root, text='Submit', command=temperatura)
submit_button.grid(row=2, column=0, columnspan=2)

# Eticheta pentru afisarea orasului
label_text0 = tk.StringVar()
label_text0.set("Orasul:")
label0 = tk.Label(root, textvariable=label_text0)
label0.grid(row=0, column=2, columnspan=2)

# Eticheta pentru afisarea populatiei orasului
label_textpop = tk.StringVar()
label_textpop.set("Populatie:")
label_pop = tk.Label(root, textvariable=label_textpop)
label_pop.grid(row=1, column=2, columnspan=2)

# Etichetă pentru afișarea Temperaturii
label_text1 = tk.StringVar()
label_text1.set("Temperatura:")
label1 = tk.Label(root, textvariable=label_text1)
label1.grid(row=3, column=1, columnspan=2)

# Checkbutton pentru Temperatura
checktemp = tk.BooleanVar()
check1 = tk.Checkbutton(root, text = "Doresti temperatura?", variable = checktemp)
check1.grid(row = 3, column = 0)

# Etichetă pentru afișarea Umidității
label_text2 = tk.StringVar()
label_text2.set("Umiditate:")
label2 = tk.Label(root, textvariable=label_text2)
label2.grid(row=4, column=1, columnspan=2)

# Checkbutton pentru Umiditate
checkhum = tk.BooleanVar()
check2 = tk.Checkbutton(root, text = "Doresti umiditatea?", variable = checkhum)
check2.grid(row = 4, column = 0)

# Etichetă pentru afișarea Temperaturii resimțite
label_text3 = tk.StringVar()
label_text3.set("Temperatura resimțită:")
label3 = tk.Label(root, textvariable=label_text3)
label3.grid(row=5, column=1, columnspan=2)

# Checkbutton pentru temperatura resimtita
checktempresim = tk.BooleanVar()
check3 = tk.Checkbutton(root, text = "Doresti temperatura resimtita?", variable = checktempresim)
check3.grid(row = 5, column = 0)

# Rulare aplicație
root.mainloop()
