import network
import socket
import time
import uasyncio as asyncio  # Asynchroniczne zadania
from ulora import LoRa, ModemConfig, SPIConfig
import re

sensor_data = {"temperature": 0, "humidity": 0}

# Lora Parameters
SX1278_RST = 4
CONFIG_SPIBUS = SPIConfig.rp2_0
SX1278_CS = 1
SX1278_INT = 5
SX1278_FREQ = 433
SX1278_POW = 15
CLIENT_ADDRESS = 1
SERVER_ADDRESS = 2
# initialise radio
lora = LoRa(CONFIG_SPIBUS, SX1278_INT, SERVER_ADDRESS, SX1278_CS, reset_pin=SX1278_RST, freq=SX1278_FREQ, tx_power=SX1278_POW, acks=True)

# Funkcja do połączenia z WiFi
def connect_wifi():
    ssid = ""
    password = ""
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
    while not wlan.isconnected():
        time.sleep(1)
    
    print("Connected to WiFi", wlan.ifconfig())
    return wlan.ifconfig()[0]

# Callback do odbierania wiadomości LoRa
def on_recv(payload):
    global sensor_data
    try:
        data = payload.message  # Oczekuje formatu: "Temperature: 25.5C, Humidity: 60.3%"
        
        # Wyrażenia regularne do wyodrębnienia liczby przed 'C' i '%'
        temp_match = re.search(r"(-?\d+(\.\d+)?)C", data)  # Szukaj temperatury z końcówką 'C'
        humidity_match = re.search(r"(\d+(\.\d+)?)%", data)  # Szukaj wilgotności z końcówką '%'

        # Wyciąganie wartości, jeśli znaleziono
        if temp_match:
            temperature = float(temp_match.group(1))
        else:
            temperature = 0

        if humidity_match:
            humidity = float(humidity_match.group(1))
        else:
            humidity = 0
        
        sensor_data = {"temperature": temperature, "humidity": humidity}
        print("Odebrane dane:", sensor_data)
    except OSError as e:
        sensor_data = {"temperature": 0, "humidity": 0}

# Asynchroniczna funkcja serwująca stronę HTML i dane
async def serve():
    ip = connect_wifi()
    addr = socket.getaddrinfo(ip, 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    print("Serwer nasluchuje na", addr)
    
    while True:
        cl, addr = s.accept()
        print('Polaczenie od klienta', addr)
        request = cl.recv(1024).decode()
        
        if "/sensor-data" in request:
            data = sensor_data
            print(sensor_data)
            response = f"""HTTP/1.1 200 OK
Content-Type: application/json

{{"temperature": {data["temperature"]}, "humidity": {data["humidity"]}}}
"""
        else:
            with open("index.html", "r") as f:
                html = f.read()
                response = f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n{html}"
        
        cl.send(response.encode())
        cl.close()
        await asyncio.sleep(0)  # Dodajemy pauzę, aby inne zadania mogły być obsługiwane

# Asynchroniczna funkcja do odbierania danych LoRa
async def lora_listen():
    lora.set_mode_rx()  # Ustawiamy tryb odbioru
    lora.on_recv = on_recv  # type: ignore # Ustawienie callbacka
    while True:
        await asyncio.sleep(1)  # Co sekundę sprawdzamy stan LoRa

# Funkcja główna
async def main():
    # Uruchomienie serwera i nasłuchiwanie LoRa równocześnie
    await asyncio.gather(
        serve(),
        lora_listen()
    ) # type: ignore

# Uruchomienie programu
try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Program zatrzymany")



