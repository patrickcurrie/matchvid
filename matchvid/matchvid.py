import argparse
import numpy
from .keyframeops import KeyframeOps
from .dwt2d import DWT2D

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('videos', type = str, nargs='+', help='First video is matched against other videos provided.')
    parser.add_argument('--start', type=int, help='Start time of video in seconds.')
    parser.add_argument('--end', type=int, help='End time of video in seconds.')
    args = parser.parse_args() # need to add interval selection
    # List of (keyframe, time in seconds) tuples
    primary_keyframe_list = KeyframeOps.get_keyframes(args.videos[0])
    '''
    Carry out wavelet transform on each frame
    '''
    primary_signature = DWT2D(primary_keyframe_list, 'bior1.3')
    #print(primary_signature.approx_coefficient_list[10])
    for video in args.videos[1:]:
        secondary_keyframe_list = KeyframeOps.get_keyframes(video)
        secondary_signature = DWT2D(secondary_keyframe_list, 'bior1.3')
        '''
        Carry out wavelet transform on each video
        Compare transfrom between primary and secondary videos
        Record locations of matching frames in time
        '''
        match_list = primary_signature.compare(secondary_signature)
        #print(match_list)
