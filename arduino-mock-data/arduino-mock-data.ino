void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}
void loop() {
  int randInt = random(2);
  if (randInt == 1) {
    digitalWrite(13, LOW);
    delay(50);
    digitalWrite(13, HIGH);
  }
  else {
    digitalWrite(13, LOW);
  }
  Serial.println(randInt);
  delay(1000);        // delay in between reads for stability
}



