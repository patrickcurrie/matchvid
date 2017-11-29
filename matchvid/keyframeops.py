import numpy as np
import cv2

class KeyframeOps(object):

    '''
    The frames location in time must also be recorded
    List should be of (keyfram, timestring) tuples
    '''
    @staticmethod
    def get_keyframes(video_path):
        keyframe_list = []
        p_frame_thresh = 300000 # This may need to be adjusted
        video = cv2.VideoCapture(video_path)
        video_fps = video.get(cv2.CAP_PROP_FPS) # Get the frame rate
        success, previous_frame = video.read() # Read the first frame
        frame_number = 1
        while success:
            success, current_frame = video.read() # -> Returns (boolean, image Array)
            if success:
                diff = cv2.absdiff(current_frame, previous_frame)
                non_zero_count = np.count_nonzero(diff)
                if non_zero_count > p_frame_thresh:
                    # Convert images to 8-Bit grayscale
                    image = cv2.cvtColor(previous_frame, cv2.COLOR_BGR2GRAY)
                    # Appends (keyframe, time of frame in seconds)
                    keyframe_list.append((image, frame_number / video_fps))
                previous_frame = current_frame
                frame_number += 1
        return keyframe_list
