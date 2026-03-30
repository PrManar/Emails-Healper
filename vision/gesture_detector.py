import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands()

def detect_gesture(frame):
  rgb = cv2.cvtColor(frame , cv2.COLOR_BAYER_BG2RGB)
  result = hands.process(rgb)

  gesture = 'unknown'

  if result.multi_hand_landmarks:
    for hand_landmarks in result.multi_hand_landmarks:

      mp_draw.draw_landmarks(
        frame,
        hand_landmarks,
        mp_hands.HAND_CONNECTIONS
      )

      thump_tip = hand_landmarks.landmark[4]
      thump_ip = hand_landmarks.landmark[3]

      if thump_tip.y < thump_ip.y:
        gesture = 'thumbs_up'
      else:
        gesture = 'thumbs_down'
  return frame, gesture
