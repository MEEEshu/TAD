from datetime import datetime
from matplotlib import pyplot as plt
import pandas as pd
import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk

# Citirea datelor din fișierul CSV
data = pd.read_csv('date_meteo.csv')

# Datele din fișierul CSV
x = data['Data'].tolist()
y = data['Temperatura'].tolist()
z = data['Umiditate'].tolist()
w = data['ValoareSenzorMq135'].tolist()
a = data['CalitateAer'].tolist()
b = data['IndiceConfort'].tolist()

# Inițializare fereastră principală
root = tk.Tk()
root.title('MeteoHub')
root.geometry('700x400')
root.configure(bg='#f0f0f0')

# Setarea iconului ferestrei
root.iconbitmap("imagine.ico")

# Funcții pentru afișarea graficelor
def temperatura(): 
    plot1, ax1 = plt.subplots() 
    ax1.plot(x[start_index:end_index], y[start_index:end_index], linestyle='solid', color="green", label="Temperatura") 
    ax1.set_title("Temperatura medie") 
    ax1.set_xlabel("Perioada") 
    ax1.set_ylabel("Valori t°C") 
    ax1.set_ylim([0, 50]) 
    ax1.legend() 
    plt.tight_layout() 
    plt.show() 

def umiditate(): 
    plot2, ax2 = plt.subplots()   
    ax2.plot(x[start_index:end_index], z[start_index:end_index], linestyle='dotted', color="red", label='Umiditate') 
    ax2.set_title("Umiditate medie") 
    ax2.set_xlabel("Perioada") 
    ax2.set_ylabel("Valori umiditate %") 
    ax2.set_ylim([10, 70]) 
    ax2.legend() 
    plt.tight_layout() 
    plt.show()

def valoare_senzor(): 
    plot3, ax3 = plt.subplots()   
    ax3.plot(x[start_index:end_index], w[start_index:end_index], linestyle='solid', color="blue", label='Valoare Analogica') 
    ax3.set_title("Valoare Analogica medie") 
    ax3.set_xlabel("Perioada") 
    ax3.set_ylabel("PPM") 
    ax3.set_ylim([1, 20000]) 
    ax3.legend() 
    plt.tight_layout() 
    plt.show()

def indice_confort(): 
    plot4, ax4 = plt.subplots()   
    ax4.plot(x[start_index:end_index], b[start_index:end_index], linestyle='solid', color="purple", label='Indice Confort') 
    ax4.set_title("Indice Confort") 
    ax4.set_xlabel("Perioada") 
    ax4.set_ylabel("Valori Indice Confort") 
    ax4.set_ylim([0, 900]) 
    ax4.legend() 
    plt.tight_layout() 
    plt.show()

def submit():
    if checktemp.get():
        temp = data.iloc[end_index]['Temperatura']
        label_text1.set("Temperatura: " + str(temp) + "°C")
    else:
        label_text1.set("Bifează pentru temperatura")
    if checkhum.get():
        humidity = str(data.iloc[end_index]['Umiditate']) + "%"
        label_text2.set("Umiditate: " + humidity)
    else:
        label_text2.set("Bifează pentru umiditate")
    if checktempresim.get():
        feels_like = str(data.iloc[end_index]['CalitateAer'])
        label_text3.set("Calitate Aer: " + feels_like)
    else:
        label_text3.set("Bifează pentru calitatea aerului")
    if checkcomfort.get():
        comfort_index = data.iloc[end_index]['IndiceConfort']
        label_text4.set("Indice Confort: " + str(comfort_index))
    else:
        label_text4.set("Bifează pentru Indice Confort")

def update_start_date(val):
    global start_index
    start_index = int(float(val))
    start_date_label.config(text="Data Start: " + x[start_index])

def update_end_date(val):
    global end_index
    end_index = int(float(val))
    end_date_label.config(text="Data End: " + x[end_index])

# Variabile pentru intervalul de date
start_index = 0
end_index = int(float(len(x) - 1))

# Etichete și butoane
label_title = tk.Label(root, text="Monitorizare Date Meteorologice", font=("Helvetica", 16), bg='#f0f0f0')
label_title.grid(row=0, column=0, columnspan=4, pady=10)

label_text0 = tk.StringVar()
label_text0.set("Orașul: Iași")
label0 = tk.Label(root, textvariable=label_text0, font=("Helvetica", 12), bg='#f0f0f0')
label0.grid(row=1, column=0, columnspan=2)

