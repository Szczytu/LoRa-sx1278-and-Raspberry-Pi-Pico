# LoRa-RA-02-sx1278-and-Raspberry-Pi-Pico

Building an IoT system using LoRa Module RA-02 SX1278 433MHz and RPi Pico modules

The client reads data from a temperature and humidity sensor and then transmits it to the server using the LoRa SX1278 module. The server receives this data and makes it available on the website created in the network to which the RPi W server is connected.

## What you need:
- **Raspberry Pi Pico W** - the main station (server) and host of the HTTP site,
- **Raspberry Pi Pico** - client receiving temperature and humidity information, 
- **DHT11** - temperature and humidity sensor,
- **2x LoRa-RA-02-sx1278 433MHz** - radio module used for communication between the client and the server

## How connect LoRa RA-02 SX1278 and RPi Pico?

<p align="center">
  <img src="https://github.com/user-attachments/assets/e7ec46a0-bbd8-4a00-a313-e53e57d73912">
  <img src="https://github.com/user-attachments/assets/9b2f498a-31d6-4930-a711-afccefd52f10">
</p>

## What is LoRa?

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

Start **Visual Studio Code**, and then open the folder - **Raspberry Pi Pico W program - serwer**.

Open the main.py file and ulora.py file to configure the LoRa sx1278 connection map with Raspberry Pi Pico W. 

In the main.py file in the **“# Lora Parameters”** section, set the **RST** (reset) pin, **CS** (chip select - NSS) pin, **INT** (interrupt eg. DIO0), set the appropriate frequency and the appropriate configuration of the SPIConfig class - to configure the SPI interface. 

Enter the “ulora.py” library, then find the **“class SPIConfig()”** class. Configure the pins in the tuple according to the description, i.e. **channel, sck, mosi, miso**. 

The last step before running the program is to complete the SSID and PASSWORD in the function to connect to WiFi. 
> [!IMPORTANT]
> When setting up the pins at the SPI interface, use the Raspberry Pi Pico pinout to use the appropriate pins (e.g. SPI0 sck should be connected to LoRa's sck, the NSS pin here is the CS pin)!

<p align="center">
  <img src="https://github.com/user-attachments/assets/e9c4ae54-95f7-48a5-b9be-bb539ff9038a">
</p>

> [!IMPORTANT]
> To upload the program you need some IDE environment, e.g. Thonny or Virtual Studio Code (VSC need extension MiroPico)

Upload the program by right-clicking on the main.py file and then selecting "Upload project to Pico".

<p align="center">
  <img src="https://github.com/user-attachments/assets/ef8f6c6c-e129-4c8b-8d3d-7a5bd29c77a9">
</p>

To run next changes in the code, use the quick access bar and the "Run" item. After running the program, read from the terminal IP position on which the HTTP page was created.

<p align="center">
  <img src="https://github.com/user-attachments/assets/f3f22717-ffc4-4fd5-b47d-4a2c244760af">
</p>

Open a browser and type the IP of the created HTTP page on the RPi Pico W server - 192.168.1.35. A page with 2 indicators as below should appear:

 <p align="center">
  <img src="https://github.com/user-attachments/assets/6254e387-a1c7-4b79-93b0-894c396c6fd1">
</p>


The next step will be to start the client. **Do not** disconnect RPi Pico W from the server or close VSC.

Start another **Visual Studio Code window**, then open the folder - **Raspberry Pi Pico program - client**

Open the main.py file and ulora.py file to configure the LoRa sx1278 connection map with Raspberry Pi Pico. 

In the main.py file in the **“# Lora Parameters”** section, set the **RST** (reset) pin, **CS** (chip select - NSS) pin, **INT** (interrupt eg. DIO0), set the appropriate frequency and the appropriate configuration of the SPIConfig class - to configure the SPI interface. 

Enter the “ulora.py” library, then find the **“class SPIConfig()”** class. Configure the pins in the tuple according to the description, i.e. **channel, sck, mosi, miso**. 

The last step is to implement the temperature and humidity sensor.

 <p align="center">
  <img src="https://github.com/user-attachments/assets/bf424335-39e5-4c4b-818d-30b9e84ca8bd">
</p>

After connecting and configuring, connect the Raspberry Pi Pico - client to the COM port using USB. Remember to connect each device with a newly opened VSC so that the program distinguishes COM ports and does not deny access.

Steps to follow when something hangs or throws an error:

1. Close all windows from VSC
2. Disconnect all COM ports connected to RPi Pico (USB)
3. Start 1 VSC window, then open the folder with the files Ćw.8 IoT System with LoRa sx1278 and Raspberry Pi Pico W – server
4. Connect Raspberry Pi Pico W – server to the power supply via COM port (USB)
5. Start the main.py program on the server
6. Start 2 VSC window, then open the folder with the files Ćw.8 IoT System with LoRa sx1278 and Raspberry Pi Pico – client
7. Connect Raspberry Pi Pico – client to the power supply via COM port (USB)
8. Start the main.py program on the client

The appearance of the page when the client sends information to the server:

 <p align="center">
  <img src="https://github.com/user-attachments/assets/75ed2be2-8fac-42d3-b6e6-cb7cc21920a3">
</p>

Test the operation of the program and the page. Hold the temperature sensor in your fingers.

The project is an example of how to communicate LoRa modules.

Now all you need to do is add the appropriate modules to your own needs and have an overview, control your own IoT system

 <p align="center">
  <img src="https://github.com/user-attachments/assets/071798a4-f0ec-4138-b64a-b1110a566b1a">
</p>

