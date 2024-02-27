import cv2 as cv
import numpy as np


def apply_postprocessing(image):
    """
    Apply post-processing techniques to refine the enhanced image.

    Args:
    - image (numpy.ndarray): Enhanced image.

    Returns:
    - postprocessed_image (numpy.ndarray): Post-processed image.
    """
    # Check if image is in BGR color space
    if len(image.shape) != 3 or image.shape[2] != 3:
        print(image.shape)
        print(image[0][0])
        raise ValueError("Input image must be in BGR color space with 3 channels.")

    color_corrected_image = correct_colors(image)
    return color_corrected_image


def correct_colors(image):
    """
    Perform color correction on the input image.

    Args:
    - image (numpy.ndarray): Enhanced image.

    Returns:
    - color_corrected_image (numpy.ndarray): Color-corrected image.
    """
    lab_image = cv.cvtColor(image, cv.COLOR_BGR2LAB)
    l_channel, a_channel, b_channel = cv.split(lab_image)

    clahe = cv.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    clahe_l_channel = clahe.apply(l_channel)

    corrected_lab_image = cv.merge((clahe_l_channel, a_channel, b_channel))
    color_corrected_image = cv.cvtColor(corrected_lab_image, cv.COLOR_LAB2BGR)

    return color_corrected_image
