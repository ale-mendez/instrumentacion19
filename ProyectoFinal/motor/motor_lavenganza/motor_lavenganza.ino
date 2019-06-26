
int iPin = 10;
int istep = 0;

void setup() {
  Serial.begin(9600);
  pinMode(iPin,OUTPUT);
  Serial.setTimeout(50);
}

void loop() {
  istep = Serial.parseInt();
  if (istep>0) {
    Serial.println("One step now: \n");
    Serial.println(istep);
    digitalWrite(iPin , LOW);
    delay(100);
    digitalWrite(iPin , HIGH);
    delay(100);
    digitalWrite(iPin , LOW);
    delay(100);
    digitalWrite(iPin , HIGH);
    istep=0;
  }
}
