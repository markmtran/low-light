import cv2 as cv
import numpy as np


def preprocess_image(image):
    """
    Pre-process the input image before enhancement.

    Args:
    - image (numpy.ndarray): Input image.

    Returns:
    - preprocessed_image (numpy.ndarray): Pre-processed image.
    """
    # Normalize
    normalized_image = image.astype(np.float32)
    normalized_image /= 255.0

    # Reduce noise via bilateral filtering
    denoised_image = cv.bilateralFilter(
        normalized_image, d=9, sigmaColor=75, sigmaSpace=75
    )

    grayscale_image = (cv.cvtColor(denoised_image, cv.COLOR_BGR2GRAY) * 255).astype(
        np.uint8
    )

    equalized_image = cv.equalizeHist(grayscale_image)
    equalized_3_channels = cv.cvtColor(equalized_image, cv.COLOR_GRAY2BGR)
    return equalized_3_channels