label_textpop = tk.StringVar()
label_textpop.set("Student: Isachi Mihai")
label_pop = tk.Label(root, textvariable=label_textpop, font=("Helvetica", 12), bg='#f0f0f0')
label_pop.grid(row=1, column=2, columnspan=2)

submit_button = tk.Button(root, text='Afișează Temperatură', command=temperatura, bg='#4caf50', fg='white', font=("Helvetica", 10))
submit_button.grid(row=2, column=0, padx=10, pady=5)

submit_button1 = tk.Button(root, text='Afișează Umiditate', command=umiditate, bg='#f44336', fg='white', font=("Helvetica", 10))
submit_button1.grid(row=2, column=1, padx=10, pady=5)

submit_button2 = tk.Button(root, text='Afișează Concentratia Gazului', command=valoare_senzor, bg='#2196f3', fg='white', font=("Helvetica", 10))
submit_button2.grid(row=2, column=2, padx=10, pady=5)

submit_button3 = tk.Button(root, text='Afișează Indice Confort', command=indice_confort, bg='#9c27b0', fg='white', font=("Helvetica", 10))
submit_button3.grid(row=2, column=3, padx=10, pady=5)

submit_button4 = tk.Button(root, text='Afișează Date', command=submit, bg='#ff9800', fg='white', font=("Helvetica", 10))
submit_button4.grid(row=7, column=1, columnspan=2, pady=10)

label_text1 = tk.StringVar()
label_text1.set("Bifează pentru temperatura")
label1 = tk.Label(root, textvariable=label_text1, font=("Helvetica", 12), bg='#f0f0f0')
label1.grid(row=3, column=1, columnspan=2)

checktemp = tk.BooleanVar()
check1 = tk.Checkbutton(root, text="Dorești temperatura?", variable=checktemp, bg='#f0f0f0', font=("Helvetica", 10))
check1.grid(row=3, column=0, padx=10)

label_text2 = tk.StringVar()
label_text2.set("Bifează pentru umiditate")
label2 = tk.Label(root, textvariable=label_text2, font=("Helvetica", 12), bg='#f0f0f0')
label2.grid(row=4, column=1, columnspan=2)

checkhum = tk.BooleanVar()
check2 = tk.Checkbutton(root, text="Dorești umiditatea?", variable=checkhum, bg='#f0f0f0', font=("Helvetica", 10))
check2.grid(row=4, column=0, padx=10)

label_text3 = tk.StringVar()
label_text3.set("Bifează pentru calitatea aerului")
label3 = tk.Label(root, textvariable=label_text3, font=("Helvetica", 12), bg='#f0f0f0')
label3.grid(row=5, column=1, columnspan=2)

checktempresim = tk.BooleanVar()
check3 = tk.Checkbutton(root, text="Dorești calitatea aerului?", variable=checktempresim, bg='#f0f0f0', font=("Helvetica", 10))
check3.grid(row=5, column=0, padx=10)

label_text4 = tk.StringVar()
label_text4.set("Bifează pentru Indice Confort")
label4 = tk.Label(root, textvariable=label_text4, font=("Helvetica", 12), bg='#f0f0f0')
label4.grid(row=6, column=1, columnspan=2)

checkcomfort = tk.BooleanVar()
check4 = tk.Checkbutton(root, text="Dorești Indice Confort?", variable=checkcomfort, bg='#f0f0f0', font=("Helvetica", 10))
check4.grid(row=6, column=0, padx=10)

start_date_label = tk.Label(root, text="Data Start: " + x[start_index], font=("Helvetica", 10), bg='#f0f0f0')
start_date_label.grid(row=9, column=0, columnspan=2, padx=10, pady=5)

# Slider pentru selectarea datei de început
start_slider = ttk.Scale(root, from_=0, to=len(x) - 1, orient='horizontal', command=update_start_date)
start_slider.set(start_index)
start_slider.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

end_date_label = tk.Label(root, text="Data End: " + x[end_index], font=("Helvetica", 10), bg='#f0f0f0')
end_date_label.grid(row=9, column=2, columnspan=2, padx=10, pady=5)


# Slider pentru selectarea datei de sfârșit
end_slider = ttk.Scale(root, from_=0, to=len(x) - 1, orient='horizontal', command=update_end_date)
end_slider.set(end_index)
end_slider.grid(row=8, column=2, columnspan=2, padx=10, pady=10)

# Rulare aplicație
root.mainloop()


