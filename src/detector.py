"""
=========================================================
AI VisionBot

detector.py

Face Detection Module

=========================================================

Author : Your Name
Version : 1.0
"""

import cv2

from src.config import *

from src.image_processing import ImageProcessor


class FaceDetector:

    """
    Face Detection Class
    """

    def __init__(self):

        self.processor = ImageProcessor()

        self.face_detector = cv2.CascadeClassifier(
            CASCADE_PATH
        )

    # ==========================================
    # Detect Faces
    # ==========================================

    def detect(self, image):

        """
        Detect faces from image
        """

        gray = self.processor.gray(image)

        faces = self.face_detector.detectMultiScale(

            gray,

            scaleFactor=FACE_SCALE_FACTOR,

            minNeighbors=FACE_MIN_NEIGHBORS,

            minSize=FACE_MIN_SIZE

        )

        return faces

    # ==========================================
    # Count Faces
    # ==========================================

    def count_faces(self, faces):

        return len(faces)

    # ==========================================
    # Check Face Found
    # ==========================================

    def face_found(self, faces):

        return len(faces) > 0

    # ==========================================
    # Get Largest Face
    # ==========================================

    def largest_face(self, faces):

        if len(faces) == 0:

            return None

        largest = max(

            faces,

            key=lambda f: f[2] * f[3]

        )

        return largest

    # ==========================================
    # Face Center
    # ==========================================

    def face_center(self, face):

        x, y, w, h = face

        center_x = x + w // 2

        center_y = y + h // 2

        return center_x, center_y

    # ==========================================
    # Draw Face Box
    # ==========================================

    def draw_face(self, image, face):

        x, y, w, h = face

        image = self.processor.draw_rectangle(

            image,

            x,

            y,

            w,

            h,

            FACE_BOX_COLOR,

            FACE_BOX_THICKNESS

        )

        center_x, center_y = self.face_center(face)

        image = self.processor.draw_face_center(

            image,

            center_x,

            center_y

        )

        return image

      # ==========================================
    # Robot Decision
    # ==========================================

    def robot_decision(self, face, image_width):

        """
        Decide robot movement
        based on face position.
        """

        if face is None:

            return "STOP"

        center_x, _ = self.face_center(face)

        left_boundary = image_width // 3

        right_boundary = (image_width * 2) // 3

        if center_x < left_boundary:

            return "LEFT"

        elif center_x > right_boundary:

            return "RIGHT"

        else:

            return "FORWARD"

    # ==========================================
    # Draw Decision
    # ==========================================

    def draw_decision(self, image, decision):

        colors = {

            "LEFT": (0,255,255),

            "RIGHT": (255,255,0),

            "FORWARD": (0,255,0),

            "STOP": (0,0,255)

        }

        color = colors.get(
            decision,
            (255,255,255)
        )

        cv2.putText(

            image,

            f"Decision : {decision}",

            (20,40),

            FONT,

            0.8,

            color,

            2

        )

        return image
          # ==========================================
    # Robot Decision
    # ==========================================

    def robot_decision(self, face, image_width):

        """
        Decide robot movement
        based on face position.
        """

        if face is None:

            return "STOP"

        center_x, _ = self.face_center(face)

        left_boundary = image_width // 3

        right_boundary = (image_width * 2) // 3

        if center_x < left_boundary:

            return "LEFT"

        elif center_x > right_boundary:

            return "RIGHT"

        else:

            return "FORWARD"

    # ==========================================
    # Draw Decision
    # ==========================================

    def draw_decision(self, image, decision):

        colors = {

            "LEFT": (0,255,255),

            "RIGHT": (255,255,0),

            "FORWARD": (0,255,0),

            "STOP": (0,0,255)

        }

        color = colors.get(
            decision,
            (255,255,255)
        )

        cv2.putText(

            image,

            f"Decision : {decision}",

            (20,40),

            FONT,

            0.8,

            color,

            2

        )

        return image

    # ==========================================
    # Draw Guide Lines
    # ==========================================

    def draw_guidelines(self, image):

        height, width = image.shape[:2]

        left = width // 3

        right = (width * 2) // 3

        cv2.line(

            image,

            (left,0),

            (left,height),

            (255,255,0),

            2

        )

        cv2.line(

            image,

            (right,0),

            (right,height),

            (255,255,0),

            2

        )

        return image

    # ==========================================
    # Face Position
    # ==========================================

    def face_position(self, face, image_width):

        if face is None:

            return "NO FACE"

        center_x, _ = self.face_center(face)

        left = image_width // 3

        right = (image_width * 2) // 3

        if center_x < left:

            return "LEFT"

        elif center_x > right:

            return "RIGHT"

        else:

            return "CENTER"

    # ==========================================
    # Face Area
    # ==========================================

    def face_area(self, face):

        if face is None:

            return 0

        _, _, w, h = face

        return w * h

    # ==========================================
    # Face Distance (Approximation)
    # ==========================================

    def estimate_distance(self, face):

        if face is None:

            return "UNKNOWN"

        _, _, w, _ = face

        if w > 220:

            return "VERY CLOSE"

        elif w > 150:

            return "CLOSE"

        elif w > 80:

            return "MEDIUM"

        else:

            return "FAR"

    # ==========================================
    # Draw Distance
    # ==========================================

    def draw_distance(self, image, distance):

        cv2.putText(

            image,

            f"Distance : {distance}",

            (20,70),

            FONT,

            0.7,

            (0,255,255),

            2

        )

        return image

    # ==========================================
    # Draw Face Count
    # ==========================================

    def draw_face_count(self, image, faces):

        cv2.putText(

            image,

            f"Faces : {len(faces)}",

            (20,100),

            FONT,

            0.7,

            (255,255,255),

            2

        )

        return image
          # ==========================================
    # Get All Face Centers
    # ==========================================

    def all_face_centers(self, faces):

        centers = []

        for (x, y, w, h) in faces:

            cx = x + w // 2

            cy = y + h // 2

            centers.append((cx, cy))

        return centers

    # ==========================================
    # Get Face Information
    # ==========================================

    def face_information(self, face):

        if face is None:

            return None

        x, y, w, h = face

        cx, cy = self.face_center(face)

        info = {

            "x": x,

            "y": y,

            "width": w,

            "height": h,

            "center_x": cx,

            "center_y": cy,

            "area": w * h

        }

        return info

    # ==========================================
    # Print Face Information
    # ==========================================

    def print_information(self, face):

        info = self.face_information(face)

        if info is None:

            print("No Face Detected")

            return

        print("-" * 35)

        print("FACE INFORMATION")

        print("-" * 35)

        print("X :", info["x"])

        print("Y :", info["y"])

        print("Width :", info["width"])

        print("Height :", info["height"])

        print("Center :", info["center_x"], info["center_y"])

        print("Area :", info["area"])

    # ==========================================
    # Draw Face Coordinates
    # ==========================================

    def draw_coordinates(self, image, face):

        if face is None:

            return image

        x, y, w, h = face

        text = f"({x},{y})"

        cv2.putText(

            image,

            text,

            (x, y - 10),

            FONT,

            0.5,

            (255,255,255),

            1

        )

        return image

    # ==========================================
    # Get Nearest Face
    # ==========================================

    def nearest_face(self, faces):

        if len(faces) == 0:

            return None

        nearest = max(

            faces,

            key=lambda f: f[2]

        )

        return nearest

    # ==========================================
    # Draw All Faces
    # ==========================================

    def draw_all_faces(self, image, faces):

        for face in faces:

            self.draw_face(image, face)

        return image

    # ==========================================
    # Get Tracking Target
    # ==========================================

    def tracking_target(self, faces):

        """
        Select the largest detected face
        as the robot tracking target.
        """

        return self.largest_face(faces)

    # ==========================================
    # Detect and Track
    # ==========================================

    def detect_and_track(self, image):

        faces = self.detect(image)

        target = self.tracking_target(faces)

        if target is not None:

            image = self.draw_face(image, target)

        return image, target, faces

    # ==========================================
    # Face Movement Direction
    # ==========================================

    def movement_direction(
        self,
        previous_center,
        current_center
    ):

        if previous_center is None:

            return "UNKNOWN"

        px, _ = previous_center

        cx, _ = current_center

        if cx > px + 10:

            return "MOVING RIGHT"

        elif cx < px - 10:

            return "MOVING LEFT"

        else:

            return "STABLE"

    # ==========================================
    # Draw Movement Direction
    # ==========================================

    def draw_movement(
        self,
        image,
        movement
    ):

        cv2.putText(

            image,

            f"Movement : {movement}",

            (20,130),

            FONT,

            0.7,

            (0,255,255),

            2

        )

        return image
          # ==========================================
    # Robot Status
    # ==========================================

    def robot_status(self, decision):

        status = {

            "LEFT": "Robot Turning Left",

            "RIGHT": "Robot Turning Right",

            "FORWARD": "Robot Moving Forward",

            "STOP": "Robot Stopped"

        }

        return status.get(decision, "Unknown")

    # ==========================================
    # Draw Robot Status
    # ==========================================

    def draw_robot_status(
        self,
        image,
        decision
    ):

        status = self.robot_status(decision)

        cv2.putText(

            image,

            status,

            (20,160),

            FONT,

            0.7,

            (0,255,0),

            2

        )

        return image

    # ==========================================
    # Draw Frame Center
    # ==========================================

    def draw_frame_center(
        self,
        image
    ):

        height, width = image.shape[:2]

        cx = width // 2

        cy = height // 2

        cv2.circle(

            image,

            (cx, cy),

            6,

            (255,0,255),

            -1

        )

        return image

    # ==========================================
    # Draw Tracking Line
    # ==========================================

    def draw_tracking_line(
        self,
        image,
        face
    ):

        if face is None:

            return image

        h, w = image.shape[:2]

        frame_center = (w // 2, h // 2)

        face_center = self.face_center(face)

        cv2.line(

            image,

            frame_center,

            face_center,

            (255,255,0),

            2

        )

        return image

    # ==========================================
    # Complete Frame Processing
    # ==========================================

    def process_frame(
        self,
        image
    ):

        faces = self.detect(image)

        face = self.tracking_target(faces)

        decision = "STOP"

        if face is not None:

            image = self.draw_face(
                image,
                face
            )

            decision = self.robot_decision(
                face,
                image.shape[1]
            )

            distance = self.estimate_distance(face)

            image = self.draw_distance(
                image,
                distance
            )

            image = self.draw_coordinates(
                image,
                face
            )

            image = self.draw_tracking_line(
                image,
                face
            )

        image = self.draw_guidelines(image)

        image = self.draw_frame_center(image)

        image = self.draw_decision(
            image,
            decision
        )

        image = self.draw_robot_status(
            image,
            decision
        )

        image = self.draw_face_count(
            image,
            faces
        )

        return image, decision, faces

    # ==========================================
    # Print Summary
    # ==========================================

    def print_summary(
        self,
        faces,
        decision
    ):

        print("=" * 40)

        print("AI VisionBot Summary")

        print("=" * 40)

        print("Faces Detected :", len(faces))

        print("Robot Decision :", decision)

        print("=" * 40)

    # ==========================================
    # Test Detector
    # ==========================================

    def test(
        self,
        image
