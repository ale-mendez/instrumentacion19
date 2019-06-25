float val;
int b = 0;
String inString = "";


void setup() 
{
  Serial.begin(9600);
  analogReadResolution(8);
  analogWriteResolution(8);
  Serial.setTimeout(50);
//  while (!Serial) {
 //   ;
//  }
//  pinMode(DAC1, OUTPUT);
//  pinMode(A0, INPUT);
}

void loop() 
{

  //while (Serial.available() > 0) {
    int inChar = Serial.read();
    if (isDigit(inChar)) {
      // convert the incoming byte to a char and add it to the string:
      inString += (char)inChar;
    }
     if (inChar == '\n') {
      b = inString.toInt();
      Serial.println(b);
     }
  //}
  
  
  if(b > 0){
    
    if(b>254)
      b=254;

    analogWrite(DAC1, b);

    b = 0;
    inString = "";
    }

  //val = analogRead(A0);
  //Serial.println(val);

  delay(100);
}
