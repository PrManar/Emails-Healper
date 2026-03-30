import cv2
import time
from vision.gesture_detector import detect_gesture

def start_camera():
  cap = cv2.VideoCapture(0)

  if not cap.isOpened():
    print('Cannot open camera')
    return
  
  # cap.set(cv2.CAP_PROP_FPS, 15)
  # time.sleep(2)
  cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

  # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
  # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

  while True:
    # cap.grab()

    ret, frame = cap.read()

    if not ret:
      print('Failed to grab frame')
      break

    frame, gesture = detect_gesture(frame)

    cv2.putText(frame, gesture, (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 2)

    cv2.imshow('Camera', frame)

    #press Q to exit
    if cv2.waitKey(1) == 0xFF == ord('q'):
      break

  cap.release()
  cv2.destroyAllWindows()