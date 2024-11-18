# IoT Temperature & Humidity Sensor with Web Server (Raspberry Pi Pico W)

This project is an implementation of an IoT temperature and humidity sensor using a **DHT22 sensor** connected to a **Raspberry Pi Pico W (2022)**. The device reads temperature and humidity data and hosts a simple web server to serve the data as JSON over a Wi-Fi network.

## Table of Contents

- [Project Overview](#project-overview)
- [Hardware Requirements](#hardware-requirements)
- [Software Requirements](#software-requirements)
- [Code Explanation](#code-explanation)
  - [1. Wi-Fi Connection](#1-wi-fi-connection)
  - [2. DHT22 Sensor Initialization](#2-dht22-sensor-initialization)
  - [3. HTTP Server Setup](#3-http-server-setup)
  - [4. Data Response Format](#4-data-response-format)
- [How to Use](#how-to-use)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Project Overview

This project enables a **Raspberry Pi Pico W (2022)** to connect to a Wi-Fi network, read temperature and humidity data from a **DHT22 sensor**, and serve this data through a simple HTTP web server. The sensor data is provided in JSON format, which can be accessed via any web browser or API client.

The main functionality is:
1. **Connect** to Wi-Fi.
2. **Read** temperature and humidity data from the DHT22 sensor.
3. **Serve** this data over an HTTP server.

## Hardware Requirements

- **Microcontroller**: Raspberry Pi Pico W (2022)
- **DHT22 Sensor**: For temperature and humidity measurements
- **Breadboard and Jumper Wires**: For wiring the sensor
- **LED (Optional)**: For visual feedback when the device is connected to Wi-Fi

## Software Requirements

- **MicroPython**: A Python implementation for microcontrollers. You can download it from [here](https://micropython.org/download/rp2-pico-w/).
- **Thonny IDE** (or any other suitable MicroPython IDE): For uploading and running the script.

## Code Explanation

### 1. Wi-Fi Connection

The Raspberry Pi Pico W connects to a Wi
