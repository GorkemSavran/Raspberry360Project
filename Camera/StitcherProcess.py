from multiprocessing import Process, Queue
import imutils
from Camera.MJPGVideoReceiver import MJPGVideoReceiver
import cv2

class StitcherProcess(Process):

    def __init__(self, queue: Queue):
        super(StitcherProcess, self).__init__()
        self.queue: Queue = queue

    def run(self):
        cam0 = MJPGVideoReceiver(address="169.254.217.60", port=5600)
        cam1 = MJPGVideoReceiver(address="169.254.217.60", port=5600)
        stitcher = cv2.createStitcher(True) if imutils.is_cv3() else cv2.Stitcher_create()
        while True:

            try:
                (status, stitched) = stitcher.stitch([frame, frame1])
                if status == 0:
                    self.queue.put_nowait(stitched)
            except:
                pass
