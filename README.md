#Temperature and Humidity Measurement with DHT22 and Raspberry Pi Pico W
Introduction
This project involves measuring temperature and humidity using a DHT22 sensor connected to a Raspberry Pi Pico W. The data pin of the DHT22 is connected to GPIO22 on the Pico W.

Components Needed
Raspberry Pi Pico W
DHT22 Sensor
Breadboard (optional)
Jumper Wires
10 kΩ Resistor (pull-up resistor)
Wiring Diagram
Connect the DHT22 sensor to the Raspberry Pi Pico W as follows:

VCC (DHT22) → 3.3V (Pico W)
Data (DHT22) → GPIO22 (Pico W)
GND (DHT22) → GND (Pico W)
Add a 10 kΩ pull-up resistor between the Data line and VCC.

Code
Use the following MicroPython code to read data from the DHT22 sensor:

 
Steps to Follow
Set Up the Hardware:

Connect the DHT22 sensor to the Pico W according to the wiring diagram.
Install MicroPython on Pico W:

If not already installed, flash MicroPython firmware onto your Pico W.
Set Up Thonny IDE:

Download and install Thonny from thonny.org.
In Thonny, select MicroPython (Raspberry Pi Pico) as the interpreter.
Upload the Code:

Copy the provided code into Thonny.
Save the script to the Pico W as main.py.
Run the Script:

Click the Run button in Thonny to execute the script.
Monitor the temperature and humidity readings in the console.
Notes
Pull-Up Resistor: Ensure the 10 kΩ resistor is connected between the Data pin and VCC for reliable communication.
Sensor Reading Interval: Do not read the sensor more frequently than once every 2 seconds to prevent inaccurate readings.
Module Availability: The dht module should be included in your MicroPython firmware. Update the firmware if necessary.
Conclusion
By following these steps, you can successfully measure temperature and humidity using a DHT22 sensor connected to a Raspberry Pi Pico W via GPIO22. This simple project serves as a foundation for more advanced applications like environmental monitoring or IoT systems.
