from VideoReceiver.RaspberryVideoReceiver import RaspberryVideoReceiver
import cv2


def main():
    # send_queue = Queue()
    # get_queue = Queue()
    camera_receivers = [RaspberryVideoReceiver(address=f"192.168.0.{47 + i}", port=5600) for i in range(2)]
    # stitcher = cv2.createStitcher(True) if imutils.is_cv3() else cv2.Stitcher_create()

    # stitcher_process = StitcherProcess(queue=queue, out_queue=out_queue)
    # stitcher_process.daemon = True
    # stitcher_process.start()

    while True:

        frames = [receiver.frame() for receiver in camera_receivers]
        # if not frames.__contains__(None):
        #     frames = [receiver.frame() for receiver in camera_receivers]
        #     [cv2.imshow(f"frame{idx}", frame) for idx, frame in enumerate(frames)]
        print(frames)
        # [cv2.imshow(f"frame{idx}", frame) for idx, frame in enumerate(frames) if frame is not None]
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