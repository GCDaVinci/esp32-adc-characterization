"""
Utility functions for the Python project.
"""

import serial
import time
import csv
import os
from datetime import datetime

def read_serial_data(measured_voltage, port='COM3', baudrate=115200, timeout=1):
    """
    Read one voltage value from the serial port and compare with measured voltage.
    Keeps the serial port open until a valid number is read.
    
    Args:
        measured_voltage (float): The measured voltage to compare against
        port (str): Serial port name (default: COM3)
        baudrate (int): Baud rate (default: 115200)
        timeout (int): Read timeout in seconds (default: 1)
    
    Returns:
        tuple: (serial_voltage, success_flag) where success_flag is True if voltage was read successfully
    """
    try:
        # Configure serial connection
        ser = serial.Serial(
            port=port,
            baudrate=baudrate,
            timeout=timeout,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE
        )
        
        print(f"Reading from {port} at {baudrate} baud...")
        print("Waiting for valid voltage data...")
        
        # Keep reading until we get a valid number
        while True:
            try:
                # Wait for data to be available
                if ser.in_waiting == 0:
                    time.sleep(0.1)
                    continue
                
                # Read one line of data
                data = ser.readline()
                if data:
                    # Decode bytes to string and strip whitespace
                    decoded_data = data.decode('utf-8').strip()
                    print(f"Received: {decoded_data}")
                    
                    # Try to extract voltage as a simple decimal number
                    try:
                        serial_voltage = float(decoded_data)
                        timestamp = time.strftime("%H:%M:%S")
                        difference = serial_voltage - measured_voltage
                        print(f"[{timestamp}] Serial: {serial_voltage:.3f}V | Measured: {measured_voltage:.3f}V | Difference: {difference:+.3f}V")
                        ser.close()
                        return serial_voltage, True
                    except ValueError:
                        print("Not a valid number, continuing to read...")
                        continue
                else:
                    time.sleep(0.1)
                    continue
                    
            except Exception as e:
                print(f"Error reading data: {e}")
                continue
                
    except serial.SerialException as e:
        print(f"Error opening serial port {port}: {e}")
        print("Make sure the device is connected and the port is correct.")
        return None, False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None, False
    finally:
        # Close the serial connection
        if 'ser' in locals() and ser.is_open:
            ser.close()

def save_to_csv(voltage_data, filename=None):
    """
    Save voltage comparison data to a CSV file.
    
    Args:
        voltage_data (list): List of tuples (timestamp, measured_voltage, serial_voltage, difference)
        filename (str): Optional filename, defaults to timestamp-based name
    """
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"voltage_comparison_{timestamp}.csv"
    
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            
            # Write header
            writer.writerow(['Timestamp', 'Measured Voltage (V)', 'Serial Voltage (V)', 'Difference (V)'])
            
            # Write data
            for timestamp, measured, serial, difference in voltage_data:
                writer.writerow([timestamp, f"{measured:.3f}", f"{serial:.3f}", f"{difference:+.3f}"])
        
        print(f"✓ Data saved to {filename}")
        print(f"✓ Total measurements: {len(voltage_data)}")
        
    except Exception as e:
        print(f"✗ Error saving to CSV: {e}")
