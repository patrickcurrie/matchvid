import argparse
import numpy
from .keyframeops import KeyframeOps
from .dwt2d import DWT2D

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('videos', type = str, nargs='+', help="First video is matched against other videos provided.")
    parser.add_argument('--start', type=int, help="Start time of primary video to match against in seconds.")
    parser.add_argument('--end', type=int, help="End time of primary video to match against in seconds.")
    parser.add_argument('--keyframe-threshold', type=int, default=300000, help="Default value is 300000. Image arrays of adjacent frames are subtracted to create new array of subtraction results. Lots of zeros means frames are too similar to be keyframes. Threshold is number of nonzero elements that need to be present to be for the preceding frame to be considered a keyframe.")
    parser.add_argument('--filter', type=str, help="Wavelet filter used to decompose videos into signatures.") # 'bior1.3'
    parser.add_argument('--num-coeff', type=int, default=128, help="Default value is 128. The n-most significant coefficients that represent a decomposed frame. Minimum value is 1 and maximum is 262144. Must be greater than or equal to --match-threshold.")
    parser.add_argument('--match-threshold', type=int, default=64, help="Default value is 64. The number of matching (coefficient, location) instances needed between two compared frames to consider them a match. Minimum value is 1 and maximum is 262144. Must be less than or equal to --num-coeff.")
    args = parser.parse_args()
    if args.match_threshold > args.num_coeff:
        parser.error("--match-threshold must be less than or equal to --num-coeff.")
    # List of (keyframe, time in seconds) tuples
    primary_keyframe_list = KeyframeOps.get_keyframes(args.videos[0], nonzero_threshold=args.keyframe_threshold, start_time=args.start, end_time=args.end)
    # Carry out wavelet transform on each frame
    primary_signature = DWT2D(primary_keyframe_list, args.filter, args.num_coeff)
    # Decompose each secondary video into a signature
    # Compare each secondary video signature to the primary vido signature
    for video in args.videos[1:]:
        secondary_keyframe_list = KeyframeOps.get_keyframes(video, nonzero_threshold=args.keyframe_threshold)
        secondary_signature = DWT2D(secondary_keyframe_list, args.filter, args.num_coeff)
        # match_list holds frame matches
        match_list = primary_signature.compare(secondary_signature, args.match_threshold)
