#pip install opencv-python
import time
import cv2
print(cv2.__version__)
video_capture = cv2.VideoCapture(0)
time.sleep(3)
grabbed, frame = video_capture.read()

print(grabbed)