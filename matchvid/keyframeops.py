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
        cap = cv2.VideoCapture(video_path)
        success, previous_frame = cap.read() # Read the first frame.
        count = 0
        while success:
            success, current_frame = cap.read()
            if success:
                diff = cv2.absdiff(current_frame, previous_frame)
                non_zero_count = np.count_nonzero(diff)
                if non_zero_count > p_frame_thresh:
                    # Convert images to 8-Bit grayscale
                    image = cv2.cvtColor(previous_frame, cv2.COLOR_BGR2GRAY)
                    keyframe_list.append(image)
                previous_frame = current_frame
                count += 1
        return keyframe_list
