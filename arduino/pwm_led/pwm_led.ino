const int LED=9;
int i;

void setup(){
  Serial.begin(9600); 
  pinMode(LED,OUTPUT);
}

void loop() {
  for (i=1;i<40; i++){
    analogWrite(LED,i);
    delay(100);
  }
  for (i=40;i>0; i--){
    analogWrite(LED,i);
    delay(100);
  }
}
