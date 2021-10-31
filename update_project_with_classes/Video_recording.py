import cv2
import numpy as np
import pyautogui

class VideoScript:
    def __init__(self):
        self.SCREEN_SIZE = (1920, 1080) # screen_resolution
        self.fourcc = cv2.VideoWriter_fourcc(*"XVID") # the codec
        self.out = cv2.VideoWriter("output.avi", self.fourcc, 17, self.SCREEN_SIZE) # create the video write object
        self.starting_video_recording()

    #this function starts to recording
    def starting_video_recording(self):
        print("Start video recording")
        count_seconds = 0
        while True:
            img = pyautogui.screenshot() # make a screenshot
            frame = np.array(img) # convert these pixels to a proper numpy array to work with OpenCV
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # convert colors from BGR to RGB
            self.out.write(frame) # write the frame
            count_seconds += 1
            if count_seconds % 17 == 0:
                print("Video recording...")
            if count_seconds == 170: # 2400
                print("Finish Video recording!")
                break
        self.end_Recording()

    #this function ends the recording successfully
    def end_Recording(self):
        cv2.destroyAllWindows()
        self.out.release()
