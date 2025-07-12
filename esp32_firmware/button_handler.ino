// esp32_firmware/button_handler.ino
// Kirim status tombol ke Pi (misalnya untuk wake assistant)

const int buttonPin = 13;
bool lastState = HIGH;

void setup() {
  pinMode(buttonPin, INPUT_PULLUP);
  Serial.begin(115200);
}

void loop() {
  bool current = digitalRead(buttonPin);
  if (current == LOW && lastState == HIGH) {
    Serial.println("BTN:PRESSED");
  }
  lastState = current;
  delay(100);
}
