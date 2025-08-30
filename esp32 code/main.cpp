#include <Arduino.h>

// ADC configuration
const int adcPin = 36;        // GPIO 36 (ADC1_CH0)
const float vRef = 3.3;       // Reference voltage
const int adcResolution = 12;  // 12-bit ADC resolution (0-4095)

void setup() {
  // Initialize serial communication
  Serial.begin(115200);
  
  // Configure ADC
  analogReadResolution(adcResolution);
  analogSetAttenuation(ADC_11db);  // 0-3.3V range
}

void loop() {

  int adcValue = analogRead(adcPin);

  // Calculate voltage
  float voltage = (adcValue * vRef) / ((1 << adcResolution) - 1);
  
  // Print results
  Serial.println(voltage, 3);
  // Wait before next reading
  delay(100);
}
