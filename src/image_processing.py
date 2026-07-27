"""
=========================================================
AI VisionBot

image_processing.py

=========================================================

This module performs all image processing operations.

Functions included

✓ Grayscale

✓ RGB Conversion

✓ Blur

✓ Threshold

✓ Edge Detection

✓ Sharpen

✓ Brightness

✓ Contrast

✓ Morphology

✓ Resize

✓ Crop

✓ Rotate

✓ Flip

Author : Your Name

Version : 1.0
"""

import cv2
import numpy as np


class ImageProcessor:

    """
    Image Processing Class
    """

    def __init__(self):

        pass

    # ===========================================
    # Convert to Gray
    # ===========================================

    def gray(self, image):

        return cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY
        )

    # ===========================================
    # BGR → RGB
    # ===========================================

    def rgb(self, image):

        return cv2.cvtColor(
            image,
            cv2.COLOR_BGR2RGB
        )

    # ===========================================
    # RGB → BGR
    # ===========================================

    def bgr(self, image):

        return cv2.cvtColor(
            image,
            cv2.COLOR_RGB2BGR
        )

    # ===========================================
    # Gaussian Blur
    # ===========================================

    def gaussian_blur(
        self,
        image,
        kernel=(5,5)
    ):

        return cv2.GaussianBlur(
            image,
            kernel,
            0
        )

    # ===========================================
    # Median Blur
    # ===========================================

    def median_blur(
        self,
        image,
        kernel=5
    ):

        return cv2.medianBlur(
            image,
            kernel
        )

    # ===========================================
    # Bilateral Filter
    # ===========================================

    def bilateral(
        self,
        image
    ):

        return cv2.bilateralFilter(
            image,
            9,
            75,
            75
        )

    # ===========================================
    # Canny Edge Detection
    # ===========================================

    def edges(
        self,
        image,
        low=50,
        high=150
    ):

        return cv2.Canny(
            image,
            low,
            high
        )

    # ===========================================
    # Binary Threshold
    # ===========================================

    def threshold(
        self,
        image,
        value=127
    ):

        _, output = cv2.threshold(

            image,

            value,

            255,

            cv2.THRESH_BINARY

        )

        return output
