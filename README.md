# MC6205-graphical-display
graphical display on old neon plasma screen. 

![alt text](https://github.com/lambdaBoost/MC6205-graphical-display/blob/main/docs/vehicle_loss_tracker.jpg "Live update on Russian vehicle losses - but could be used for pretty much anything else")
*I'm showing this because it's funny - tracking wrecked Soviet era vehicles on a Soviet era device. Also, note the dead display line on the 'abandoned' section. We'll fix that later.*

This is a two part project using the Soviet Ukrainian MC6205 plasma display.
Part 1 uses the unaltered device with an ESP32 in order to display text info from any suitable webpage or API.
Part 2 will convert the device into a full graphical display (ie not just text).

## MC6205 Intro
The device itself is a monochrome neon plasma display, produced throughout the 1980s and early 1990s in Soviet Ukraine. It is capable of displaying text on a 100x100px screen. This is achieved by supplying appropriate serial inputs to the 64 pin connector on the base of the display.
Included in the package is an EEPROM which converts the serial inputs into text characters. This unfortunately mean the MC6205 is only capable of displaying text, but part 2 will see me re-wiring and adding a custom PCB to allow for full graphical display.

## Vehicle Loss Tracker
To demo part 1, I'm using the device to provide live updates on Russian vehicle losses. Data is from the excellent [Oryx loss tracker](https://www.oryxspioenkop.com/2022/02/attack-on-europe-documenting-equipment.html)

Fortunately someone else did the hard work and wrote an arduino library [arduino library](https://github.com/holzachr/MS6205-arduino-library) to display text to the display, so all I needed to do was hook it up to the ESP32 (following the instructions from the linked repo).

Data is provided by a custom API which runs on a seperate machine. In my case, the API runs from a raspberry pi and is queried by the ESP32. This avoided having to attempt to parse the webpage in Arduino...which would be a nightmare. The code for part 2 will be in Micropython which I find much easier to work with.

For now, the setup is wired up via a breadboard. When part 2 is complete it will be entirely contained in the original enclosure.

## Prerequisites
To build the vehicle tracker display in the exact format shown here you will need:

* MC6205 display. Available on ebay...but they are gradually getting more and more expensive!
* Raspberry pi with docker installed
* SN74HC595 shift register
* ESP32 WROOM development board
* A lot of hookup wire
* [MS6205-arduino-library](https://github.com/holzachr/MS6205-arduino-library) installed in your Arduino libraries folder
* 12v power supply (mine is 1A)

## Instructions
To build the vehicle loss tracker do the following:

* Hook up the MC6205 to the ESP32 and 12v power supply as detailed in [holzachr's repo](https://github.com/holzachr/MS6205-arduino-library)
* clone this repo to the raspberry pi
* on the pi, cd into the web-scraper directory
* run the following: `docker build -t vehicle_losses_scraper .`
* then run the docker container with: `docker run -d --name vehicle_loss_scraper -p 8080:8080 --restart always vehicle_loss_scraper`
* the API should now be active - note the pi's IP address (ifconfig)
* open the file at /mc6205/vehicle_loss_tracker.ino
* edit the first 3 lines (after the library imports) to include the correct IP address for the pi, your wifi network SSID and your wifi password (this is a lazy way of getting credentials - I'll add a proper wifi manager later).
* upload the edited .ino file to the esp32
* Enjoy!

