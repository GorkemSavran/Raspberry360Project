from RaspberryVideoReceiver import RaspberryVideoReceiver
import cv2
from multiprocessing import Queue
import imutils
from StitcherProcess import StitcherProcess
import time

def main():
    # queue = Queue()
    # out_queue = Queue()
    video = RaspberryVideoReceiver(address="192.168.0.20", port=5600)
    video.daemon = True
    video.start()
    video = RaspberryVideoReceiver(address="192.168.0.20", port=5600)
    video.daemon = True
    video.start()
    # video1 = RaspberryVideoReceiver(address="192.168.3.1", port=5604)
    # stitcher = cv2.createStitcher(True) if imutils.is_cv3() else cv2.Stitcher_create()

    # print(cv2.getBuildInformation())
    # for i in range(8):
    # stitcher_process = StitcherProcess(queue=queue, out_queue=out_queue)
    # stitcher_process.daemon = True
    # stitcher_process.start()

    sum = 0
    counter = 0
    while True:
        start = time.time()

        frame = video.frame()
        # frame1 = video1.frame()
        if frame is not None:
            cv2.imshow("frame", frame)
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
            # queue.put_nowait([frame, frame1])
            #
            #
            # if not out_queue.empty():
            #     stitched = out_queue.get_nowait()
            #     cv2.imshow('frame', stitched)
            #     elapsed = time.time() - start
            #     counter += 1
            #     sum += elapsed
            #     print("Counter: ", counter)
            #     print("Avarage: ", sum / counter)
            #     print("Finish: ", elapsed)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

import serial
import tkinter
from tkinter import Label, StringVar, RAISED
import threading
from RadioSerialConnection.RadioSerialConnection import RadioSerialConnection


window = tkinter.Tk()
derece0 = StringVar()
derece1 = StringVar()
derece0.set("0")
derece1.set("0")
window.title("Test")
l0 = Label(window, textvariable=derece0)
l1 = Label(window, textvariable=derece1)
l0.pack()
l1.pack()
window.geometry("400x200")


def main2():
    r = RadioSerialConnection(derece0,derece1)
    window.mainloop()

if __name__ == "__main__":
    main2()