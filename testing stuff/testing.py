import cv2
import mediapipe as mp

# Initialize mediapipe hands model
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# Initialize the video capture
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Convert the color to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Flip the frame horizontally for a later selfie-view display
    rgb_frame = cv2.flip(rgb_frame, 1)

    # Process the frame with mediapipe
    results = hands.process(rgb_frame)

    # Draw the hand annotations on the frame
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Check which fingers are up
            thumb = hand_landmarks.landmark[4].y < hand_landmarks.landmark[3].y
            index = hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y
            middle = hand_landmarks.landmark[12].y < hand_landmarks.landmark[10].y
            ring = hand_landmarks.landmark[16].y < hand_landmarks.landmark[14].y
            pinky = hand_landmarks.landmark[20].y < hand_landmarks.landmark[18].y

            fingers = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
            up_fingers = [f for f, v in zip(fingers, [thumb, index, middle, ring, pinky]) if v]

            print(f"Fingers up: {', '.join(up_fingers) if up_fingers else 'None'}")

    # Display the resulting frame
    cv2.imshow('Hand Tracking', frame)

    if cv2.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
