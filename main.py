import cv2
import mediapipe as mp
from arduino import Arduino

"""
This function checks whether the palm is open or close and return landmarks
if open
"""
def palm_open(landmarks):
    tip_ids = [4, 8, 12, 16, 20]  
    pip_ids = [3, 6, 10, 14, 18]  
    open_fingers = 0

    if landmarks.landmark[tip_ids[0]].x < landmarks.landmark[pip_ids[0]].x:
        open_fingers += 1


    for i in range(1, 5):
        if landmarks.landmark[tip_ids[i]].y < landmarks.landmark[pip_ids[i]].y:
            open_fingers += 1

    return open_fingers >= 4 

ard = Arduino()

print("LOADING, PLEASE WAIT")

#Initializing the Mediapipe Module
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1,min_detection_confidence=0.5, min_tracking_confidence=0.5)


cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb_frame)
    cv2.putText(frame, "Press Esc to Stop", (450,450), cv2.FONT_HERSHEY_PLAIN, 1, (255,15,0), 1, cv2.LINE_AA)
        
    if results.multi_hand_landmarks:
        for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            if handedness.classification[0].label == "Right" : #Disabled left hand as rule based system is working poor on it
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                mp_draw.DrawingSpec(color=(0, 0, 255), thickness=3, circle_radius=2),  
                mp_draw.DrawingSpec(color=(255, 255, 255), thickness=2))

                #All the major Landmarks
                wrist = hand_landmarks.landmark[0]
                index = hand_landmarks.landmark[8]
                index_middle = hand_landmarks.landmark[6]
                index_base = hand_landmarks.landmark[5]
                middle =hand_landmarks.landmark[12]
                middle_base = hand_landmarks.landmark[9]
                middle_middle = hand_landmarks.landmark[10]
                ring = hand_landmarks.landmark[16]
                ring_middle = hand_landmarks.landmark[14]
                pinky = hand_landmarks.landmark[20]
                pinky_middle= hand_landmarks.landmark[18]
                
                #added a threshold to make it less sensitive to gestures  
                pointing_threshold = 0.09
                

                #Left Pointing Rule
                if index.x < wrist.x - pointing_threshold and index.x < index_base.x  - pointing_threshold  and index.x < middle_base.x - pointing_threshold :  # Tip is above the base
                        cv2.putText(frame, "Moving Left", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 
                                    1, (0, 0 ,255), 2, cv2.LINE_AA)
                        
                        ard.send_to_arduino("L")
                        
                
                
                #Pointing Right Rule
                elif index.x > wrist.x - pointing_threshold  and index.x > index_base.x - pointing_threshold  and index.x - pointing_threshold  > middle_base.x - pointing_threshold  :  # Tip is below the base
                        cv2.putText(frame, "Moving Right", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 
                                    1, (0, 0, 255), 2, cv2.LINE_AA)

                        ard.send_to_arduino("R")

                #Checks palm condition
                else:

                    if palm_open(hand_landmarks):
                        cv2.putText(frame, "Moving Backward", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 
                                    1, (0, 255, 0), 2, cv2.LINE_AA)

                        ard.send_to_arduino("B")

                    else:
                        cv2.putText(frame, "Moving Forward", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 
                                    1, (0, 255, 0), 2, cv2.LINE_AA, )

                        ard.send_to_arduino("F")
                        
            elif handedness.classification[0].label == "Right" and handedness.classification[0].label == "Left":
                cv2.putText(frame, "Stopping", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 
                                    1, (0, 255, 0), 2, cv2.LINE_AA, )

                ard.send_to_arduino("Q")

    else:
         ard.send_to_arduino("Q")                

    cv2.imshow("Hand Tracking", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
