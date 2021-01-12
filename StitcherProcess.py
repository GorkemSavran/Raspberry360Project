from multiprocessing import Process, Queue
import imutils
import time
import numpy as np
import cv2

class StitcherProcess(Process):

    def __init__(self, queue: Queue, out_queue: Queue):
        super(StitcherProcess, self).__init__()
        self.queue = queue
        self.out_queue = out_queue

    def run(self):
        stitcher = cv2.createStitcher() if imutils.is_cv3() else cv2.Stitcher_create()
        while True:
            if not self.queue.empty():
                frame, frame1 = self.queue.get()
                try:
                    (status, stitched) = stitcher.stitch([frame, frame1])
                    if status == 0:
                        self.out_queue.put(stitched)
                except:
                    pass
