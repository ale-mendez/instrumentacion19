 
// Incluímos la librería para poder utilizarla
#include <Stepper.h>
 
int in1Pin = 8;
int in2Pin = 10;
int in3Pin = 9;
int in4Pin = 11;
int maxsteps = 2048; // número de pasos en un minuto (full step mode)
//int maxsteps = 4096; // número de pasos en un minuto (half step mode)
int nstops = 8;  // number of stops 
int nsteps = maxsteps/nstops; // número de pasos que queremos que de
int stepCount = 0; 
 
// Constructor, pasamos STEPS y los pines donde tengamos conectado el motor
Stepper motor(maxsteps, in1Pin, in2Pin, in3Pin, in4Pin);
 
void setup() {
  // initialize the serial port:
  Serial.begin(9600);
  // Asignamos la velocidad en RPM (Revoluciones por Minuto)
  motor.setSpeed(5);
}
 
void loop() {

  // Step one revolution in one direction:
  Serial.println("clockwise");
  motor.step(nsteps);
  delay(500);
  // Step one revolution in the other direction:
  Serial.println("counterclockwise");
  motor.step(-nsteps);
  delay(500);

  
//  // Movemos el motor un número determinado de pasos
//  int init=Serial.read();
//  if (init>0) {
//    Serial.print('Initiate motor');
//    for 
//    motor.step(nsteps);
//    Serial.print("steps:");
//    Serial.println(stepCount);
//    stepCount++;
//    delay(3000);
//  }

//  motor.step(-nsteps);
//  delay(3000);


}
