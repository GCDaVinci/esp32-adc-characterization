# ESP32 ADC Characterization

This script is for characterizing the ESP32's 12-bit ADC performance by comparing measured voltage values with serial readings from the device. Note this script runs independently from the ESP32. The ESP32 must already be coded and flashed to be contiously reading ADC values, converting them to voltage values, and then printing the data to the serial port.

## Overview

This project helps you evaluate the accuracy and linearity of your ESP32's ADC by:
- Reading voltage values from the ESP32 via serial communication
- Comparing them with manually measured reference voltages
- Calculating the difference/error between measured and serial values
- Exporting all data to CSV format for analysis

## Hardware Setup

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

```
=== Python Serial Communication Project ===
This script will continuously compare your measured voltages with serial data
Type 'end' to save data to CSV and exit
Press Ctrl+C to exit without saving
------------------------------------------------------------

Enter measured voltage (3-digit number, e.g., 3.30) or 'end' to save and exit: 3.30
Reading serial data for measured voltage: 3.30V
Reading from COM3 at 115200 baud...
Waiting for valid voltage data...
Received: 3.28
[14:30:22] Serial: 3.280V | Measured: 3.300V | Difference: -0.020V
✓ Voltage comparison completed and stored
------------------------------------------------------------

Enter measured voltage (3-digit number, e.g., 3.30) or 'end' to save and exit: end

Saving 1 measurements to CSV...
✓ Data saved to voltage_comparison_20241201_143022.csv
✓ Total measurements: 1
Goodbye!
```

### Configuration

The default serial settings are:
- **Port**: COM3 (Windows) - modify in `src/utils.py` if needed
- **Baud rate**: 115200
- **Data bits**: 8
- **Parity**: None
- **Stop bits**: 1

## Output

### CSV File Format

The program generates CSV files with the following columns:
- **Timestamp**: Time of measurement (HH:MM:SS)
- **Measured Voltage (V)**: Your reference voltage measurement
- **Serial Voltage (V)**: Voltage read from ESP32 via serial
- **Difference (V)**: Calculated difference (Serial - Measured)

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
