import pyrealsense2 as rs
import numpy as np
import cv2
from threading import Thread

class VideoGetHD:
    """
    Class that continuously gets frames from a RealSense sensor
    with a dedicated thread.
    """

    def __init__(self):
        # Configure depth and color streams
        self.pipeline = rs.pipeline()
        self.config = rs.config()
        
        # Enable both depth and color streams
        self.config.enable_stream(rs.stream.depth, 1280, 720, rs.format.z16, 30)
        self.config.enable_stream(rs.stream.color, 1280, 720, rs.format.bgr8, 30)

        # Start streaming
        self.pipeline.start(self.config)

        # Initialize frame variables
        self.color_frame = None
        self.depth_frame = None

        self.stopped = False

    def start(self):
        Thread(target=self.get, args=()).start()
        return self

    def get(self):
        while not self.stopped:
            # Wait for a coherent pair of frames: depth and color
            frames = self.pipeline.wait_for_frames()
            depth_frame = frames.get_depth_frame()
            color_frame = frames.get_color_frame()
            if not depth_frame or not color_frame:
                continue
            
            # Convert images to numpy arrays
            self.depth_frame = np.asanyarray(depth_frame.get_data())
            self.color_frame = np.asanyarray(color_frame.get_data())

    def stop(self):
        self.stopped = True
        self.pipeline.stop()
    
    def frame_available(self):
        return self.color_frame is not None and self.depth_frame is not None
