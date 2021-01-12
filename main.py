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
    # stitcher = cv2.createStitcher(True) if imutils.is_cv3() else cv2.Stitcher_create()

    # print(cv2.getBuildInformation())
    # for i in range(8):
    stitcher_process = StitcherProcess(queue=queue, out_queue=out_queue)
    stitcher_process.daemon = True
    stitcher_process.start()

    sum = 0
    counter = 0
    while True:
        start = time.time()

        frame = video.frame()
        frame1 = video1.frame()
        if frame is not None and frame1 is not None:
            # try:
            #     (status, stitched) = stitcher.stitch([frame, frame1])
            #     if status == 0:
            #         cv2.imshow("stitched", stitched)
            #         elapsed = time.time() - start
            #         counter += 1
            #         sum += elapsed
            #         print("Counter: ", counter)
            #         print("Avarage: ", sum / counter)
            #         print("Finish: ", elapsed)
            # except:
            #     pass
            # cv2.imshow("frame", frame)
            # cv2.imshow("frame1", frame1)
            # frame1 = video1.frame()
            queue.put_nowait([frame, frame1])


            if not out_queue.empty():
                stitched = out_queue.get_nowait()
                cv2.imshow('frame', stitched)
                elapsed = time.time() - start
                counter += 1
                sum += elapsed
                print("Counter: ", counter)
                print("Avarage: ", sum / counter)
                print("Finish: ", elapsed)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == "__main__":
    main()