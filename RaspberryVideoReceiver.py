import time
import cv2
import numpy as np
import imutils

import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject


GObject.threads_init()

class RaspberryVideoReceiver:
    cam_num = 0

    def __init__(self, address, port=5600):
        Gst.init(None)
        self.address = address
        self.port = port
        self._frame = None

        self.video_source = 'udpsrc address={} port={}'.format(self.address, self.port)
        print(self.video_source)
        self.video_codec = '! application/x-rtp, payload=96 ! rtph264depay ! h264parse ! avdec_h264'

        self.video_decode = \
            '! decodebin ! videoconvert ! video/x-raw,format=(string)BGR ! videoconvert'

        self.video_sink_conf = \
            '! appsink emit-signals=true max-buffers=2 drop=true'

        self.video_pipe = None
        self.video_sink = None

        self.run_gst()

    def start_gst(self, config=None):
        if not config:
            config = \
                [
                    'videotestsrc ! decodebin',
                    '! videoconvert ! video/x-raw,format=(string)BGR ! videoconvert',
                    '! appsink'
                ]

        # config = \
        #     [
        #         'videotestsrc ! decodebin',
        #         '! videoconvert ! video/x-raw,format=(string)BGR ! videoconvert',
        #         '! appsink emit-signals=true'
        #     ]
        command = ' '.join(config)
        print(command)
        self.video_pipe = Gst.parse_launch(command)
        self.video_pipe.set_state(Gst.State.PLAYING)
        self.video_sink = self.video_pipe.get_by_name('appsink{}'.format(RaspberryVideoReceiver.cam_num))
        RaspberryVideoReceiver.cam_num += 1
        print("video sink: ", self.video_sink)

    @staticmethod
    def gst_to_opencv(sample):
        buf = sample.get_buffer()
        caps = sample.get_caps()
        array = np.ndarray(
            (
                caps.get_structure(0).get_value('height'),
                caps.get_structure(0).get_value('width'),
                3
            ),
            buffer=buf.extract_dup(0, buf.get_size()), dtype=np.uint8)
        return array

    def frame(self):
        return self._frame

    def frame_available(self):
        return type(self._frame) != type(None)

    def run_gst(self):
        self.start_gst(
            [
                self.video_source,
                self.video_codec,
                self.video_decode,
                self.video_sink_conf
            ])

        self.video_sink.connect('new-sample', self.callback)

    def callback(self, sink):
        sample = sink.emit('pull-sample')
        new_frame = self.gst_to_opencv(sample)
        self._frame = new_frame

        return Gst.FlowReturn.OK



