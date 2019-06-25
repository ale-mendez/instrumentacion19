/*
  String to Integer conversion

  Reads a serial input string until it sees a newline, then converts the string
  to a number if the characters are digits.

  The circuit:
  - No external components needed.

  created 29 Nov 2010
  by Tom Igoe

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/StringToInt
*/

char inString = 0;    // string to hold input
char outString = 0;    // string to hold input

void setup() {
  Serial.begin(9600);
}

void loop() {
  inString = Serial.read();

  if(inString != -1)
  {
    outString = inString;
    }
  Serial.print(outString);
}
