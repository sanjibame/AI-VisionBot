"""
=========================================================
AI VisionBot

utils.py

Utility Functions

Author : Your Name
Version : 1.0
=========================================================
"""

import cv2
import time
import math


# ==========================================
# Current Time
# ==========================================

def current_time():

    """
    Return current time.
    """

    return time.time()


# ==========================================
# Calculate FPS
# ==========================================

def calculate_fps(previous_time):

    """
    Calculate Frames Per Second.
    """

    current = time.time()

    fps = 1 / (current - previous_time)

    return fps, current


# ==========================================
# Euclidean Distance
# ==========================================

def distance(x1, y1, x2, y2):

    """
    Distance between two points.
    """

    return math.sqrt(

        (x2 - x1) ** 2 +

        (y2 - y1) ** 2

    )


# ==========================================
# Draw Robot
# ==========================================

def draw_robot(

    frame,

    x,

    y,

    radius=15,

    color=(255,0,0)

):

    cv2.circle(

        frame,

        (int(x), int(y)),

        radius,

        color,

        -1

    )

    return frame


# ==========================================
# Draw Target
# ==========================================

def draw_target(

    frame,

    x,

    y,

    color=(0,255,255)

):

    cv2.circle(

        frame,

        (int(x), int(y)),

        8,

        color,

        2

    )

    return frame


# ==========================================
# Draw Text
# ==========================================

def draw_text(

    frame,

    text,

    x,

    y,

    color=(255,255,255),

    scale=0.6

):

    cv2.putText(

        frame,

        text,

        (x, y),

        cv2.FONT_HERSHEY_SIMPLEX,

        scale,

        color,

        2

    )

    return frame


# ==========================================
# Draw Line
# ==========================================

def draw_line(

    frame,

    x1,

    y1,

    x2,

    y2,

    color=(0,255,0)

):

    cv2.line(

        frame,

        (x1,y1),

        (x2,y2),

        color,

        2

    )

    return frame
  # ==========================================
# Draw Rectangle
# ==========================================

def draw_rectangle(

    frame,

    x,

    y,

    w,

    h,

    color=(0,255,0),

    thickness=2

):

    cv2.rectangle(

        frame,

        (x, y),

        (x + w, y + h),

        color,

        thickness

    )

    return frame


# ==========================================
# Draw Center Point
# ==========================================

def draw_center(

    frame,

    x,

    y,

    color=(0,0,255)

):

    cv2.circle(

        frame,

        (int(x), int(y)),

        4,

        color,

        -1

    )

    return frame


# ==========================================
# Draw Circle
# ==========================================

def draw_circle(

    frame,

    x,

    y,

    radius,

    color=(255,255,0),

    thickness=2

):

    cv2.circle(

        frame,

        (int(x), int(y)),

        radius,

        color,

        thickness

    )

    return frame


# ==========================================
# Keep Value Within Range
# ==========================================

def clamp(

    value,

    minimum,

    maximum

):

    """
    Limit a value between minimum and maximum.
    """

    return max(

        minimum,

        min(value, maximum)

    )


# ==========================================
# Check Screen Boundary
# ==========================================

def inside_screen(

    x,

    y,

    width,

    height

):

    """
    Check whether point is inside screen.
    """

    return (

        0 <= x < width and

        0 <= y < height

    )


# ==========================================
# Center of Rectangle
# ==========================================

def rectangle_center(

    x,

    y,

    w,

    h

):

    """
    Return rectangle center.
    """

    return (

        x + w // 2,

        y + h // 2

    )


# ==========================================
# Resize Frame
# ==========================================

def resize_frame(

    frame,

    width,

    height

):

    """
    Resize image frame.
    """

    return cv2.resize(

        frame,

        (width, height)

    )


# ==========================================
# Flip Frame
# ==========================================

def flip_frame(

    frame

):

    """
    Flip webcam frame horizontally.
    """

    return cv2.flip(

        frame,

        1

    )


# ==========================================
# Convert To Gray
# ==========================================

def gray(

    frame

):

    """
    Convert frame to grayscale.
    """

    return cv2.cvtColor(

        frame,

        cv2.COLOR_BGR2GRAY

    )


# ==========================================
# Put Label
# ==========================================

def put_label(

    frame,

    text,

    position,

    color=(255,255,255)

):

    cv2.putText(

        frame,

        text,

        position,

        cv2.FONT_HERSHEY_SIMPLEX,

        0.5,

        color,

        2

    )

    return frame
  import random
from datetime import datetime


# ==========================================
# Save Image
# ==========================================

def save_image(frame, filename):

    """
    Save image to disk.
    """

    cv2.imwrite(filename, frame)

    return filename


# ==========================================
# Load Image
# ==========================================

def load_image(filename):

    """
    Load image from disk.
    """

    return cv2.imread(filename)


# ==========================================
# Timestamp
# ==========================================

def timestamp():

    """
    Return current timestamp.
    """

    return datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


# ==========================================
# Log Message
# ==========================================

def log(message):

    """
    Print timestamped log.
    """

    print(

        f"[{timestamp()}] {message}"

    )


# ==========================================
# Random Color
# ==========================================

def random_color():

    """
    Generate a random BGR color.
    """

    return (

        random.randint(0,255),

        random.randint(0,255),

        random.randint(0,255)

    )


# ==========================================
# Blank Frame
# ==========================================

def blank_frame(

    width,

    height,

    color=(0,0,0)

):

    """
    Create a blank image.
    """

    import numpy as np

    frame = np.zeros(

        (height, width, 3),

        dtype=np.uint8

    )

    frame[:] = color

    return frame


# ==========================================
# Frame Information
# ==========================================

def frame_info(frame):

    """
    Return frame information.
    """

    h, w = frame.shape[:2]

    return {

        "Width": w,

        "Height": h,

        "Channels":

            frame.shape[2]

            if len(frame.shape) == 3

            else 1

    }


# ==========================================
# Print Frame Information
# ==========================================

def print_frame_info(frame):

    info = frame_info(frame)

    print("=" * 40)

    print("FRAME INFORMATION")

    print("=" * 40)

    for key, value in info.items():

        print(f"{key:<10}: {value}")

    print("=" * 40)


# ==========================================
# Utility Summary
# ==========================================

def summary():

    return {

        "Drawing":

            "Available",

        "Logging":

            "Available",

        "Image Save":

            "Available",

        "Image Load":

            "Available",

        "Timestamp":

            timestamp()

    }


# ==========================================
# Print Utility Summary
# ==========================================

def print_summary():

    print("=" * 45)

    print("AI VisionBot Utility Summary")

    print("=" * 45)

    for key, value in summary().items():

        print(f"{key:<15}: {value}")

    print("=" * 45)


# ==========================================
# Utility Self Test
# ==========================================

def test():

    print("Testing Utility Module...\n")

    log("Utility module loaded successfully.")

    print_summary()

    print("\nUtility Test Completed.")
  
