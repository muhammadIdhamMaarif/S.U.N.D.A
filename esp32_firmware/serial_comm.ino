// esp32_firmware/serial_comm.ino
// Kombinasi pengiriman data dari beberapa input

const int battPin = 34;
const int btnPin = 13;

void setup() {
  Serial.begin(115200);
  pinMode(btnPin, INPUT_PULLUP);
}

void loop() {
  // Kirim baterai
  int raw = analogRead(battPin);
  float voltage = raw * (3.3 / 4095.0) * 2;
  int percent = map(voltage * 100, 330, 420, 0, 100);
  percent = constrain(percent, 0, 100);
  Serial.print("BAT:");
  Serial.println(percent);

  // Kirim tombol
  if (digitalRead(btnPin) == LOW) {
    Serial.println("BTN:PRESSED");
  }

  delay(1000);
}
