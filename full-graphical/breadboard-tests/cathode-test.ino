
   
#include <Arduino.h>

// pin definitions
// should be H1-H7 in latin alphabet

#define X1 0
#define X2 4
#define X3 2
#define X4 21
#define X5 19
#define X6 5
#define X7 18

// cathode clock 1
#define CCLK 12
#define CCLK2 13

// anode shift register data in pins
#define AD1357 23
#define AD246 22

// both anode shift register clocks connected to one pin
#define ACLK2 27
#define ACLK1 26




void setCathode(int8_t cathode) {

  // begin clock pulse
  digitalWrite(CCLK,HIGH);
  // MSB X7,X6,X5,X4 LSB counts from 0 to 15
  digitalWrite(X4,cathode & 0x1);
  digitalWrite(X5,((cathode & 0x2)>>1));
  digitalWrite(X6,((cathode & 0x4)>>2));
  digitalWrite(X7,((cathode & 0x8)>>3));
  // MSB X3,X2,X1 LSB counts 0,1,2,3,4
  digitalWrite(X1,((cathode & 0x10)>>4));
  digitalWrite(X2,((cathode & 0x20)>>5));
  digitalWrite(X3,((cathode & 0x40)>>6));


  //signal ready to cathode input
      digitalWrite(CCLK2, HIGH);
      delayMicroseconds(2);
      digitalWrite(CCLK2,LOW);

  digitalWrite(CCLK,LOW);

  
}

void setup() {

  // Setting up serial
  Serial.begin(9600);
  Serial.println("MS6205 logic replacement board");


  // Setting up pins  
  pinMode(X1,OUTPUT);
  pinMode(X2,OUTPUT);
  pinMode(X3,OUTPUT);
  pinMode(X4,OUTPUT);
  pinMode(X5,OUTPUT);
  pinMode(X6,OUTPUT);
  pinMode(X7,OUTPUT);
  pinMode(CCLK,OUTPUT);
  pinMode(AD1357,OUTPUT);
  pinMode(AD246,OUTPUT);
  pinMode(ACLK2,OUTPUT);
  pinMode(ACLK1,OUTPUT);
  pinMode(CCLK2, OUTPUT);


  digitalWrite(ACLK1,LOW);
  digitalWrite(ACLK2,LOW);
  digitalWrite(CCLK,LOW);
  digitalWrite(CCLK2,LOW);


  //setup done
  Serial.println("Setup done");
  digitalWrite(LED_BUILTIN,LOW);
}



void loop() {
  for(uint8_t i=0;i<16;i++) {
    for(uint8_t j=0;j<5;j++) {

      //shift in zebra (10101...)

      for (int i=0;i<40;i++) {
      digitalWrite(ACLK1,LOW);

      digitalWrite(AD1357,HIGH);
      digitalWrite(ACLK1,HIGH);
      delayMicroseconds(2);
      digitalWrite(ACLK1,LOW);


      digitalWrite(AD246,HIGH);
      digitalWrite(ACLK2,HIGH);
      delayMicroseconds(2);
      digitalWrite(ACLK2,LOW);
      

      }



     
      setCathode((j<<4)|i);
      delayMicroseconds(200);

      Serial.println("CATHODE WROTE");



    }
  }
}
