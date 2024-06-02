#include <DHT.h>

#define DHTPIN 14     // Pinul la care este conectat senzorul DHT22
#define DHTTYPE DHT22 // Specificăm tipul de senzor DHT (DHT22 sau DHT11)
#define MQ135_PIN A0 // Pinul analogic la care este conectat senzorul MQ135



DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  Serial.println("Citire senzor DHT22:");
  dht.begin();
  Serial.println("Citire senzor MQ135:");
}

void loop() {
  delay(2000); // Pauză de 2 secunde între citiri
  //relatia liniara a concentratiei ppm de gaze = slope * (Rs/Ro + intercept)
  float slope = 0.65;
  float intercept = 10;
  float R0_gaz = 100;
  float temp_standard = 20;
  float umiditate_standard = 65;


  // Citim temperatura și umiditatea
  float temperatura = dht.readTemperature(); // Citire temperatura în grade Celsius
  float umiditate = dht.readHumidity();       // Citire umiditatea relativă în procente

  // Verificăm dacă citirea a fost cu succes
  if (isnan(temperatura) || isnan(umiditate)) {
    Serial.println("Eroare la citirea senzorului DHT22!");
    return;
  }
  float i = (temperatura * 1.8 + 32) - (0.55 - 0.0055 * umiditate) * ((temperatura * 1.8 + 32) - 58);
  
  
  //sub 65 este confort intre 65 si 80 alerta si dupa 80 este disconfort


  // Afișăm valorile citite pe ecranul serial
  //Serial.print("Temperatura: ");
  Serial.print(temperatura);
  //Serial.println(" °C");
  Serial.print(",");
  Serial.print(umiditate);
  //Serial.println(" %");

// Citim valoarea analogică de la senzorul MQ135
  int valoareSenzor = analogRead(MQ135_PIN);
  float Rs_ro = valoareSenzor / R0_gaz;
  float concentratieGaz =  slope * Rs_ro + intercept;
  //int valoareSenzor2 = valoareSenzor / 20;
  // Calculăm concentrația de gaz în aer
  // Aceasta este doar o estimare aproximativă și poate necesita calibrare pentru a fi precisă
  //float concentratieGaz = valoareSenzor / 4095.0 * 3.3; // Conversie la tensiune
  //int concentratieGaz2 = concentratieGaz; // Reglajul pentru MQ135

  float rezistentaSenzorinAer = 3.3 - concentratieGaz / concentratieGaz;
  float rezistenta0 = rezistentaSenzorinAer / 9.8;
  //float Rs = 4095.0 * 20000 / valoareSenzor - 20000;  //rs = 4095 * 20000 / valoaresenzor - 20000

  // Afișăm valoarea citită pe ecranul serial
  Serial.print(",");
  Serial.print(valoareSenzor);
  Serial.print(",");
  Serial.print(i);
  Serial.print(",");
    if (concentratieGaz < 16) {
    Serial.println("Calitate Foarte Buna a Aerului sub 200 ppm");
  } 
  else if (concentratieGaz >= 16 && concentratieGaz < 20) {
    Serial.println("Calitate Buna a Aerului 200-400 ppm");
  } 
  else if (concentratieGaz >= 18 && concentratieGaz < 22) {
    Serial.println("Calitate moderata a Aerului 400-600 ppm");
  } 
  else if (concentratieGaz >= 22 && concentratieGaz < 26) {
    Serial.println("Calitate slaba a Aerului 600-800 ppm");
  } 
  else {
    Serial.println("Calitate foarte slaba a Aerului peste 800 ppm");
  }
  
  Serial.print("\n");
  
  delay(1000); // Pauză de 1 secundă între citiri

}
