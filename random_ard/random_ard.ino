void setup() {
  Serial.begin(9600);
  randomSeed(10);
}

void loop() {
  // 0 에서 299 사이 임의 값 출력
  int randNumber = random(700);
  int randNumber2 = random(300);
  Serial.print(randNumber);
  Serial.println(',');
  Serial.print(randNumber2);
  Serial.println('/');
  delay(250);
}
