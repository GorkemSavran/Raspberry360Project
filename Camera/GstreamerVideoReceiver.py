from Camera.VideoReceiver import VideoReceiver
import logging
import cv2


class GstreamerVideoReceiver(VideoReceiver):

    def __init__(self, address: str, port: int):
        super(GstreamerVideoReceiver, self).__init__(address=address, port=port)

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
