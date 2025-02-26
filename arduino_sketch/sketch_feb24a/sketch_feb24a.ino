#include <AFMotor.h> // Include the AFMotor library

// Create motor objects
AF_DCMotor motor1(1); // Motor 1 on M1
AF_DCMotor motor2(2); // Motor 2 on M2
AF_DCMotor motor3(3); // Motor 3 on M3
AF_DCMotor motor4(4); // Motor 4 on M4


void moveFront(){
  
  motor1.setSpeed(80);
  motor2.setSpeed(80);
  motor3.setSpeed(80);
  motor4.setSpeed(80);
  motor1.run(FORWARD);
  motor2.run(FORWARD);
  motor3.run(FORWARD);
  motor4.run(FORWARD);

}

void moveBack(){
  
  motor1.setSpeed(80);
  motor2.setSpeed(80);
  motor3.setSpeed(80);
  motor4.setSpeed(80);
  motor1.run(BACKWARD);
  motor2.run(BACKWARD);
  motor3.run(BACKWARD);
  motor4.run(BACKWARD);

}

void moveLeft(){
  motor1.setSpeed(180);
  motor2.setSpeed(180);
  motor3.setSpeed(180);
  motor4.setSpeed(180);
  motor1.run(FORWARD);
  motor2.run(FORWARD);
  motor3.run(BACKWARD);
  motor4.run(BACKWARD);

}

void moveRight(){
  motor1.setSpeed(180);
  motor2.setSpeed(180);
  motor3.setSpeed(180);
  motor4.setSpeed(180);
  motor1.run(BACKWARD);
  motor2.run(BACKWARD);
  motor3.run(FORWARD);
  motor4.run(FORWARD);
}

void stop(){
  motor1.run(RELEASE);
  motor2.run(RELEASE);
  motor3.run(RELEASE);
  motor4.run(RELEASE);
}


void setup() {
  Serial.begin(9600);
}

void loop() {
  if(Serial.available()){
    String command = Serial.readStringUntil('\n');
    if (command == "S"){
      stop();
    }
    else if (command == "F"){
      moveFront();
    }
    else if (command == "L"){
      moveLeft();
    }
    else if (command == "R"){
      moveRight();
    }
    else if (command == "B"){
      moveBack();
    }
    else if (command == "Q"){
      stop();
    }


  }}
