import cv2
from multiprocessing import Queue
from Camera.GstreamerVideoReceiver import GstreamerVideoReceiver
import imutils

def main():
    config0 = f"udpsrc address=192.168.0.20 port=5600 ! application/x-rtp, payload=96 ! rtph264depay ! h264parse ! avdec_h264 ! decodebin ! videoconvert ! video/x-raw,format=(string)BGR ! videoconvert ! appsink"
    config1 = f"udpsrc address=192.168.0.20 port=5604 ! application/x-rtp, payload=96 ! rtph264depay ! h264parse ! avdec_h264 ! decodebin ! videoconvert ! video/x-raw,format=(string)BGR ! videoconvert ! appsink"
    # cam0 = cv2.VideoCapture(config0, cv2.CAP_GSTREAMER)
    # cam1 = cv2.VideoCapture(config1, cv2.CAP_GSTREAMER)
    cam0 = GstreamerVideoReceiver(address="192.168.0.20", port=5600)
    cam1 = GstreamerVideoReceiver(address="192.168.0.20", port=5604)
    stitcher = cv2.createStitcher(True) if imutils.is_cv3() else cv2.Stitcher_create()

    while True:
        # ret, frame0 = cam0.read()
        # ret, frame1 = cam1.read()
        frame0 = cam0.frame()
        frame1 = cam1.frame()
        if frame0 is not None and frame1 is not None:
            # cv2.imshow("frame0", frame0)
            # cv2.imshow("frame1", frame1)
            try:
                (status, stitched) = stitcher.stitch([frame0, frame1])
                if status == 0:
                    cv2.imshow("stitched", stitched)
            except:
                pass

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
#
# import serial
# import tkinter
# from tkinter import Label, StringVar, RAISED
# import threading
# from RadioSerialConnection.RadioSerialConnection import RadioSerialConnection
#
#
# window = tkinter.Tk()
# derece0 = StringVar()
# derece1 = StringVar()
# derece0.set("0")
# derece1.set("0")
# window.title("Test")
# l0 = Label(window, textvariable=derece0)
# l1 = Label(window, textvariable=derece1)
# l0.pack()
# l1.pack()
# window.geometry("400x200")
#
#
# def main2():
#     r = RadioSerialConnection(derece0,derece1)
#     window.mainloop()
#
if __name__ == "__main__":
    main()