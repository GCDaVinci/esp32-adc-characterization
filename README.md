# ESP32 ADC Characterization

A simple method for characterizing the ESP32's 12-bit ADC performance by comparing measured voltage values with serial readings from the device. The code for this project consists of two parts. The first is the code on the esp32 that continously reads the ADC value, converts it to a voltage value based on a 3.3v reference voltage, and then prints it to the serial port. The second code is a Python script that runs on your computer and reads the serial output of the esp32 via usb.

## Overview

This project helps you evaluate the accuracy and linearity of your ESP32's ADC by:
- Reading voltage values from the ESP32 via serial communication
- Comparing them with manually measured reference voltages
- Calculating the difference/error between measured and serial values
- Exporting all data to CSV format for analysis

## Hardware Setup

<img width="640" height="400" alt="ESP32_ADC_Wiring_Diagram drawio" src="https://github.com/user-attachments/assets/52c246c4-a9b7-40e7-b379-f76c68a3eba6" />

### Connection Details

- **3.3V** → **Potentiometer VCC** (top terminal)
- **GND** → **Potentiometer GND** (bottom terminal)  
- **ADC Pin** → **Potentiometer Wiper** (middle terminal)

### Recommended ESP32 Pins

- **ADC1_CH0** (GPIO36) - Most stable ADC channel
- **ADC1_CH1** (GPIO37) - Alternative option
- **ADC1_CH2** (GPIO38) - Another alternative

### Parts List

- ESP32 development board
- 10kΩ potentiometer (linear taper recommended)
- Breadboard and jumper wires
- USB cable for programming and serial communication
- Multimeter

## Features

- **Real-time voltage comparison**: Continuously measure and compare voltages
- **Serial communication**: Reads data from ESP32 via COM port
- **CSV export**: Automatically saves all measurements with timestamps

## Requirements

### Software
- Python 3.7+
- pyserial library for serial communication

## Installation

1. **Clone or download this repository**
2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Operation

1. **Connect your ESP32** to your computer via USB
2. **Run the program**:
   ```bash
   python main.py
   ```
3. **Enter measured voltages**: Type the actual voltage you're measuring (e.g., 3.30, 12.5)
4. **Read serial data**: The program will automatically read from the ESP32
5. **Continue measuring**: Adjust the potentiometer to measure a different voltage and repeat
6. **Save and exit**: Type 'end' to save all data to CSV and exit

### Example Session

<img width="634" height="520" alt="image" src="https://github.com/user-attachments/assets/5e1a3b05-b3be-40ad-bb63-714da05c4db5" />

### Configuration

The default serial settings are:
- **Port**: COM3 (Windows) - modify in `src/utils.py` if needed
- **Baud rate**: 115200
- **Data bits**: 8
- **Parity**: None
- **Stop bits**: 1

## Output

### CSV File Format

<img width="418" height="650" alt="image" src="https://github.com/user-attachments/assets/5d37d060-f1a1-48b7-97cc-8781898ce92c" />

The program generates CSV files with the following columns:
- **Timestamp**: Time of measurement (HH:MM:SS)
- **Measured Voltage (V)**: Your reference voltage measurement
- **Serial Voltage (V)**: Voltage read from ESP32 via serial
- **Difference (V)**: Calculated difference (Serial - Measured)

With this data, you can easily create a scatter plot to assess the accuraty of your ESP32's ADC

<img width="1061" height="622" alt="image" src="https://github.com/user-attachments/assets/db154658-d5b5-428f-81c4-158ab30853c4" />

### File Naming

Files are automatically named with timestamps:
```
voltage_comparison_YYYYMMDD_HHMMSS.csv
```

Example: `voltage_comparison_20241201_143022.csv`

## Project Structure

```
ESP32_ADC_Characterization/
├── main.py              # Main program entry point
├── requirements.txt     # Python dependencies
├── README.md           # This documentation
└── src/                # Source code directory
    ├── __init__.py     # Package initialization
    └── utils.py        # Utility functions (serial communication, CSV export)
```

## Troubleshooting

### Serial Port Issues
- **Port not found**: Check device manager for correct COM port
- **Permission denied**: Close other programs using the serial port
- **Connection failed**: Ensure ESP32 is properly connected and powered

### Data Reading Issues
- **No valid data**: Check ESP32 code is sending voltage values
- **Invalid format**: Ensure ESP32 sends plain decimal numbers (e.g., "3.28")
- **Timeout errors**: Increase timeout value in `src/utils.py` if needed

## Development

### Adding Features
- Modify `src/utils.py` for new utility functions
- Update `main.py` for new main program logic
- Add new dependencies to `requirements.txt`

### Testing
- Test with known voltage sources for accuracy validation
- Verify serial communication with different ESP32 configurations
- Test CSV export with various data sets

## License

This project is open source. Feel free to modify and distribute as needed.

## Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.






