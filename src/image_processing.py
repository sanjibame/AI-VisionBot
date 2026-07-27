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

    # ===========================================
    # Resize Image
    # ===========================================

    def resize(self, image, width, height):

        """
        Resize image to given width and height.
        """

        return cv2.resize(
            image,
            (width, height)
        )

    # ===========================================
    # Crop Image
    # ===========================================

    def crop(self, image, x, y, width, height):

        """
        Crop image using x, y, width and height.
        """

        return image[
            y:y + height,
            x:x + width
        ]

    # ===========================================
    # Rotate 90° Clockwise
    # ===========================================

    def rotate_clockwise(self, image):

        """
        Rotate image clockwise.
        """

        return cv2.rotate(
            image,
            cv2.ROTATE_90_CLOCKWISE
        )

    # ===========================================
    # Rotate 90° Counter Clockwise
    # ===========================================

    def rotate_counter_clockwise(self, image):

        """
        Rotate image counter clockwise.
        """

        return cv2.rotate(
            image,
            cv2.ROTATE_90_COUNTERCLOCKWISE
        )

    # ===========================================
    # Rotate 180°
    # ===========================================

    def rotate_180(self, image):

        """
        Rotate image by 180 degrees.
        """

        return cv2.rotate(
            image,
            cv2.ROTATE_180
        )

    # ===========================================
    # Horizontal Flip
    # ===========================================

    def flip_horizontal(self, image):

        """
        Flip image horizontally.
        """

        return cv2.flip(
            image,
            1
        )

    # ===========================================
    # Vertical Flip
    # ===========================================

    def flip_vertical(self, image):

        """
        Flip image vertically.
        """

        return cv2.flip(
            image,
            0
        )

    # ===========================================
    # Translate Image
    # ===========================================

    def translate(self, image, x_shift, y_shift):

        """
        Move image in x and y direction.
        """

        rows, cols = image.shape[:2]

        matrix = np.float32([
            [1, 0, x_shift],
            [0, 1, y_shift]
        ])

        return cv2.warpAffine(
            image,
            matrix,
            (cols, rows)
        )

    # ===========================================
    # Scale Image
    # ===========================================

    def scale(self, image, fx=1.0, fy=1.0):

        """
        Scale image.
        """

        return cv2.resize(
            image,
            None,
            fx=fx,
            fy=fy,
            interpolation=cv2.INTER_LINEAR
        )

    # ===========================================
    # Add Border
    # ===========================================

    def add_border(
        self,
        image,
        border=10,
        color=(0, 0, 0)
    ):

        """
        Add constant border around image.
        """

        return cv2.copyMakeBorder(
            image,
            border,
            border,
            border,
            border,
            cv2.BORDER_CONSTANT,
            value=color
        )

    # ===========================================
    # Copy Image
    # ===========================================

    def copy(self, image):

        """
        Return a copy of image.
        """

        return image.copy()

    # ===========================================
    # Get Image Size
    # ===========================================

    def image_size(self, image):

        """
        Return width and height.
        """

        height, width = image.shape[:2]

        return width, height

    # ===========================================
    # Check Grayscale
    # ===========================================

    def is_grayscale(self, image):

        """
        Check whether image is grayscale.
        """

        return len(image.shape) == 2

    # ===========================================
    # Create Kernel
    # ===========================================

    def kernel(self, size=3):

        """
        Create a square kernel.
        """

        return np.ones(
            (size, size),
            np.uint8
        )

    # ===========================================
    # Erosion
    # ===========================================

    def erode(
        self,
        image,
        size=3,
        iterations=1
    ):

        """
        Perform erosion.
        """

        k = self.kernel(size)

        return cv2.erode(
            image,
            k,
            iterations=iterations
        )

    # ===========================================
    # Dilation
    # ===========================================

    def dilate(
        self,
        image,
        size=3,
        iterations=1
    ):

        """
        Perform dilation.
        """

        k = self.kernel(size)

        return cv2.dilate(
            image,
            k,
            iterations=iterations
        )

    # ===========================================
    # Opening
    # ===========================================

    def opening(
        self,
        image,
        size=3
    ):

        """
        Opening removes small noise.
        """

        k = self.kernel(size)

        return cv2.morphologyEx(
            image,
            cv2.MORPH_OPEN,
            k
        )

    # ===========================================
    # Closing
    # ===========================================

    def closing(
        self,
        image,
        size=3
    ):

        """
        Closing fills small holes.
        """

        k = self.kernel(size)

        return cv2.morphologyEx(
            image,
            cv2.MORPH_CLOSE,
            k
        )

    # ===========================================
    # Morphological Gradient
    # ===========================================

    def gradient(
        self,
        image,
        size=3
    ):

        """
        Morphological gradient.
        """

        k = self.kernel(size)

        return cv2.morphologyEx(
            image,
            cv2.MORPH_GRADIENT,
            k
        )

    # ===========================================
    # Top Hat
    # ===========================================

    def top_hat(
        self,
        image,
        size=3
    ):

        """
        Top Hat transformation.
        """

        k = self.kernel(size)

        return cv2.morphologyEx(
            image,
            cv2.MORPH_TOPHAT,
            k
        )

    # ===========================================
    # Black Hat
    # ===========================================

    def black_hat(
        self,
        image,
        size=3
    ):

        """
        Black Hat transformation.
        """

        k = self.kernel(size)

        return cv2.morphologyEx(
            image,
            cv2.MORPH_BLACKHAT,
            k
        )

    # ===========================================
    # Morphological Edge Detection
    # ===========================================

    def morph_edges(
        self,
        image,
        size=3
    ):

        """
        Detect edges using morphology.
        """

        k = self.kernel(size)

        dilated = cv2.dilate(image, k)

        eroded = cv2.erode(image, k)

        return cv2.subtract(
            dilated,
            eroded
        )

    # ===========================================
    # Skeleton Approx

    # ===========================================
    # Draw Rectangle
    # ===========================================

    def draw_rectangle(
        self,
        image,
        x,
        y,
        width,
        height,
        color=(0,255,0),
        thickness=2
    ):

        cv2.rectangle(
            image,
            (x, y),
            (x + width, y + height),
            color,
            thickness
        )

        return image

    # ===========================================
    # Draw Circle
    # ===========================================

    def draw_circle(
        self,
        image,
        x,
        y,
        radius=5,
        color=(0,0,255),
        thickness=-1
    ):

        cv2.circle(
            image,
            (x, y),
            radius,
            color,
            thickness
        )

        return image

    # ===========================================
    # Draw Line
    # ===========================================

    def draw_line(
        self,
        image,
        start,
        end,
        color=(255,0,0),
        thickness=2
    ):

        cv2.line(
            image,
            start,
            end,
            color,
            thickness
        )

        return image

    # ===========================================
    # Draw Arrow
    # ===========================================

    def draw_arrow(
        self,
        image,
        start,
        end,
        color=(0,255,255),
        thickness=2
    ):

        cv2.arrowedLine(
            image,
            start,
            end,
            color,
            thickness
        )

        return image

    # ===========================================
    # Draw Crosshair
    # ===========================================

    def draw_crosshair(
        self,
        image,
        x,
        y,
        size=15,
        color=(255,255,0)
    ):

        cv2.line(
            image,
            (x-size, y),
            (x+size, y),
            color,
            2
        )

        cv2.line(
            image,
            (x, y-size),
            (x, y+size),
            color,
            2
        )

        return image

    # ===========================================
    # Draw Text
    # ===========================================

    def draw_text(
        self,
        image,
        text,
        x,
        y,
        color=(255,255,255),
        scale=0.7
    ):

        cv2.putText(
            image,
            text,
            (x, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            scale,
            color,
            2
        )

        return image

    # ===========================================
    # Draw Face Center
    # ===========================================

    def draw_face_center(
        self,
        image,
        x,
        y
    ):

        cv2.circle(
            image,
            (x, y),
            6,
            (0,0,255),
            -1
        )

        cv2.putText(
            image,
            "CENTER",
            (x+10, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255,255,255),
            1
        )

        return image

    # ===========================================
    # Draw Robot Direction
    # ===========================================

    def draw_direction(
        self,
        image,
        direction
    ):

        cv2.putText(
            image,
            "Direction : " + direction,
            (20,30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0,255,0),
            2
        )

        return image

    # ===========================================
    # Draw FPS
    # ===========================================

    def draw_fps(
        self,
        image,
        fps
    ):

        cv2.putText(
            image,
            f"FPS : {fps:.2f}",
            (20,60),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255,255,0),
            2
        )

        return image

    # ===========================================
    # Draw Battery
    # ===========================================

    def draw_battery(
        self,
        image,
        level
    ):

        cv2.putText(
            image,
            f"Battery : {level} %",
            (20,90),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0,255,255),
            2
        )

        return image

    # ===========================================
    # Draw Status
    # ===========================================

    def draw_status(
        self,
        image,
        status
    ):

        cv2.putText(
            image,
            status,
            (20,120),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0,255,0),
            2
        )

        return image

    # ===========================================
    # Display Processing Result
    # ===========================================

    def show(self, title, image):

        from google.colab.patches import cv2_imshow

        print(title)

        cv2_imshow(image)
           
