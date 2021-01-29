import logging
from Camera.VideoReceiver import VideoReceiver


class MJPGVideoReceiver(VideoReceiver):

    def __init__(self, address: str, port: int):
        super(MJPGVideoReceiver, self).__init__(address=address, port=port)

    def setupPipeline(self):
        try:
            config = f"http://{self.address}:{self.port}/stream.mjpg"
            self.cap = cv2.VideoCapture(config)
        except:
            logging.error("Error when creating pipeline")
        if not self.cap.isOpened():
            raise Exception("Cap is not opened")