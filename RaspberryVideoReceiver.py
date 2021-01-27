import time
import cv2
import numpy as np
import imutils
import threading


class RaspberryVideoReceiver(threading.Thread):
    def __init__(self, address=None, port=None):
        threading.Thread.__init__(self)
        if address and port:
            config = f"udpsrc address={address} port={port} ! application/x-rtp, payload=96 ! rtph264depay ! h264parse ! avdec_h264 ! decodebin ! videoconvert ! video/x-raw,format=(string)BGR ! videoconvert ! appsink"
        else:
            config = 'videotestsrc ! decodebin! videoconvert ! video/x-raw,format=(string)BGR ! videoconvert ! appsink'
        self.cap = cv2.VideoCapture(config, cv2.CAP_GSTREAMER)
        if not self.cap.isOpened():
            raise Exception("Cap is not opened")
        self.__frame = None

    def run(self):
        while True:
            ret, self.__frame = self.cap.read()

    def frame(self):
        return self.__frame

