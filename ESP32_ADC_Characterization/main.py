#!/usr/bin/env python3
"""
Main entry point for the Python project.
Continuously prompts for measured voltage, reads one serial value, then asks for next.
Saves data to CSV when user types "end".
"""

from src.utils import read_serial_data, save_to_csv
from datetime import datetime

def get_measured_voltage():
    """Get measured voltage input from user."""
    while True:
        try:
            user_input = input("Enter measured voltage (3-digit number, e.g., 3.30) or 'end' to save and exit: ").strip().lower()
            
            if user_input == 'end':
                return 'end'
            
            # Check if input is a valid 3-digit number
            if len(user_input) <= 5 and user_input.replace('.', '').replace('-', '').isdigit():
                voltage = float(user_input)
                if 0 <= voltage <= 999:
                    return voltage
                else:
                    print("Please enter a voltage between 0 and 999V")
            else:
                print("Please enter a valid 3-digit number (e.g., 3.30, 12.5, 100) or 'end' to save and exit")
                
        except ValueError:
            print("Please enter a valid number")
        except KeyboardInterrupt:
            print("\nExiting...")
            exit(0)

def main():
    """Main function that continuously prompts for voltage and reads serial data."""
    print("=== Python Serial Communication Project ===")
    print("This script will continuously compare your measured voltages with serial data")
    print("Type 'end' to save data to CSV and exit")
    print("Press Ctrl+C to exit without saving")
    print("-" * 60)
    
    # List to store voltage comparison data
    voltage_data = []
    
    while True:
        try:
            print()
            # Get measured voltage from user
            user_input = get_measured_voltage()
            
            if user_input == 'end':
                if voltage_data:
                    print(f"\nSaving {len(voltage_data)} measurements to CSV...")
                    save_to_csv(voltage_data)
                else:
                    print("No data to save.")
                print("Goodbye!")
                break
            
            measured_voltage = user_input
            print(f"Reading serial data for measured voltage: {measured_voltage}V")
            
            # Read one voltage value from COM3
            result = read_serial_data(measured_voltage)
            if result:
                serial_voltage, success = result
                if success:
                    # Calculate difference and store data
                    difference = serial_voltage - measured_voltage
                    timestamp = datetime.now().strftime("%H:%M:%S")
                    voltage_data.append((timestamp, measured_voltage, serial_voltage, difference))
                    print("✓ Voltage comparison completed and stored")
                else:
                    print("✗ Failed to read voltage from serial port")
            else:
                print("✗ Failed to read voltage from serial port")
            
            print("-" * 60)
            
        except KeyboardInterrupt:
            print("\nExiting without saving...")
            break
        except Exception as e:
            print(f"Error: {e}")
            print("Continuing with next measurement...")

if __name__ == "__main__":
    main()
