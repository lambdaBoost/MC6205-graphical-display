
#include <MS6205.h>
#include "RTClib.h"
#include "WiFi.h"
#include <HTTPClient.h>
#include <Arduino_JSON.h>


String URI = "http://192.168.1.217:8080/items/";
String results;

//lazy way to get wifi credentials in. 
const char* ssid = "";
const char* password =  "";

int const shiftRegisterLatchPin  = 15; // GPIO15 = Pin D8 on NodeMCU boards. Pin 12 on 74HC595.
int const shiftRegisterClockPin  = 14; // GPIO14 = Pin D5 on NodeMCU boards. Pin 11 on 74HC595.
int const shiftRegisterDataPin   = 13; // GPIO13 = Pin D7 on NodeMCU boards. Pin 14 on 74HC595.
int const displaySetPositionPin  = 12; // GPIO12 = Pin D6 on NodeMCU boards. Pin 16A on MS6205.
int const displaySetCharacterPin = 2;  // GPIO2  = Pin D4 on NodeMCU boards. Pin 16B on MS6205.
int const displayClearPin        = 5;  // GPIO5  = Pin D1 on NodeMCU boards. Pin 18A on MS6205.

MS6205 display(shiftRegisterLatchPin, shiftRegisterClockPin, shiftRegisterDataPin, displaySetPositionPin, displaySetCharacterPin, displayClearPin);
RTC_Millis rtc;



void setup() {

  Serial.begin(115200);
 
  WiFi.begin(ssid, password);
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("Connecting to WiFi..");
  }
 
  Serial.println("Connected to the WiFi network");


  
  rtc.begin(DateTime(F(__DATE__), F(__TIME__)));

  
}

void loop() {
  // get api data
  results = httpGETRequest(URI);
  Serial.println(results);


  int i1 = results.indexOf(',');
  int i2 = results.indexOf(',', i1+1);
  int i3 = results.indexOf(',', i2+1);
  int i4 = results.indexOf(',', i3+1);

  String total = results.substring(0, i1);
  String dest = results.substring(i1 + 1, i2);
  String dam = results.substring(i2 +1, i3);
  String ab = results.substring(i3 + 1, i4);
  String cap = results.substring(i4 + 1);

  total.replace("\"","");
  cap.replace("\"","");
  
  Serial.println(total);
  Serial.println(dest);
  Serial.println(dam);
  Serial.println(ab);
  Serial.println(cap);

  display.clear();

  display.setCursor(0,0);
  display.write("RUSSIAN VEHICLE");

  display.setCursor(5,1);
  display.write("LOSSES");

  display.setCursor(0,3);
  display.write("TOTAL " + total);

  display.setCursor(0,4);
  display.write("DESTROYED " + dest);

  display.setCursor(0,5);
  display.write("DAMAGED " + dam);

  display.setCursor(0,6);
  display.write("ABANDONED " + ab);

  display.setCursor(0,7);
  display.write("CAPTURED " + cap);


  display.setCursor(2, 9);
  display.write("slava ukraini");


  delay(40000);
  display.clear();

  for (int r=0; r<=9; r++){
    for(int c=0; c<=15;c++){
  
  int row = r;
  int column = c;

  display.writeBlock(c,r);
  delay(5);

  }
  }
 
  
  delay(5000);

  display.clear();
  DateTime tm = rtc.now();
  int hr = tm.hour();
  int mn = tm.minute();

  int T1 = (hr / 10) % 10;
  int T2 = hr % 10;
  int T3 = (mn / 10) % 10;
  int T4 = mn % 10;

  display.writeBigDigit(0,2,T1);
  display.writeBigDigit(4,2,T2);
  display.writeBigDigit(9,2,T3);
  display.writeBigDigit(13,2,T4);
  

  delay(30000);
}




String httpGETRequest(String serverName) {
  WiFiClient client;
  HTTPClient http;
    
  // Your Domain name with URL path or IP address with path
  http.begin(client, serverName);
  
  // Send HTTP POST request
  int httpResponseCode = http.GET();
  
  String payload = "{}"; 
  
  if (httpResponseCode>0) {
    Serial.print("HTTP Response code: ");
    Serial.println(httpResponseCode);
    payload = http.getString();
  }
  else {
    Serial.print("Error code: ");
    Serial.println(httpResponseCode);
  }
  // Free resources
  http.end();

  return payload;
}
