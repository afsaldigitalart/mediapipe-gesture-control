# Gesture-Controlled Robot Car

## Overview
This project is a gesture-controlled robot car that operates using hand gestures and an Arduino. The system utilizes OpenCV and MediaPipe to recognize hand movements and send commands to the Arduino, which controls the robot's motion. The goal is to provide an intuitive and interactive way to control a robot car without physical controllers, bridging the gap between human motion and robotic automation.

## Features
- Hand gesture recognition using OpenCV and MediaPipe for real-time tracking.
- Rule-based detection for basic gestures like pointing left, pointing right, open palm, and closed palm, ensuring reliable and responsive control.
- Real-time video processing for capturing and analyzing hand movements.
- Communication with an Arduino to translate detected gestures into motor control commands.
- Smooth and low-latency responses for seamless control.

## Project Structure
```
├── main.py     # Gesture detection and hand tracking logic
├── arduino.py  # Handles communication with Arduino
└── README.md   # Project documentation and instructions
```

## Dependencies
Ensure you have the following Python libraries installed before running the project:
```bash
pip install -r requirements.txt
```
These libraries enable hand tracking, gesture recognition, real-time processing, and serial communication with the Arduino.

## Hardware Requirements
- Arduino Uno (or compatible microcontroller)
- L293D motor driver module
- Four DC motors
- Laptop with a webcam
- Jumper wires and power supply

## How to Run
1. Connect a webcam to your system to capture hand gestures.
2. Upload the Arduino code to your Arduino board.
3. Run the script using the following command:
   ```bash
   python main.py
   ```
4. Use predefined gestures such as pointing left, pointing right, open palm, and closed palm to control the robot car.
5. Observe the movement of the robot car as it responds to your gestures.
6. Press `Esc` at any time to exit the application.

## Future Improvements
- Expand the gesture set to include more complex commands.
- Improve graphical feedback for detected gestures.
- Optimize real-time processing for enhanced performance.
- Conduct extensive testing in various lighting conditions and environments to improve robustness.

## Contributions
Contributions and suggestions are welcome! If you have ideas for improving gesture recognition, robot control mechanisms, or expanding the feature set, feel free to fork the repository and submit a pull request.

## License
This project is open-source under the MIT License, allowing anyone to modify, distribute, and contribute to its development. We encourage collaboration to refine and expand the project.

