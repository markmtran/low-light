import cv2 as cv
import numpy as np


def apply_filters(image):
    """
    Apply various filters to enhance the input image.

    Args:
    - image (numpy.ndarray): Input image.

    Returns:
    - filtered_image (numpy.ndarray): Filtered image.
    """
    # Contrast Enhancement
    # contrast_enhanced = cv.equalizeHist(image)

    # Sharpening
    blurred = cv.GaussianBlur(image, (0, 0), 3)
    # laplacian = cv.Laplacian(blurred, cv.CV_64F)
    # filtered_image = np.uint8(np.abs(laplacian))
    sharpened = cv.addWeighted(image, 1.5, blurred, -0.5, 0)

    # Brightness Adjustment
    brightness_adjusted = cv.convertScaleAbs(sharpened, alpha=1.0, beta=0.0)

    # Exposure Compensation
    exposure_compensated = np.uint8(cv.pow(brightness_adjusted / 255.0, 1.0) * 255)
    return exposure_compensated
