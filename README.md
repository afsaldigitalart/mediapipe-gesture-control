# Gesture-Controlled Robot Car

## Overview
This project is a work-in-progress robot car that will be controlled using hand gestures and an Arduino. The current version uses a rule-based system to detect gestures via OpenCV and MediaPipe. Future plans include implementing a machine learning-based system for more advanced gesture recognition. The ultimate goal is to achieve precise and seamless control over the robot car using hand movements, making it a highly interactive and intuitive system. The project aims to bridge the gap between human motion and robotic automation.

## Features
- Hand gesture recognition using OpenCV and MediaPipe for real-time tracking.
- Rule-based detection for basic gestures like pointing left, pointing right, open palm, and closed palm, ensuring reliable and responsive control.
- Real-time video processing for capturing and analyzing hand movements.
- Planned integration with Arduino for robot car control, allowing physical movement based on detected gestures.
- Future implementation of a machine learning-based gesture recognition system to enhance accuracy and adaptability.
- Potential expansion to include additional gestures for more complex commands and functionalities.

## Project Structure
```
├── main.py    # Gesture detection and hand tracking logic
├── robot_control.py  # Handles communication with Arduino (planned feature)
└── README.md  # Project documentation and instructions
```

## Dependencies
Ensure you have the following Python libraries installed before running the project:
```bash
pip install opencv-python mediapipe
```
These libraries enable hand tracking, gesture recognition, and real-time processing.

## How to Run
1. Connect a webcam to your system to capture hand gestures.
2. Run the script using the following command:
   ```bash
   python main.py
   ```
3. Use predefined gestures such as pointing left, pointing right, open palm, and closed palm to interact with the system.
4. Observe the gesture recognition output on the screen to ensure proper tracking.
5. Press `Esc` at any time to exit the application.

## Planned Enhancements
- Implement a communication module to send recognized gestures as commands to an Arduino-powered robot car.
- Develop a machine learning model trained on a diverse dataset of hand gestures to improve recognition accuracy.
- Expand the gesture set to include more nuanced and complex hand signals for advanced control.
- Optimize real-time processing to ensure smooth and low-latency responses.
- Improve the graphical interface to provide better feedback and visualization of detected gestures.
- Conduct extensive testing in various lighting conditions and environments to enhance robustness.

## Contributions
Contributions and suggestions are welcome! If you have ideas for improving the gesture recognition accuracy, robot control mechanisms, or expanding the feature set, feel free to fork the repository and submit a pull request. We encourage collaboration to refine and expand the project.

## License
This project is open-source under the MIT License, allowing anyone to modify, distribute, and contribute to its development. We believe in open collaboration and innovation in the field of gesture-based robotics.

