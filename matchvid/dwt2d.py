import numpy as np
import pywt

class DWT2D(object):

    # Carry out wavelet transform on each frame with specified filter
    # Get locations of n-most significant coefficients for each frame
    # [(x_index, y_index, coefficient), ...] -> frame representation
    # Append (frame_representation, frame_time) to self.approx_coeff_list
    # Video signature is self.approx_coeff_list
    # [ ([(x_index, y_index, coefficient), ...], time_in_seconds), ... ]
    # -> video signature
    # Each element of list is a frame representation
    def __init__(self, keyframe_list, wavelet_filter, num_coeff):
        self.keyframe_list = keyframe_list
        self.wavelet_filter = wavelet_filter
        self.approx_coeff_list = []
        for keyframe, time_seconds in keyframe_list:
            coefficients = pywt.dwt2(keyframe, wavelet_filter)
            coeff_approximation, (coeff_horizontal, coeff_vertical, coeff_diagonal) = coefficients
            coeff_significant = self.__get_n_largest_location(coeff_approximation, num_coeff)
            self.approx_coeff_list.append((coeff_significant, time_seconds))


    # Returns representation of the n most significant coefficients for a frame
    #
    # Frame representation is coeff_significat
    # [(x_index, y_index, coefficient), ...] -> frame representation
    #
    # Sort coeff_significant by most significant coefficients
    # Return sorted coeff_significat
    def __get_n_largest_location(self, array, num_coeff):
        coeff_significant = []
        # Convert it into a 1D array
        flattened_array = array.flatten()
        # Find the indices in the 1D array
        indicies = flattened_array.argsort()[-num_coeff:]
        # Convert flattened indicies to original dimensions
        x_index, y_index = np.unravel_index(indicies, array.shape)
        indicies = zip(x_index, y_index)
        for x, y, in indicies:
            coeff_significant.append((x, y, array[x][y]))
        return list(reversed(coeff_significant)) # Largest to smallest coeff

    # Compares the the signatures of this instance and given DWT2D object
    # For each primary_frame:
    #   For each secondary_frame:
    #       If location-coefficient matches >= match_threshold
    #           Append frame-match representation to match_list
    #
    # [(x, y, (prime_coeff, prime_time), (second_coeff, second_time)), ...]
    # -> frame-match representation
    #
    # [frame_match_representation, ...] -> match_list
    #
    # Return match_list
    def compare(self, other_dwt2d, match_threshold):
        match_list = []
        for primary_frame in self.approx_coeff_list:
            for secondary_frame in other_dwt2d.approx_coeff_list:
                frame_matches = [(primary_x, primary_y, (primary_coeff, primary_frame[1]), (secondary_coeff, secondary_frame[1])) for (primary_x, primary_y, primary_coeff) in primary_frame[0] for (secondary_x, secondary_y, secondary_coeff) in secondary_frame[0] if ((primary_x==secondary_x) and (primary_y==secondary_y) and (primary_coeff==secondary_coeff))]
                if len(frame_matches) != 0 and len(frame_matches) >= match_threshold:
                    match_list.append(frame_matches)
                    print("\n\n")
                    print(frame_matches)
        return match_list
