import cv2

#This file captures the video feed from the website its being streams to which is 192.168.40.25:5000/video

class RemoteCamera:
    def __init__(self, Ip):
        self.url = Ip
        self.cap = cv2.VideoCapture(self.url)


    def get_frame(self):
        success, frame = self.cap.read()

        if success:
            return frame

        return None


    def release(self):
        self.cap.release()