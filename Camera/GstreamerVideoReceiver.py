from Camera.VideoReceiver import VideoReceiver
import logging
import cv2
from threading import Thread


class GstreamerVideoReceiver(Thread):

    def __init__(self, address: str, port: int):
        Thread.__init__(self)
        if not address or not port:
            raise Exception("Please provide address and port")
        self.cap: cv2.VideoCapture = None
        self.address: str = address
        self.port: int = port
        self.__isRunning: bool = False
        self.__frame = None
        self.setupPipeline()
        self.daemon = True
        self.start()

    def setupPipeline(self):
        try:
            config = f"udpsrc address={self.address} port={self.port} ! application/x-rtp, payload=96 ! rtph264depay ! h264parse ! avdec_h264 ! decodebin ! videoconvert ! video/x-raw,format=(string)BGR ! videoconvert ! appsink"
            self.cap = cv2.VideoCapture(config, cv2.CAP_GSTREAMER)
        except:
            config = 'videotestsrc ! decodebin! videoconvert ! video/x-raw,format=(string)BGR ! videoconvert ! appsink'
            self.cap = cv2.VideoCapture(config, cv2.CAP_GSTREAMER)
        if not self.cap.isOpened():
            logging.error("Cap is not opened")
#udpsrc port=5600 ! application/x-rtp, payload=96 !rtph264depay ! h264parse ! avdec_h264 ! decodebin ! videoconvert ! video/x-raw,format=(string)BGR ! videoconvert ! appsink

    def run(self):
        """Thread execution"""
        while True:
            ret, self.__frame = self.cap.read()


    def frame(self):
        """Get frame"""
        return self.__frame
