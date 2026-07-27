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

    # ===========================================
    # Adaptive Threshold
    # ===========================================

    def adaptive_threshold(self, image):

        return cv2.adaptiveThreshold(
            image,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            11,
            2
        )

    # ===========================================
    # Otsu Threshold
    # ===========================================

    def otsu_threshold(self, image):

        _, output = cv2.threshold(
            image,
            0,
            255,
            cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )

        return output

    # ===========================================
    # Histogram Equalization
    # ===========================================

    def equalize(self, image):

        return cv2.equalizeHist(image)

    # ===========================================
    # CLAHE
    # ===========================================

    def clahe(self, image):

        clahe = cv2.createCLAHE(
            clipLimit=2.0,
            tileGridSize=(8,8)
        )

        return clahe.apply(image)

    # ===========================================
    # Brightness
    # ===========================================

    def brightness(self, image, value=30):

        return cv2.convertScaleAbs(
            image,
            alpha=1,
            beta=value
        )

    # ===========================================
    # Contrast
    # ===========================================

    def contrast(self, image, alpha=1.5):

        return cv2.convertScaleAbs(
            image,
            alpha=alpha,
            beta=0
        )

    # ===========================================
    # Gamma Correction
    # ===========================================

    def gamma(self, image, gamma=1.2):

        inverse = 1.0 / gamma

        table = np.array([
            ((i / 255.0) ** inverse) * 255
            for i in np.arange(256)
        ]).astype("uint8")

        return cv2.LUT(image, table)

    # ===========================================
    # Sharpen Image
    # ===========================================

    def sharpen(self, image):

        kernel = np.array([
            [0,-1,0],
            [-1,5,-1],
            [0,-1,0]
        ])

        return cv2.filter2D(
            image,
            -1,
            kernel
        )

    # ===========================================
    # Noise Reduction
    # ===========================================

    def denoise(self, image):

        return cv2.fastNlMeansDenoisingColored(
            image,
            None,
            10,
            10,
            7,
            21
        )
