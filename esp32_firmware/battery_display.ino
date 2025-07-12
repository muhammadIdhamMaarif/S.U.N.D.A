// esp32_firmware/battery_display.ino
// Kirim status baterai melalui Serial setiap detik

int batteryPin = 34;

void setup() {
  Serial.begin(115200);
}

void loop() {
  int raw = analogRead(batteryPin);
  float voltage = raw * (3.3 / 4095.0) * 2; // asumsikan voltage divider
  int percent = map(voltage * 100, 330, 420, 0, 100); // 3.3V - 4.2V

  percent = constrain(percent, 0, 100);
  Serial.print("BAT:");
  Serial.println(percent);
  delay(1000);
}
