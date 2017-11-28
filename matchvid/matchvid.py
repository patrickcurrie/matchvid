import argparse
import numpy
from .keyframeops import KeyframeOps

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('videos', type = str, nargs='+', help='First video is matched against other videos provided.')
    parser.add_argument('--start', type=int, help='Start time of video in seconds.')
    parser.add_argument('--end', type=int, help='End time of video in seconds.')
    args = parser.parse_args() # need to add interval selection
    primary_keyframe_list = KeyframeOps.get_keyframes(arg.videos[0])
    '''
    Carry out wavelt transform on each frame
    '''
    for video in args.videos[1:]:
        secondary_keyframe_list = KeyframeOps.get_keyframes(video)
        '''
        Carry out wavelet transform on each video
        Compare transfrom between primary and secondary videos
        Record locations of matching frames in time
        '''
    '''
    Print location of matches in time of secondary videos
    '''
