"""
Description: This file follows the LearnOpenCV tutorial listed in Project 2.
Author: Mark Tran
Date: February 2024
"""

import cv2 as cv
import numpy as np
import os

def generate_kernel(shape, type=np.float32):
  return np.ones(shape, type)


def apply_custom_kernel(img_path, kernel):
  image = cv.imread(img_path)
  result = cv.filter2D(src=image, ddepth=-1, kernel=kernel)
  cv.imshow('Original', image)
  cv.imshow('Result', result)

  cv.waitKey()
  cv.imwrite('results/custom_' + os.path.basename(img_path), result)
  cv.destroyAllWindows()


def apply_opencv_blur(img_path, kernel_shape):
  image = cv.imread(img_path)
  blurred = cv.blur(src=image, ksize=kernel_shape)
  cv.imshow('Original', image)
  cv.imshow('Result', blurred)

  cv.waitKey()
  cv.imwrite('results/cv_blurred_' + os.path.basename(img_path), blurred)
  cv.destroyAllWindows()


def apply_bilateral_filter(img_path):
  image = cv.imread(img_path)
  bilateral_filter = cv.bilateralFilter(image, d=9, sigmaColor=75, sigmaSpace=75)
  cv.imshow('Original', image)
  cv.imshow('Bilateral Filtering', bilateral_filter)

  cv.waitKey()
  cv.imwrite('results/bilateral_' + os.path.basename(img_path), bilateral_filter)
  cv.destroyAllWindows()


def main():
  img_path = "originals/wood.jpg"

  kernel_shape = (5, 5)
  # kernel = generate_kernel(kernel_shape) / 25
  kernel3 = np.array([[0, -1,  0],
                   [-1,  5, -1],
                    [0, -1,  0]])

  # apply_custom_kernel(img_path, kernel3)
  apply_bilateral_filter(img_path)


if __name__ == "__main__":
  main()
