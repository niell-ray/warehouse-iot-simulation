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
