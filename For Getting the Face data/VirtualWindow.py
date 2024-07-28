import cv2
import time
import asyncio
import websockets
import json
from VideoGetHD import VideoGetHD
from FaceTracker import FaceTracker
from threading import Thread

# USER MUST UPDATE THE FOLLOWING
# Screen specifications, camera location, units are inches
cameraOffset = 4.75  # from center of screen, up is positive, inches. Program assumes camera is centered over or under the screen, with positive value being over.
screenWidth = 20.4
screenHeight = 12.6
screenResolution = (1920, 1200)

scrnW = screenWidth / 2
scrnH = screenHeight / 2
pixperinch = screenResolution[0] / screenWidth
i = screenResolution[0] / 2
j = screenResolution[1] / 2

distance = 45  # arbitrary, quickly overwritten with real values
distance2 = distance
distance3 = distance2
first = True

headxyz = None
frame_available = False
video_getter = None
face_tracker = None


async def threadVirtualWindow(websocket, path):  # Source is which camera on your system you will be using, and for most users will be '0'
    global headxyz, frame_available, video_getter, face_tracker

    while not frame_available:
        await asyncio.sleep(0.01)

    while True:
        await asyncio.sleep(0.001)  # ESSENTIAL DELAY FOR PROGRAM TO WORK
        face_tracker.frame = video_getter.color_frame
        headxyz = face_tracker.track()

        data = json.dumps({'headxyz': headxyz})
        await websocket.send(data)


def start_video_and_tracking():
    global headxyz, frame_available, video_getter, face_tracker

    video_getter = VideoGetHD().start()
    while not video_getter.frame_available():
        time.sleep(0.01)

    face_tracker = FaceTracker(video_getter.color_frame).start()
    frame_available = True


def main():
    global headxyz, frame_available, video_getter, face_tracker

    headxyz = None
    frame_available = False
    video_getter = None
    face_tracker = None

    video_thread = Thread(target=start_video_and_tracking)
    video_thread.start()

    start_server = websockets.serve(threadVirtualWindow, 'localhost', 8765)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    main()
