# LoRa-sx1278-and-Raspberry-Pi-Pico

Building an IoT system using LoRA-02 sx1278 and RPi Pico modules
What you need:
- Raspberry Pi Pico W - the main station (server) and host of the HTTP site,
- Raspberry Pi Pico - client receiving temperature and humidity information, 
- DHT11 - temperature and humidity sensor,
- 2x LoRa-02 sx1278 433MHz - radio module used for communication between the client and the server

LoRa (Long Range) is a radio technology that is widely used in IoT (Internet of Things) systems due to its ability to transmit data over long distances with low power consumption. In the exercise, LoRa plays a key role in wireless communication between the client and the server. The client reads data from a temperature and humidity sensor and then transmits it to the server using the LoRa SX1278 module. The server receives this data and makes it available in the form of a web page accessible via Wi-Fi. 
Lora is part of the LPWAN (Low Power Wide Area Network) category operating 
in the unlicensed radio band. It is characterized by low power consumption and long range - up to several kilometers. The data transmission speed for LoRa ranges from a few to several hundred kilobits per second, which is sufficient for transmitting simple information such as temperature or humidity readings in IoT systems.

<p align="center">
  <img src="https://github.com/user-attachments/assets/3405cf24-dfea-46d8-a754-6094823ddef1">
</p>
 
LoRa wyróżnia się przede wszystkim:
•	Długim zasięgiem transmisji, nawet do kilkunastu kilometrów, co sprawia, że jest idealna do zastosowań IoT, gdzie urządzenia mogą być rozmieszczone w znacznej odległości od siebie.
•	Niskim poborem mocy, co pozwala na długą żywotność urządzeń zasilanych bateryjnie, co jest istotne w systemach IoT, gdzie energooszczędność jest kluczowa.
•	Dobrą odpornością na zakłócenia, co zapewnia stabilną transmisję nawet w trudnych warunkach środowiskowych.
Dzięki niskim kosztom oraz możliwości długodystansowej transmisji, LoRa znajduje zastosowanie w aplikacjach, gdzie potrzeba przesyłać niewielkie ilości danych z urządzeń rozmieszczonych na dużych obszarach, jak na przykład w monitoringu środowiskowym, rolnictwie czy inteligentnym mieście.


Uruchom Visual Studio Code, a następnie otwórz folder - Opracowane ćwiczenia z elektroniki\Raspberry Pi Pico\Ćw.8 System IoT z LoRa sx1278 i Raspberry Pi Pico\Program Raspberry Pi Pico W - serwer
Otwórz plik main.py oraz ulora.py aby skonfigurować mape połączeń LoRa sx1278 z Raspberry Pi Pico W. W pliku main.py w sekcji „# Lora Parameters” ustaw pin RST (reset), pin CS (chip select - NSS), INT (interrupt np. DIO0), ustaw odpowiednią częstotliwość oraz odpowiednią konfigurację klasy SPIConfig – aby skonfigurować interfejs SPI wejdź w bibliotekę „ulora.py”, a następnie znajdź klasę „class SPIConfig()”. Skonfiguruj piny w krotce według opisu tj. channel, sck, mosi, miso. Ostatnim krokiem przed uruchomieniem programu jest uzupełnienie SSID oraz PASSWORD w funkcji do połączenia z WiFi. Przy ustalaniu pinów przy interfejsie SPI należy korzystać z pinout Raspberry Pi Pico aby wykorzystać odpowiednie piny (np. SPI0 sck należy połączyć z sck LoRa, pin NSS tutaj to pin CS)!
 
Wgraj program klikając prawym przyciskiem myszy na plik main.py, a następnie wybierz opcję „Upload project to Pico”.
 
Aby uruchamiać kolejne zmiany w kodzie używaj szybkiego paska dostępu i pozycji „Run”.
Po uruchomieniu programu odczytaj z pozycji terminalu IP, na którym została utworzona strona HTTP.
 
Otwórz przeglądarkę i wpisz IP utworzonej strony HTTP na serwerze RPi Pico W – 192.168.1.35. Powinna ukazać się strona z 2 wskaźnikami jak poniżej:
 
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
