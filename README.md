# Arduino LCD Message Display with Python

This Python script allows you to send messages from your computer to an Arduino board, which can then be displayed on an LCD screen. The script utilizes the `pyFirmata` library to communicate with the Arduino via serial.

## Features

- **Send messages to Arduino**: Easily send any string to your Arduino board to be displayed on an attached LCD screen.
- **Simple and efficient**: Uses Python's `pyFirmata` library for serial communication.
- **Customizable**: Adjust the port and message as needed for different setups and applications.

## Requirements

- Python 3.x
- Arduino board (e.g., Arduino Uno)
- LCD screen connected to the Arduino
- [pyFirmata](https://pypi.org/project/pyFirmata/) library

## Installation

1. **Install Python**: Make sure you have Python 3.x installed on your system.

2. **Install the `pyFirmata` library**:

    ```bash
    pip install pyfirmata
    ```

3. **Upload StandardFirmata to the Arduino**:

    - Download and install the [Arduino IDE](https://www.arduino.cc/en/software) if you haven't already.
    - Connect your Arduino board to your computer via USB.
    - Open the Arduino IDE and go to **File > Examples > Firmata > StandardFirmata**.
    - Select the appropriate port for your Arduino under **Tools > Port**.
    - Choose your Arduino board model under **Tools > Board**.
    - Click the **Upload** button (right arrow icon) to upload the StandardFirmata code to your Arduino.

4. **Connect your Arduino**: Note the port that your Arduino is connected to (e.g., `COM3` on Windows or `/dev/ttyUSB0` on Linux).

## Usage

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Rcode879/arduino-lcd-display.git
    cd arduino-lcd-display
    ```

2. **Run the script**:

    Open a terminal or command prompt, navigate to the directory, and run:

    ```bash
    python lcd.py
    ```

3. **Modify the script as needed**:

    - **Change the port**: Adjust the `COM3` value to match the port your Arduino is connected to.
    - **Update the message**: Modify the `display_message("Hello, Arduino!")` line to send a different message to the LCD.

## How It Works

1. **Initialize Connection**: The script connects to the Arduino board using the `pyFirmata` library, specifying the port (e.g., `COM3`).
2. **Send a Message**: The `display_message` function sends a string to the Arduino to be displayed on the LCD screen using the `STRING_DATA` sysex message.
3. **Keep the Script Running**: A `while True` loop keeps the script active, maintaining the connection with the Arduino.

## Example

To display "Hello, Arduino!" on the LCD screen, the script uses:

```python
display_message("Hello, Arduino!")
