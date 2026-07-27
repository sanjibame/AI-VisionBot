"""
=====================================================
AI VisionBot
camera.py
=====================================================

This module is responsible for

• Uploading images
• Loading images
• Displaying images
• Saving images
• Loading videos
• Image information
• Resizing
• Rotating
• Flipping

Author : Your Name
Version : 1.0
"""

import cv2
import os

from google.colab import files
from google.colab.patches import cv2_imshow


class Camera:

    """
    Camera Utility Class
    """

    def __init__(self):

        self.image = None

        self.video = None

    # ---------------------------------------------

    def upload_image(self):

        """
        Upload image from Google Colab
        """

        uploaded = files.upload()

        filename = list(uploaded.keys())[0]

        return filename

    # ---------------------------------------------

    def load_image(self, filename):

        """
        Load image
        """

        self.image = cv2.imread(filename)

        if self.image is None:

            raise FileNotFoundError(
                f"Unable to load {filename}"
            )

        return self.image

    # ---------------------------------------------

    def show_image(self, image=None):

        """
        Display image
        """

        if image is None:

            image = self.image

        cv2_imshow(image)

    # ---------------------------------------------

    def save_image(self, image, filename):

        """
        Save image
        """

        cv2.imwrite(filename, image)

        print(f"Image saved as {filename}")

    # ---------------------------------------------

    def image_info(self, image=None):

        """
        Display image properties
        """

        if image is None:

            image = self.image

        height, width = image.shape[:2]

        channels = 1

        if len(image.shape) == 3:

            channels = image.shape[2]

        print("-" * 35)

        print("Image Information")

        print("-" * 35)

        print("Width    :", width)

        print("Height   :", height)

        print("Channels :", channels)

        print("Shape    :", image.shape)

    # ---------------------------------------------

    def resize(self, image, width, height):

        """
        Resize image
        """

        return cv2.resize(

            image,

            (width, height)

        )

    # ---------------------------------------------

    def rotate_clockwise(self, image):

        """
        Rotate 90 degrees clockwise
        """

        return cv2.rotate(

            image,

            cv2.ROTATE_90_CLOCKWISE

        )

    # ---------------------------------------------

    def rotate_counter_clockwise(self, image):

        """
        Rotate 90 degrees anti-clockwise
        """

        return cv2.rotate(

            image,

            cv2.ROTATE_90_COUNTERCLOCKWISE

        )

    # ---------------------------------------------

    def flip_horizontal(self, image):

        """
        Horizontal Flip
        """

        return cv2.flip(

            image,

            1

        )

    # ---------------------------------------------

    def flip_vertical(self, image):

        """
        Vertical Flip
        """

        return cv2.flip(

            image,

            0

        )

    # ---------------------------------------------

    def open_video(self, filename):

        """
        Open video
        """

        self.video = cv2.VideoCapture(filename)

        return self.video

    # ---------------------------------------------

    def release_video(self):

        """
        Release video
        """

        if self.video is not None:

            self.video.release()

    # ---------------------------------------------

    def file_exists(self, filename):

        """
        Check file exists
        """

        return os.path.exists(filename)

    # ---------------------------------------------

    def file_size(self, filename):

        """
        File size in bytes
        """

        if self.file_exists(filename):

            return os.path.getsize(filename)

        return 0

    # ---------------------------------------------

    def image_dimensions(self, image):

        """
        Return width and height
        """

        height, width = image.shape[:2]

        return width, height
