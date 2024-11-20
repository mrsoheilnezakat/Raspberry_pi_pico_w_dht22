import machine
import time
import network
import dht
import socket

# ssid and pass
name = "****"
password = "****"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
led=machine.Pin('LED',machine.Pin.OUT)
ap=wlan.scan()
for ap in ap:
    print(ap)
dht_pin = machine.Pin(22)

dht_sensor = dht.DHT22(dht_pin)


def connect():
    while not wlan.isconnected():
        print('try to connect... ')
        wlan.connect(name,password)
        time.sleep(20)
    
    if wlan.isconnected() == True:
        print('wifi is connected')
        print('Try to ping the device at', wlan.ifconfig())
        led.off()
        time.sleep(2.5)
        led.on()
        time.sleep(2.5)
        ip = wlan.ifconfig()[0]
        print(f'Connected on {ip}')
    return ip
def measure():
    dht_sensor.measure()
    temperature_celsius = str(dht_sensor.temperature())
    humidity_percent=str(dht_sensor.humidity())
    return temperature_celsius,humidity_percent


connect()
tem,hum=measure()
print(tem)
print(hum)

addr = socket.getaddrinfo('0.0.0.0',80)[0][-1]
s=socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1) #allow address reuse
s.bind(addr)
s.listen(1)
print('listening on:', addr)
try:
    while True:
        cl, addr=s.accept()
        print('client connected from:', addr)
        request = cl.recv(1024)
        temp,humi=measure()
        response = ("HTTP/1.1 200 ok\r\nContent-Type: application/json\r\n\r\n"
                    f'{{"temp": {temp}, "humi": {humi}}}'
                    )
        cl.send(response)
        time.sleep(1)
        cl.close()
except Exception as e:
    print("Error: ",e)
    s.close
    
