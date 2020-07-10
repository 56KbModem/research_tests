#!/usr/bin/env python3
import numpy as np
import cv2


def get_stream(cap, vid_stream):
	frame_count = 0
	while True:
		ret, frame = cap.read()
		fps = cap.get(cv2.CAP_PROP_FPS)
		frame_count += 1
		if not ret:
			# we do need to reopen the capture...
			print("[!] cannot receive frame (stream ended?)\n[!] reopening...")
			print("[+] FRAME COUNT: {}".format(frame_count))
			print("[+] FPS: {}".format(round(fps,2)))
			print("[+] DURATION: {}s".format(round(frame_count / fps, 2)))
			frame_count = 0
			cap = cv2.VideoCapture(vid_stream)
			ret, frame = cap.read()

		cv2.imshow('webcam',frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			print("[!] user abort of stream")
			break




if __name__ == "__main__":
	vid_stream = "http://192.168.1.5:8080"
	cap = cv2.VideoCapture(vid_stream)

	if not cap.isOpened():
		print("[!] cannot open stream at {}".format(vid_stream))
		print("[!] exiting...")
		exit()
	else:
		print("[!] starting stream at {}".format(vid_stream))
		get_stream(cap, vid_stream)


cap.release()
cv2.destroyAllWindows()
