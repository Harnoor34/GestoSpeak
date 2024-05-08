from cv2 import VideoCapture, destroyAllWindows
class Webcam():
    def __init__(self):
        self.vc = VideoCapture(0)
    def end_task(self):
        self.vc.release()
        destroyAllWindows()