import cv2
import mediapipe as mp
from mediapipe.tasks import python as mp_python
from mediapipe.tasks.python import vision

# Initialize global variables
latest_result = None
powered_on = False
print_counter = 0

# Callback function to receive results from the hand landmarker
def result_callback(result, image, timestamp):
    global latest_result
    latest_result = result

# Set up hand landmarker options and create the landmarker
options = vision.HandLandmarkerOptions(
    base_options=mp_python.BaseOptions(model_asset_path="hand_landmarker.task"),
    running_mode=vision.RunningMode.LIVE_STREAM,
    num_hands=2,
    result_callback=result_callback,
)
landmarker = vision.HandLandmarker.create_from_options(options)

# Function to determine if the hand is an open palm
def is_open_palm(hand_landmarks):
    tips = [4, 8, 12, 16, 20]
    bases = [2, 6, 10, 14, 18]
    fingers_up = 0
    for tip, base in zip(tips, bases):
        if hand_landmarks[tip].y < hand_landmarks[base].y:
            fingers_up += 1 # Count fingers that are up (tip above base)
    return fingers_up == 5

# Function to determine if the hand is tilting outward
def is_tilting_outward(hand_landmarks, is_right_hand):
    wrist = hand_landmarks[0]
    middle_tip = hand_landmarks[12]
    diff = middle_tip.x - wrist.x
    if is_right_hand:
        return diff < -0.05
    else:
        return diff > 0.05
    
# Function to determine if the hand is tilting inward
def is_tilting_inward(hand_landmarks, is_right_hand):
    wrist = hand_landmarks[0]
    middle_tip = hand_landmarks[12]
    diff = middle_tip.x - wrist.x
    if is_right_hand:
        return diff > 0.05
    else:
        return diff < -0.05
    
# Function to determine if the hand is a closed fist
def is_closed_fist(hand_landmarks):
    tips = [4, 8, 12, 16, 20]
    bases = [2, 6, 10, 14, 18]
    fingers_down = 0
    for tip, base in zip(tips, bases):
        if hand_landmarks[tip].y > hand_landmarks[base].y:
            fingers_down += 1
    return fingers_down >= 4

# Function to determine if the hand is pointing up (index finger up, others down)
def is_pointing_up(hand_landmarks):
    index_tip = hand_landmarks[8]
    index_base = hand_landmarks[5]
    middle_tip = hand_landmarks[12]
    ring_tip = hand_landmarks[16]
    pinky_tip = hand_landmarks[20]
    index_up = index_tip.y < index_base.y
    others_down = (middle_tip.y > index_tip.y and 
                   ring_tip.y > index_tip.y and 
                   pinky_tip.y > index_tip.y)
    return index_up and others_down

# Open the webcam
cap = cv2.VideoCapture(0)
timestamp_ms = 0

# Process video frames and perform hand landmark detection
while True:
    ret, frame = cap.read()
    if not ret:
        break
    # Convert the frame to RGB and create a MediaPipe image
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
    landmarker.detect_async(mp_image, timestamp_ms)
    timestamp_ms += 1

    # Draw hand landmarks and check for open palm gesture
    if latest_result and latest_result.hand_landmarks:
        for hand_landmarks in latest_result.hand_landmarks:
            for landmark in hand_landmarks:
                h, w = frame.shape[:2]
                x = int(landmark.x * w)
                y = int(landmark.y * h)
                cv2.circle(frame, (x, y), 5, (255, 255, 255), -1)

        # Check for gestures if two hands are detected
        if len(latest_result.hand_landmarks) == 2:
            hand1 = None
            hand2 = None
            for i, handedness in enumerate(latest_result.handedness):
                if handedness[0].category_name == "Right":
                    hand1 = latest_result.hand_landmarks[i]
                else:
                    hand2 = latest_result.hand_landmarks[i]
            if hand1 is None or hand2 is None:
                continue
            if not powered_on and is_open_palm(hand1) and is_open_palm(hand2):
                print("POWER ON")
                powered_on = True
            if is_closed_fist(hand1) and is_closed_fist(hand2):
                if powered_on:
                    print("POWER OFF")
                    powered_on = False
            hand1_is_right = True
            hand2_is_right = False
            if powered_on:
                if is_open_palm(hand1) and is_open_palm(hand2):
                    if is_tilting_outward(hand1, True) and is_tilting_outward(hand2, False):
                        print_counter += 1
                        print(f"{print_counter}.UP")
                    elif is_tilting_inward(hand1, True) and is_tilting_inward(hand2, False):
                        print_counter += 1
                        print(f"{print_counter}.DOWN")
                elif is_open_palm(hand1) and is_closed_fist(hand2):
                    print_counter += 1
                    print(f"{print_counter}. RIGHT")
                elif is_closed_fist(hand1) and is_open_palm(hand2):
                    print_counter += 1
                    print(f"{print_counter}. LEFT")

        if len(latest_result.hand_landmarks) == 1:
            hand1 = latest_result.hand_landmarks[0]
            if powered_on and is_pointing_up(hand1):
                print_counter += 1
                print(f"{print_counter}. 360")

    # Display the video feed with landmarks
    cv2.imshow('Video', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == 27:  # 27 is the ESC key
        break

# Resource cleanup
cap.release()
cv2.destroyAllWindows()
landmarker.close()