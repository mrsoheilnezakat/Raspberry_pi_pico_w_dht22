# Temperature and Humidity Measurement with DHT22 and Raspberry Pi Pico W

## Introduction
This project involves measuring temperature and humidity using a DHT22 sensor connected to a Raspberry Pi Pico W. The data pin of the DHT22 is connected to GPIO22 on the Pico W.

### Components Needed
1. Raspberry Pi Pico W
2. DHT22 Sensor
4. Jumper Wires

### Connect the DHT22 sensor to the Raspberry Pi Pico W as follows:

1. VCC (DHT22) → 3.3V (Pico W)
2. Data (DHT22) → GPIO22 (Pico W)
3. GND (DHT22) → GND (Pico W)
**optional** Add a 10 kΩ pull-up resistor between the Data line and VCC.

### Code:

Use the following MicroPython code to read data from the DHT22 sensor: [python script](https://github.com/mrsoheilnezakat/Raspberry_pi_pico_w_dht22/blob/main_branch/main.py)
 
## Steps to Follow

### Set Up the Hardware:

Connect the DHT22 sensor to the Pico W according to the wiring diagram.

[actual setup](https://github.com/mrsoheilnezakat/Raspberry_pi_pico_w_dht22/blob/main_branch/image/actual%20setup.jpeg)

[diagram](https://github.com/mrsoheilnezakat/Raspberry_pi_pico_w_dht22/blob/main_branch/image/diagram.png)

### Install MicroPython on Pico W and setup script:

1. Flash pico-w by holding the button on pico and connect it to RPi or workstation running thonny. A storage device should be available on your devic.
2. Copy the downloaded micropython into storage and the device automatically get restarted. (always download from raspberry pi "latest and specifically for your microcontroller")
3. Select the device in thonny.
4. Configure interpreter from run menu, and select micropython.
5. Install dht library from manage packages in tools menu.
6. Save the script on the pico-w as main.py (in order to run on pico startup)

