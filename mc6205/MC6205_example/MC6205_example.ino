/* Example of using a NodeMCUv3 ES8266 with a 74HC595 shift register
 * to drive an Elektronika MS6205 multi-line character display.
 * 
 *  
 * Copyright 2018 Christian Holzapfel
 * 
 * Released under the MIT License.
 * 
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 * 
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
*/

#include <MS6205.h>
#include "RTClib.h"

int const shiftRegisterLatchPin  = 15; // GPIO15 = Pin D8 on NodeMCU boards. Pin 12 on 74HC595.
int const shiftRegisterClockPin  = 14; // GPIO14 = Pin D5 on NodeMCU boards. Pin 11 on 74HC595.
int const shiftRegisterDataPin   = 13; // GPIO13 = Pin D7 on NodeMCU boards. Pin 14 on 74HC595.
int const displaySetPositionPin  = 12; // GPIO12 = Pin D6 on NodeMCU boards. Pin 16A on MS6205.
int const displaySetCharacterPin = 2;  // GPIO2  = Pin D4 on NodeMCU boards. Pin 16B on MS6205.
int const displayClearPin        = 5;  // GPIO5  = Pin D1 on NodeMCU boards. Pin 18A on MS6205.

MS6205 display(shiftRegisterLatchPin, shiftRegisterClockPin, shiftRegisterDataPin, displaySetPositionPin, displaySetCharacterPin, displayClearPin);
RTC_Millis rtc;



void setup() {
  // put your setup code here, to run once:
  rtc.begin(DateTime(F(__DATE__), F(__TIME__)));
}

void loop() {
  // put your main code here, to run repeatedly:


  display.clear();

 
  for (int r=0; r<=9; r++){
  
  int row = r;
  int column = 2;
  display.setCursor(column, row);
  display.write("slava ukraini");

  }

  delay(5000);
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
  

  delay(5000);
}
