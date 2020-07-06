#!/usr/bin/env python3
import numpy as np
import cv2

cap = cv2.VideoCapture("http://192.168.1.5:8080")

while True:
    while(cap.isOpened()):
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('webcam',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
