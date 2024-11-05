from time import sleep
from ulora import LoRa, SPIConfig
from machine import Pin
import dht

LED = Pin(19, Pin.OUT)
# DHT11 sensor
DHT11 = dht.DHT11(Pin(...))

# LoRa Parameters
SX1278_RST = ...
CONFIG_SPIBUS = SPIConfig.rp2_0
SX1278_CS = ...
SX1278_INT = ...
SX1278_FREQ = ...
SX1278_POW = 15
CLIENT_ADDRESS = 1
SERVER_ADDRESS = 2

# initialise radio
lora = LoRa(CONFIG_SPIBUS, SX1278_INT, CLIENT_ADDRESS, SX1278_CS, reset_pin=SX1278_RST, freq=SX1278_FREQ, tx_power=SX1278_POW, acks=True)

# loop and send data
while True:
    LED.on()
    try:
        DHT11.measure()
        temperature = DHT11.temperature()
        humidity = DHT11.humidity()
        LED.off()
        data = f"Temperature:{temperature}C, Humidity:{humidity}%"
        lora.send_to_wait(data, SERVER_ADDRESS)
        print(data)
    except OSError as e:
        print("Błąd odczytu z czujnika.")
    sleep(5)
