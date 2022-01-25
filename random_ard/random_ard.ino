void setup() {
  Serial.begin(9600);
  randomSeed(10);
}

void loop() {
  // 0 에서 299 사이 임의 값 출력
  int randNumber = analogRead(A0);
  Serial.println(randNumber);
  delay(100);
}
