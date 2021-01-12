import RaspberryVideoReceiver as rp
import cv2
from multiprocessing import Queue
import imutils
from StitcherProcess import StitcherProcess
import time

def main():
    queue = Queue()
    out_queue = Queue()
    video = rp.RaspberryVideoReceiver(address="192.168.2.1", port=5600)
    video1 = rp.RaspberryVideoReceiver(address="192.168.3.1", port=5604)

    stitcher_process = StitcherProcess(queue=queue, out_queue=out_queue)
    stitcher_process.daemon = True
    stitcher_process.start()

    while True:
        start = time.time()
        frame = video.frame()
        frame1 = video1.frame()
        if frame is not None and frame1 is not None:
            queue.put([frame, frame1])

            if not out_queue.empty():
                stitched = out_queue.get()
                cv2.imshow('frame1', stitched)
                print("Finish: ", (time.time() - start))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == "__main__":
    main()