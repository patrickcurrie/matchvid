import numpy as np
import pywt

class DWT2D(object):

    def __init__(self, keyframe_list, wavelet_filter):
        self.keyframe_list = keyframe_list
        self.wavelet_filter = wavelet_filter
        self.approx_coeff_list = []
        for keyframe, time_seconds in keyframe_list:
            '''
            Find approximation coefficients
            Record coefficient as (coefficient, location) tuples
            Add new tuple to self.approx_coefficient_list
            '''
            coefficients = pywt.dwt2(keyframe, wavelet_filter)
            coeff_approximation, (coeff_horizontal, coeff_vertical, coeff_diagonal) = coefficients
            coeff_significant = self.__get_n_largest_location(coeff_approximation, 128)
            self.approx_coeff_list.append((coeff_significant, time_seconds))

    '''
    Returns a representation of the n most significant coefficients for a frame.
    The is of the form:
        [[(x_index, y_index, coefficient), ...], time_in_seconds]
    '''
    def __get_n_largest_location(self, array, n):
        coeff_significant = []
        # Convert it into a 1D array
        flattened_array = array.flatten()
        # Find the indices in the 1D array
        indicies = flattened_array.argsort()[-n:]
        # Convert flattened indicies to original dimensions
        x_index, y_index = np.unravel_index(indicies, array.shape)
        indicies = zip(x_index, y_index)
        for x, y, in indicies:
            coeff_significant.append((x, y, array[x][y]))
        return list(reversed(coeff_significant)) # Largest to smallest coeff

    def compare(self, other_dwt2d):
        '''
        For each primary_frame:
            For each secondary_frame:
                compare primary_frame_locations[0] to secondary_frame_locations[0]
                if locations match then compare compare coefficients
                if coefficients match add to match_list
        '''
        match_list = []
        for primary_frame in self.approx_coeff_list:
            for secondary_frame in other_dwt2d.approx_coeff_list:
                frame_matches = [(primary_x, primary_y, (primary_coeff, primary_frame[1]), (secondary_coeff, secondary_frame[1])) for (primary_x, primary_y, primary_coeff) in primary_frame[0] for (secondary_x, secondary_y, secondary_coeff) in secondary_frame[0] if ((primary_x==secondary_x) and (primary_y==secondary_y) and (primary_coeff==secondary_coeff))]
                if len(frame_matches) != 0 and len(frame_matches) > 4:
                    match_list.append(frame_matches)
                    print("{}\n", frame_matches)
        return match_list
