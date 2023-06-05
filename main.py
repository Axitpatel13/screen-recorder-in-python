import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
dimension = (width,height)

format = cv2.VideoWriter_fourcc(*"XVID")

video_output = cv2.VideoWriter('Recorded.mp4',format, 30.0, dimension)

Present_time = time.time()
Duration = 10
finish_time = Present_time + Duration

while True:
    picture = pyautogui.screenshot()
    frame = np.array(picture)
    frame_1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    video_output.write(frame_1)
    current_time =time.time()
    if current_time > finish_time:
        break
video_output.release()
