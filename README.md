ROMANIAN:
Pas 1: Pornim ServerDate.py
Pas 2: Pornim SalvareDate.py
Pas 3: Pornim GUI_Date.py
Pas 4: Pornim GUI_Date_temporare.py

Pentru acest proiect se folosesc 2 placi ESP32-WROOM, un senzor DHT22 si un senzor MQ135. Rulam acelasi cod pe ambele placi ESP32, conectand la pinii aferenti codului.
Pentru pasul 3 si 4 putem sa le accesam pe ambele simultan, sau putem accesa fiecare separat in functie de ce valori dorim sa vedem pe grafice
GUI_Date este pentru datele prelevate de cand pornim pentru prima oara placile sa achizitioneze date (de prima oara de cand pornim SalvareDate.py)
GUI_Date_temporare este pentru datele prelevate de la ultima pornire a aplicatiei SalvareDate.py
interfata_client.html.txt este interfata pentru pagina web
Am introdus si un fisier de tip csv date_meteo_temporare.csv deoarece in SalvareDate.py, avem comanda os.remove("date_meteo_temporare.csv") care va sterge toate datele adunate pentru a avea parte de masuratoare doar de la ultima pornire a aplicatiei (sesiunea curenta)
Am introdus in cod COM5 si COM6, dar recomand sa se uite utilizatorul pe Device Manager pentru a identifica porturile aferente. 
Sper sa te bucuri de proiect. Vor mai urma :)

ENGLISH:
Step 1: Start ServerDate.py
Step 2: Start SalvareDate.py
Step 3: Start GUI_Date.py
Step 4: Start GUI_Date_temporare.py

For this project, 2 ESP32-WROOM boards, a DHT22 sensor, and an MQ135 sensor are used.We run the same code on both ESP32 boards, connecting to the corresponding pins as indicated in the code.
For steps 3 and 4, we can access both simultaneously, or we can access each one separately depending on which values we want to see on the graphs.
GUI_Date is for the data collected from the first time we start the boards to acquire data (from the first time we start SalvareDate.py).
GUI_Date_temporare is for the data collected since the last startup of the SalvareDate.py application.
interfata_client.html.txt is the interface for the web page.
I also introduced a csv file, date_meteo_temporare.csv, because in SalvareDate.py, we have the command os.remove("date_meteo_temporare.csv"), which will delete all the data gathered to have measurements only from the last startup of the application (current session).
I included COM5 and COM6 in the code, but I recommend the user to check the Device Manager to identify the corresponding ports.
I hope you enjoy the project. More to come :)

GERMAN: 
Schritt 1: Starten Sie ServerDate.py
Schritt 2: Starten Sie SalvareDate.py
Schritt 3: Starten Sie GUI_Date.py
Schritt 4: Starten Sie GUI_Date_temporare.py

Für dieses Projekt werden 2 ESP32-WROOM-Platinen, ein DHT22-Sensor und ein MQ135-Sensor verwendet.Wir führen denselben Code auf beiden ESP32-Boards aus und verbinden sie mit den entsprechenden Pins gemäß dem Code.
Für Schritt 3 und 4 können wir beide gleichzeitig zugreifen oder wir können jeden separat zugreifen, je nachdem, welche Werte wir auf den Grafiken sehen möchten.
GUI_Date ist für die Daten gedacht, die seit dem ersten Start der Platinen zur Datenerfassung (seit dem ersten Start von SalvareDate.py) gesammelt wurden.
GUI_Date_temporare ist für die Daten gedacht, die seit dem letzten Start der SalvareDate.py-Anwendung gesammelt wurden.
interfata_client.html.txt ist die Schnittstelle für die Webseite.
Ich habe auch eine CSV-Datei, date_meteo_temporare.csv, eingefügt, weil wir in SalvareDate.py den Befehl os.remove("date_meteo_temporare.csv") haben, der alle gesammelten Daten löschen wird, um nur Messungen seit dem letzten Start der Anwendung (aktuelle Sitzung) zu haben.
Ich habe COM5 und COM6 im Code eingefügt, aber ich empfehle dem Benutzer, den Geräte-Manager zu überprüfen, um die entsprechenden Anschlüsse zu identifizieren.
Ich hoffe, Ihnen gefällt das Projekt. Mehr wird folgen :)
