from threading import Thread
from cv2 import VideoCapture


class VideoReceiver(Thread):

    def __init__(self, address: str, port: int):
        Thread.__init__(self)
        if not address or not port:
            raise Exception("Please provide address and port")
        self.cap: VideoCapture = None
        self.address: str = address
        self.port: int = port
        self.__isRunning: bool = False
        self.__frame = None
        self.setupPipeline()
        self.start()
        self.startExecution()

    def setupPipeline(self):
        """Setup the pipeline"""
        raise NotImplementedError

    def run(self):
        """Thread execution"""
        while self.__isRunning:
            self.task()

    def task(self):
        """
        Script that we run
        Get frame
        """
        ret, self.__frame = self.cap.read()

    def frame(self):
        """Get frame"""
        return self.__frame

    def startExecution(self):
        """Start Execution"""
        self.__isRunning = True

    def stopExecution(self):
        """Stop Execution"""
        self.__isRunning = False