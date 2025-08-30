#include <Arduino.h>

// ADC configuration
const int adcPin = 36;        // GPIO 36 (ADC1_CH0)
const float vRef = 3.3;       // Reference voltage
const int adcResolution = 12;  // 12-bit ADC resolution (0-4095)
const int samples = 100;       // Number of samples for averaging

void setup() {
  // Initialize serial communication
  Serial.begin(115200);
  //Serial.println("ESP32 ADC Voltage Reader");
  //Serial.println("Reading from GPIO 36 (ADC1_CH0)");
  //Serial.println("Reference voltage: 3.3V");
  //Serial.println("ADC Resolution: 12-bit");
  //Serial.println("----------------------------------------");
  
  // Configure ADC
  analogReadResolution(adcResolution);
  analogSetAttenuation(ADC_11db);  // 0-3.3V range
}

void loop() {

  int adcValue = analogRead(adcPin);
  /*
  // Read multiple samples and average them for better accuracy
  long adcSum = 0;
  
  for (int i = 0; i < samples; i++) {
    adcSum += analogRead(adcPin);
    delayMicroseconds(100);  // Small delay between readings
  }
  
  // Calculate average ADC value
  int adcValue = adcSum / samples;
  */

  // Calculate voltage
  float voltage = (adcValue * vRef) / ((1 << adcResolution) - 1);
  
  // Print results
 // Serial.print("ADC Value: ");
  //Serial.print(adcValue);
  //Serial.print(" | Voltage: ");
  Serial.println(voltage, 3);
  //Serial.println("V");
  
  // Wait before next reading
  delay(100);
}