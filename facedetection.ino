#include <Servo.h>

int xang;
int yang;

Servo Servo1;//top
Servo Servo2;//bottom

int pinservtop=9;
int pinservbot=7;
void setup() {
	Serial.begin(115200); 
  Servo2.attach(pinservbot);
  Servo1.attach(pinservtop);
	Serial.setTimeout(1); 

}

void loop() {
  while (!Serial.available()); 
  String str = Serial.readStringUntil('\n');
  int comma = str.indexOf(','); 
  xang = str.substring(0, comma).toInt();
  yang =str.substring(comma +1).toInt();
  Servo1.write(xang);
  Servo2.write(yang);

}
