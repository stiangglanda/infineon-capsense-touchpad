# Infineon PSoC External Touchpad

This project turns an Infineon evaluation board (acquired at Embedded World 2026) into a functional external PC touchpad. 

It reads finger coordinates using the onboard CAPSENSE™ technology, transmits that data over a serial connection (UART), and uses a host-side Python script to capture the data and move the desktop mouse cursor accordingly.

## How It Works
1. **Firmware (C):** The PSoC microcontroller continuously scans the touchpad widget. When a touch is detected, it calculates the X and Y coordinates and prints them over the KitProg3 UART bridge (e.g., `T:120,45`). When the finger is lifted, it sends a release signal (`R`).
2. **Host Script (Python):** The `CaptureSerial.py` script listens to the corresponding serial port (`/dev/ttyACM0`). It parses the coordinate strings, calculates the relative delta between reads, and uses `pyautogui` to seamlessly move the system mouse.

## Requirements

### Hardware
- Infineon PSoC Evaluation Board with CAPSENSE™ touchpad (e.g., PSoC™ 4100T Plus Prototyping Kit).
- USB-C cable.

### Software
- **ModusToolbox™:** Required to compile and flash the firmware to the microcontroller.
- **Python 3:** To run the host script.
- **Linux with X11:** The host machine must be running an X11 display server. 

## Setup & Usage

### 1. Flash the Hardware
1. Import the firmware project into **ModusToolbox**.
2. Connect your Infineon board to your PC.
3. Build the project and click **Program** to flash the firmware onto the chip. 

### 2. Run the Python Script
Open a terminal and install the required Python libraries and run the script
```bash
pip install pyserial pyautogui
python scripts/CaptureSerial.py
```