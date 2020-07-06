#!/usr/bin/env python3
import numpy as np
import cv2

vid_stream = "http://192.168.1.5:8080"
cap = cv2.VideoCapture(vid_stream)
frame_count = 0

if not cap.isOpened():
    print("[!] cannot open stream\n[!] exiting...")
    exit()

while True:
    ret, frame = cap.read()
    frame_count += 1
    if not ret:
        print("[!] cannot receive frame (stream ended?)\n[!] exiting...")
        break

    if frame_count == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        frame_count = 0
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('webcam',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
