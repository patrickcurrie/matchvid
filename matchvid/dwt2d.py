import numpy
import pywt

class DWT2D(object):

    def __init__(self, keyframe_list, wavelet_filter):
        self.keyframe_list = keyframe_list
        self.filter = wavelet_filter
        self.approx_coefficient_list = None
        for keyframe in keyframe_list:
            '''
            Find approximation coefficients
            Record coefficient as (coefficient, location) tuples
            Add new tuple to self.approx_coefficient_list
            '''
        '''
        Select n most significant coefficients, drop the rest from the approx_coefficient_list
        '''

    def compare(self, other_dwt2d, threshold):
        '''
        Compare this instance of DWT2D to the supplies instance using the given threshold
        Record time of matching frames in other_dwt2d, add to list
        Return list of matching frame times
        '''
