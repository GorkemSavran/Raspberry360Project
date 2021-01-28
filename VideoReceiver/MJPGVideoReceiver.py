import VideoReceiver

class RaspberryVideoReceiver(VideoReceiver):
    def __init__(self, address:str="192.168.2.1", port:int=5600):
        VideoReceiver.__init__(self)
        self.cap: cv2.VideoCapture = None
        if address and port and not isGstreamer:
            config = f"http://{address}:{port}/stream.mjpg"
            self.cap = cv2.VideoCapture(config)
        elif address and port and isGstreamer:
            config = f"udpsrc address={address} port={port} ! application/x-rtp, payload=96 ! rtph264depay ! h264parse ! avdec_h264 ! decodebin ! videoconvert ! video/x-raw,format=(string)BGR ! videoconvert ! appsink"
            self.cap = cv2.VideoCapture(config, cv2.CAP_GSTREAMER)
        else:
            config = 'videotestsrc ! decodebin! videoconvert ! video/x-raw,format=(string)BGR ! videoconvert ! appsink'
            self.cap = cv2.VideoCapture(config, cv2.CAP_GSTREAMER)
        if not self.cap.isOpened():
            raise Exception("Cap is not opened")
        self.__frame = None
        self.daemon = True
        self.start()

    def run(self):
        while True:
            ret, self.__frame = self.cap.read()

    def frame(self):
        return self.__frame