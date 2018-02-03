#########
matchvid
#########

matchvid is a command-line tool for detecting matching keyframes across distinct videos, powered by two-dimensional discrete wavelet transform.

*************
Abstract
*************

With the advent of convolutional neural networks (CNNs) and their acceptance as the state-of-the-art approach to most image processing problems, research in the applications of wavelet transform has been increasingly restricted to file compression. The goal of this project is to demonstrate that the potential of wavelet transform in media processing has yet to be realized, shed light on problems where utilizing wavelet transform makes more sense than CNNs, and encourage additional research by experts in the field of signal processing.

The motivation underlying this project was to explore the applications of two-dimensional discrete wavelet transform in video processing and identify specific applications in this domain where this approach excels. These applications are in effect matching problems; identifying exact/nearly-exact matches among compared images.

*************
Introduction
*************

The technical objective of this project was to develop a command-line tool for detecting matching keyframes across distinct videos, powered by two-dimensional discrete wavelet transform. My approach differentiates itself from other image processing applications of two-dimensional discrete wavelet transform by using the transform to create a holistic image signature that is comparable to others of the same kind, instead of feature extraction (CNNs are a much better option for such a task). This approach allows my project to leverage the most significant advantages wavelet transform has over CNNs in the context of matching problems.

matchvid demonstrates that the potential applications of two-dimensional discrete wavelet transform in image processing have yet to be fully realized and extend beyond file compression. It shows how the the success of wavelet transform in both file compression and matching problems can be leveraged in conjunction to solve current problems. As a first-iteration proof of concept however there are a number of improvements that have yet to be made. The most significant is utilizing dual-tree complex wavelet transform for signature generation. Dual-tree complex wavelet transform is a relatively new enhancement of the two-dimensional discrete wavelet transform. The dual-tree complex wavelet transform is nearly shift invariant and is implemented as two separate two-channel filter banks. This allows for a redundancy factor substantially lower than two-dimensional discrete wavelet transform, resulting in both a sparser and more accurate compression (in terms of signal-to-noise ratio). It is also more computationally efficient than my current implementation, and offers the ability to generate more compact and accurate video signatures. Unfortunately, PyWavelets is not capable of dual-tree complex wavelet transforms, so this will have to be manually implemented in the next iteration of the project.

*************
Run matchvid Without Installation
*************

It is suggested that at this stage you run the project without installing it.

In order to run the project, openCV2 must be installed on your system and configured for Python3 bindings. Symlink the system cv2.so into the matchvid/lib/python3.6/ directory.
.. highlight:: bash
  ln -s /usr/local/lib/python3.5/site-packages/cv2.so cv2.so

Activate the virtual environment.
.. highlight:: bash
  . bin/activate

Install numpy in this virtual environment.
.. highlight:: bash
  pip install numpy

Install PyWavelets in this virtual environment.
.. highlight:: bash
  pip install PyWavelets

A runner script, matchvid-runner.py, is included that will allow you to run the project without installing it.

*************
Installation
*************

Will eventually be published to PyPi.

The project is still in a prototype phase, so I would advise against installing it to your system as improvements are ongoing. However if you still wish to install it, you can do so by cloning a local copy of the project and then installing it to your system with pip.

*************
Usage
*************

The following details how the project can be run with the runner script in the activated virtual environment (without a system install).

.. code-block::

  usage: python3 ./matchvid_runner.py [-h] [--start START] [--end END]
                            [--keyframe-threshold KEYFRAME_THRESHOLD]
                            [--filter FILTER] [--num-coeff NUM_COEFF]
                            [--match-threshold MATCH_THRESHOLD]
                            videos [videos ...]

  positional arguments:
    videos                First video is matched against other videos provided.

  optional arguments:
    -h, --help            show this help message and exit
    --start START         Start time of primary video to match against in
                          seconds.
    --end END             End time of primary video to match against in seconds.
    --keyframe-threshold KEYFRAME_THRESHOLD
                          Default value is 300000. Image arrays of adjacent
                          frames are subtracted to create new array of
                          subtraction results. Lots of zeros means frames are
                          too similar to be keyframes. Threshold is number of
                          nonzero elements that need to be present to be for the
                          preceding frame to be considered a keyframe.
    --filter FILTER       Wavelet filter used to decompose videos into
                          signatures.
    --num-coeff NUM_COEFF
                          Default value is 128. The n-most significant
                          coefficients that represent a decomposed frame.
                          Minimum value is 1 and maximum is 262144. Must be
                          greater than or equal to --match-threshold.
    --match-threshold MATCH_THRESHOLD
                          Default value is 64. The number of matching
                          (coefficient, location) instances needed between two
                          compared frames to consider them a match. Minimum
                          value is 1 and maximum is 262144. Must be less than or
                          equal to --num-coeff.

If you decided to install the package to the system, use the matchvid command instead.
