import os
import cv2 as cv
import numpy as np


def contrast_enhancement_laplacian_of_gaussian(
    image, kernel_size=(5, 5), sigma=1.0, alpha=1.5
):
    smoothed_image = cv.GaussianBlur(image, kernel_size, sigma)
    laplacian = cv.Laplacian(smoothed_image, cv.CV_64F)
    enhanced_image = image + alpha * laplacian
    enhanced_image = np.clip(enhanced_image, 0, 255).astype(np.uint8)

    return enhanced_image


input_image = cv.imread("../data/originals/zion.jpg", cv.IMREAD_GRAYSCALE)
resized = cv.resize(input_image, None, fx=0.2, fy=0.2, interpolation=cv.INTER_LINEAR)
enhanced = contrast_enhancement_laplacian_of_gaussian(resized)

# cv.imshow("Original Image", resized)
# cv.imshow("Enhanced Image", enhanced)
# cv.waitKey()
# cv.destroyAllWindows()
filename = os.path.basename("../data/originals/zion.jpg")
output_file = os.path.join("../data/results/log_" + filename)
cv.imwrite(output_file, enhanced)
