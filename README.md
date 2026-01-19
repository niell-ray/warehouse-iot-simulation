# warehouse-iot-simulation
ESP32-based IoT simulation for warehouse digital twin (Wokwi + MicroPython)


# Warehouse IoT Simulation (ESP32)

This repository contains the IoT simulation part of our B.Tech Major Project:
**Real-Time Warehouse Digital Twin Integrated with Blockchain Ledger**.

## Overview
The project simulates basic warehouse operations using an ESP32 controller in Wokwi.

Features implemented:
- Ultrasonic sensor for shelf occupancy detection
- Button-based scan simulation (mock RFID)
- I2C LCD display for real-time system messages
- LED indicator for shelf status
- Buzzer alert on scan detection

## Tools Used
- ESP32 (MicroPython)
- Wokwi Simulator
- HC-SR04 Ultrasonic Sensor
- I2C LCD (16x2)
- Push Button
- Buzzer

## Current Functionality
- Displays EMPTY / OCCUPIED shelf status
- Turns LED ON/OFF based on shelf state
- Shows “SCAN DETECTED” message on LCD
- Buzzer alerts on scan

## Note
RFID is mocked using a push button for simulation purposes.
Actual RFID testing is done on physical hardware.

## Author
Navoneel Ray

## Screenshots

### Wokwi Circuit Diagram
<img width="751" height="532" alt="Screenshot 2026-01-19 at 11 07 14 PM" src="https://github.com/user-attachments/assets/2dad4ec6-7da0-4507-9d53-c42e2618dab8" />


### Shelf Empty State
<img width="764" height="486" alt="Screenshot 2026-01-19 at 11 05 40 PM" src="https://github.com/user-attachments/assets/3961625d-a889-411c-b001-d8c283b7f779" />


### Shelf Occupied State
<img width="732" height="434" alt="Screenshot 2026-01-19 at 11 05 52 PM" src="https://github.com/user-attachments/assets/00d91006-8a5d-4b08-8322-422a10378c10" />


### Scan Detected
<img width="758" height="436" alt="Screenshot 2026-01-19 at 11 11 03 PM" src="https://github.com/user-attachments/assets/aede3e58-26c9-4cc9-bc61-f9f67670b060" />


