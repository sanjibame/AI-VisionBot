"""
=====================================================
AI VisionBot
Configuration File
=====================================================

This file stores all configurable settings used
throughout the project.

Author : Your Name
Version : 1.0
"""

import cv2

# =====================================================
# Project Information
# =====================================================

PROJECT_NAME = "AI VisionBot"

VERSION = "1.0"

AUTHOR = "Your Name"

# =====================================================
# Screen Settings
# =====================================================

SCREEN_WIDTH = 640

SCREEN_HEIGHT = 480

FPS = 30

# =====================================================
# Robot Settings
# =====================================================

ROBOT_START_X = 320

ROBOT_START_Y = 240

ROBOT_SPEED = 5

ROBOT_RADIUS = 20

ROBOT_DIRECTION = "STOP"

# =====================================================
# Face Detection
# =====================================================

FACE_SCALE_FACTOR = 1.3

FACE_MIN_NEIGHBORS = 5

FACE_MIN_SIZE = (30, 30)

CASCADE_PATH = (
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

# =====================================================
# Robot Decision Boundaries
# =====================================================

LEFT_ZONE = 213

CENTER_ZONE = 426

# =====================================================
# Battery
# =====================================================

BATTERY_MAX = 100

BATTERY_MIN = 0

BATTERY_LEVEL = 100

BATTERY_DRAIN = 0.20

BATTERY_CHARGE_RATE = 2

LOW_BATTERY_LEVEL = 20

# =====================================================
# Sensor
# =====================================================

SENSOR_RANGE = 100

SENSOR_WARNING_DISTANCE = 40

# =====================================================
# Obstacle
# =====================================================

OBSTACLE_RADIUS = 30

MAX_OBSTACLES = 5

# =====================================================
# Camera
# =====================================================

CAMERA_WIDTH = 640

CAMERA_HEIGHT = 480

# =====================================================
# Output Folder
# =====================================================

OUTPUT_FOLDER = "output/"

# =====================================================
# Supported Image Formats
# =====================================================

IMAGE_FORMATS = [
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp"
]

# =====================================================
# Supported Video Formats
# =====================================================

VIDEO_FORMATS = [
    ".mp4",
    ".avi",
    ".mov"
]

# =====================================================
# Drawing Colors (BGR)
# =====================================================

WHITE = (255,255,255)

BLACK = (0,0,0)

RED = (0,0,255)

GREEN = (0,255,0)

BLUE = (255,0,0)

YELLOW = (0,255,255)

CYAN = (255,255,0)

MAGENTA = (255,0,255)

GRAY = (150,150,150)

ORANGE = (0,165,255)

# =====================================================
# Face Drawing
# =====================================================

FACE_BOX_COLOR = GREEN

FACE_CENTER_COLOR = RED

FACE_BOX_THICKNESS = 2

FACE_CENTER_RADIUS = 5

# =====================================================
# Robot Drawing
# =====================================================

ROBOT_COLOR = BLUE

ROBOT_BORDER = BLACK

# =====================================================
# Dashboard
# =====================================================

FONT = cv2.FONT_HERSHEY_SIMPLEX

FONT_SCALE = 0.6

FONT_THICKNESS = 2

TEXT_COLOR = WHITE

BACKGROUND_COLOR = BLACK

# =====================================================
# Simulation
# =====================================================

SIMULATION_DELAY = 30

SHOW_FPS = True

SHOW_STATUS = True

SHOW_BATTERY = True

SHOW_SENSOR = True

SHOW_FACE_CENTER = True

SHOW_OBSTACLES = True

# =====================================================
# Messages
# =====================================================

STATUS_SEARCHING = "Searching Face"

STATUS_TRACKING = "Tracking Face"

STATUS_LEFT = "Turning Left"

STATUS_RIGHT = "Turning Right"

STATUS_FORWARD = "Moving Forward"

STATUS_STOP = "Stopped"

STATUS_OBSTACLE = "Obstacle Detected"

STATUS_LOW_BATTERY = "Low Battery"

STATUS_CHARGING = "Charging"
