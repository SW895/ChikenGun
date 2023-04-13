#include <Stepper.h>
#define STEPS 200

Stepper stepper_x(STEPS, 2, 3);
Stepper stepper_y(STEPS, 5, 6);

//#define motorInterfaceType 1
//#define motorInterfaceType 2

void setup() {
    Serial.begin(9600);
    stepper_x.setSpeed(1000);
    stepper_y.setSpeed(1000);
}

void loop() {
    if (Serial.available() > 0)
    {
      Serial.println("string received");      
      long coor_x = Serial.parseInt();
      long coor_y = Serial.parseInt();
      Serial.println("X coordinate:");
      Serial.println(coor_x);
      Serial.println("Y coordinate:");
      Serial.println(coor_y);
      //stepper_x.step(engine_x);
      //stepper_y.step(engine_y);
    }  
}
