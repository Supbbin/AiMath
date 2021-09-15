#pip install opencv-python

import cv2
import time
print(cv2.__version__)

video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
time.sleep(2)
grabbed, frame = video_capture.read()
time.sleep(2)
# print(grabbed) #연결상태 확인 True


# cv2.imshow('webcam 영상', frame)
# cv2.waitKey(0)


cv2.imwrite('test.jpg', frame)
