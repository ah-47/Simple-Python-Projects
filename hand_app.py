from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivy.uix.boxlayout import BoxLayout
import cv2
import mediapipe as mp
import time

# KV file to define the app layout
KV = '''
MDScreen:
    BoxLayout:
        orientation: 'vertical'
        CameraPreview:
            id: camera_preview
            size_hint: (1, 1)
            allow_stretch: True
            keep_ratio: True
        MDRaisedButton:
            text: "Click Me!!!"
            size_hint: None, None
            size: "200dp", "60dp"
            pos_hint: {"center_x": 0.5}
            on_release: app.click_btn()
        MDLabel:
            id: fps_label
            text: "FPS: 0"
            halign: "center"
'''

class CameraPreview(MDLabel):
    pass

class HandTrackingApp(MDApp):
    def build(self):
        self.screen = Builder.load_string(KV)
        return self.screen

    def click_btn(self):
        cam = cv2.VideoCapture(0)
        mp_hands = mp.solutions.hands
        hands = mp_hands.Hands()
        mp_draw = mp.solutions.drawing_utils
        prev_time = 0

        while True:
            success, img = cam.read()
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = hands.process(img_rgb)

            if results.multi_hand_landmarks:
                for landmarks in results.multi_hand_landmarks:
                    mp_draw.draw_landmarks(img, landmarks, mp_hands.HAND_CONNECTIONS)

            curr_time = time.time()
            fps = 1 / (curr_time - prev_time)
            prev_time = curr_time
            self.screen.ids.fps_label.text = f"FPS: {int(fps)}"

            cv2.imshow('Hand Tracking', img)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cam.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    HandTrackingApp().run()
