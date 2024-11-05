# LoRa-RA-02-sx1278-and-Raspberry-Pi-Pico

Building an IoT system using LoRa Module RA-02 SX1278 433MHz and RPi Pico modules

What you need:
- Raspberry Pi Pico W - the main station (server) and host of the HTTP site,
- Raspberry Pi Pico - client receiving temperature and humidity information, 
- DHT11 - temperature and humidity sensor,
- 2x LoRa-RA-02-sx1278 433MHz - radio module used for communication between the client and the server

LoRa (Long Range) is a radio technology that is widely used in IoT (Internet of Things) systems due to its ability to transmit data over long distances with low power consumption. In the exercise, LoRa plays a key role in wireless communication between the client and the server. The client reads data from a temperature and humidity sensor and then transmits it to the server using the LoRa SX1278 module. The server receives this data and makes it available in the form of a web page accessible via Wi-Fi. 
Lora is part of the LPWAN (Low Power Wide Area Network) category operating in the unlicensed radio band. It is characterized by low power consumption and long range - up to several kilometers. The data transmission speed for LoRa ranges from a few to several hundred kilobits per second, which is sufficient for transmitting simple information such as temperature or humidity readings in IoT systems.

<p align="center">
  <img src="https://github.com/user-attachments/assets/3405cf24-dfea-46d8-a754-6094823ddef1">
</p>
 
LoRa is distinguished primarily by:
- Long transmission range, up to several kilometers, which makes it ideal for IoT applications where devices may be located at a considerable distance from each other.
- Low power consumption, allowing long life of battery-powered devices, which is important in IoT systems where energy efficiency is key.
- Good immunity to interference, which ensures stable transmission even in harsh environments.
Thanks to its low cost and long-distance transmission capability, LoRa is used in applications where small amounts of data need to be transmitted from devices distributed over large areas, such as in environmental monitoring, agriculture and smart city.

# How to start an IoT system

Start Visual Studio Code, and then open the folder - Raspberry Pi Pico W program - server Open the main.py file and ulora.py file to configure the LoRa sx1278 connection map with Raspberry Pi Pico W. In the main.py file in the “# Lora Parameters” section, set the RST (reset) pin, CS (chip select - NSS) pin, INT (interrupt eg. DIO0), set the appropriate frequency and the appropriate configuration of the SPIConfig class - to configure the SPI interface, enter the “ulora.py” library, then find the “class SPIConfig()” class. Configure the pins in the tuple according to the description, i.e. channel, sck, mosi, miso. The last step before running the program is to complete the SSID and PASSWORD in the function to connect to WiFi. When setting up the pins at the SPI interface, use the Raspberry Pi Pico pinout to use the appropriate pins (e.g. SPI0 sck should be connected to LoRa's sck, the NSS pin here is the CS pin)!

<p align="center">
  <img src="https://github.com/user-attachments/assets/e9c4ae54-95f7-48a5-b9be-bb539ff9038a">
</p>

 
Upload the program by right-clicking on the main.py file and then selecting "Upload project to Pico".

<p align="center">
  <img src="https://github.com/user-attachments/assets/cb3df6a1-f3b2-46d5-89bd-c181b2f0acb2">
</p>

To run next changes in the code, use the quick access bar and the "Run" item. After running the program, read from the terminal IP position on which the HTTP page was created.

<p align="center">
  <img src="https://github.com/user-attachments/assets/b7cb966c-f053-4566-a665-5ae8ed75f917">
</p>

Open a browser and type the IP of the created HTTP page on the RPi Pico W server - 192.168.1.35. A page with 2 indicators as below should appear:

 <p align="center">
  <img src="https://github.com/user-attachments/assets/6254e387-a1c7-4b79-93b0-894c396c6fd1">
</p>


Kolejnym krokiem będzie uruchomienie klienta. Nie rozłączaj RPi Pico W z serwerem ani nie zamykaj VSC. Uruchom kolejne okno Visual Studio Code, a następnie otwórz folder - Opracowane ćwiczenia z elektroniki\Raspberry Pi Pico\Ćw.8 System IoT z LoRa sx1278 i Raspberry Pi Pico\Program Raspberry Pi Pico - klient
Otwórz plik main.py oraz ulora.py aby skonfigurować mape połączeń LoRa sx1278 z Raspberry Pi Pico. W pliku main.py w sekcji „# Lora Parameters” ustaw pin RST (reset), pin CS (chip select - NSS), INT (interrupt np. DIO0), ustaw odpowiednią częstotliwość oraz odpowiednią konfigurację klasy SPIConfig – aby skonfigurować interfejs SPI wejdź w bibliotekę „ulora.py”, a następnie znajdź klasę „class SPIConfig()”. Skonfiguruj piny w krotce według opisu tj. channel, sck, mosi, miso. Ostatnim krokiem jest zaimplementowanie czujnika temperatury i wilgotności. 
 
Rys. 6.6 czujnik DHT11
W zależności jaki czujnik będzie dostępny oraz jakie ma wyprowadzenia podłącz go zgodnie z dokumentacją tj. zasilanie, masa oraz pin data. Na rys. 6.6 przedstawiono przykładowy czujnik DHT11 z jego wyprowadzeniami. W kodzie programu znajdź informację do którego pinu trzeba podłączyć pin DATA czujnika – oczywiście można to edytować.
Po podłączeniu oraz konfiguracji należy podłączyć Raspberry Pi Pico – klienta do portu COM przy użyciu usb. Należy pamiętać aby każde urządzenie podłączać z nowo otwartym VSC aby program rozróżniał porty COM i nie odmawiał dostępu.
Kroki postępowania gdy coś się zwiesi lub wyrzuci jakiś błąd:
1.	Zamknij wszystkie okna z VSC
2.	Odłącz wszystkie porty COM podłączone do RPi Pico (USB)
3.	Uruchom 1 okno VSC, a następnie otwórz folder z plikami Ćw.8 System IoT z LoRa sx1278 i Raspberry Pi Pico W – serwer
4.	Podłącz Raspberry Pi Pico W – serwer do zasilania poprzez port COM (USB)
5.	Uruchom program main.py na serwerze
6.	Uruchom 2 okno VSC, a następnie otwórz folder z plikami Ćw.8 System IoT z LoRa sx1278 i Raspberry Pi Pico – klient
7.	Podłącz Raspberry Pi Pico  – klient do zasilania poprzez port COM (USB)
8.	Uruchom program main.py na kliencie



Wygląd strony gdy klient wysyła informację do serwera:
 
Potestuj działanie programu oraz strony. Przytrzymaj w palcach czujnik temperatury – zaobserwuj działanie projektu. Spróbuj pozmieniać czasy opóźnień w programach. Edytuj stronę HTTP – plik index.html na serwerze według uznania. Zmień np. wykresy, wielkości czcionek ich kolory, spróbuj pododawać/edytować style css itd. Zmień częstotliwość LoRa – zaobserwuj zmiany w wysyłaniu i odbieraniu pakietów. Jeśli jest możliwość przetestuj zasięg działania systemu oraz zmienną SX1278_POW i jej wpływ na zasięg. Każdą zmianę w plikach np. konfigurowanie strony – plik index.html należy wysłać do pamięci pico „Upload project to Pico”.
 
Rys. 6.7 System IoT z wykorzystaniem modułów LoRA-02 sx1278 oraz RPi Pico
