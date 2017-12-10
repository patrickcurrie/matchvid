import numpy as np
import cv2
import math

class KeyframeOps(object):

    # Returns list of keyframes in the given video
    #
    # List of keyframes is keyframe_list
    #
    # [(image_array, time_seconds), (image_array, time_seconds), ... ]
    # -> List of keyframes representation
    #
    # Return keyframe_list
    @staticmethod
    def get_keyframes(video_path, nonzero_threshold, start_time=None, end_time=None):
        keyframe_list = []
        frame_number = None
        video = cv2.VideoCapture(video_path)
        # Get the frame rate
        video_fps = video.get(cv2.CAP_PROP_FPS)
        # Set first and last frames to be read
        if start_time:
            start_frame = math.floor(video_fps * start_time)
            video.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
            frame_number = start_frame
        else:
            frame_number = 1
        if end_time:
            end_frame = math.floor(video_fps * end_time)
        else:
            end_frame = video.get(cv2.CAP_PROP_FRAME_COUNT)
        # Read the first frame
        success, previous_frame = video.read()
        # Read each frame
        # Stop upon failure or last frame read
        while success and frame_number <= end_frame:
            # Returns (boolean, image Array)
            success, current_frame = video.read()
            if success:
                # Matrix subtraction
                difference_array = cv2.absdiff(current_frame, previous_frame)
                # Count nonzero elements
                nonzero_count = np.count_nonzero(difference_array)
                if nonzero_count > nonzero_threshold:
                    # Convert images to 8-Bit grayscale
                    image = cv2.cvtColor(previous_frame, cv2.COLOR_BGR2GRAY)
                    # Appends (keyframe, time of frame in seconds)
                    keyframe_list.append((image, frame_number / video_fps))
                previous_frame = current_frame
                frame_number += 1
        return keyframe_list
