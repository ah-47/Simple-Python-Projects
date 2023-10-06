from tkinter import *
import cv2
import mediapipe as mp
import time

window = Tk()

def clickBtn():

    # Initialize the webcam
    cam = cv2.VideoCapture(0)

    # Initialize the MediaPipe Hands module
    mpHands = mp.solutions.hands
    hands = mpHands.Hands()

    # Initialize the MediaPipe Drawing Utilities
    mpDraw = mp.solutions.drawing_utils

    # Variables for FPS calculation
    prev_time = 0
    curr_time = 0

    while True:
        # Read a frame from the webcam
        success, img = cam.read()

        # Convert the frame to RGB format (MediaPipe requires RGB input)
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Process the frame with the Hands module
        results = hands.process(imgRGB)

        # Uncomment the following line to see the hand landmarks data
        # print(results.multi_hand_landmarks)

        # Draw landmarks and hand connections if hands are detected
        if results.multi_hand_landmarks:
            for landmarks in results.multi_hand_landmarks:
                # Draw the landmarks on the frame
                mpDraw.draw_landmarks(img, landmarks, mpHands.HAND_CONNECTIONS)
        
        # Calculate and display FPS
        curr_time = time.time()
        fps = 1 / (curr_time - prev_time)
        prev_time = curr_time
        cv2.putText(img, f"FPS: {int(fps)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Display the frame with landmarks and FPS
        cv2.imshow('Hand Tracking', img)

        # Exit the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close OpenCV windows
    cam.release()
    cv2.destroyAllWindows()

# Buttons 

myButton = Button(window, text = 'Click Me!!!', command=clickBtn) 

# to disable this button we have to add state = 'disabled'

# to change the size of button we have to do padx = ? and pady = ?

myButton.pack()

window.mainloop()