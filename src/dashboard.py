"""
=========================================================
AI VisionBot

dashboard.py

Robot Dashboard Module

Author : Your Name
Version : 1.0
=========================================================
"""

import cv2

from src.config import *


class Dashboard:

    """
    Dashboard Class
    """

    def __init__(self):

        self.font = cv2.FONT_HERSHEY_SIMPLEX

        self.font_scale = 0.6

        self.color = (0,255,0)

        self.thickness = 2

    # ==========================================
    # Draw Title
    # ==========================================

    def title(self, image):

        cv2.putText(

            image,

            "AI VisionBot Dashboard",

            (15,30),

            self.font,

            0.8,

            (255,255,0),

            2

        )

        return image

    # ==========================================
    # Draw Robot Position
    # ==========================================

    def robot_position(

        self,

        image,

        robot

    ):

        text = f"Position : ({robot.x}, {robot.y})"

        cv2.putText(

            image,

            text,

            (15,60),

            self.font,

            self.font_scale,

            self.color,

            self.thickness

        )

        return image

    # ==========================================
    # Draw Robot Direction
    # ==========================================

    def robot_direction(

        self,

        image,

        robot

    ):

        text = f"Direction : {robot.direction}"

        cv2.putText(

            image,

            text,

            (15,90),

            self.font,

            self.font_scale,

            self.color,

            self.thickness

        )

        return image

    # ==========================================
    # Draw Robot Speed
    # ==========================================

    def robot_speed(

        self,

        image,

        robot

    ):

        text = f"Speed : {robot.speed}"

        cv2.putText(

            image,

            text,

            (15,120),

            self.font,

            self.font_scale,

            self.color,

            self.thickness

        )

        return image

    # ==========================================
    # Draw Robot Status
    # ==========================================

    def robot_status(

        self,

        image,

        robot

    ):

        text = f"Status : {robot.status}"

        cv2.putText(

            image,

            text,

            (15,150),

            self.font,

            self.font_scale,

            self.color,

            self.thickness

        )

        return image

    # ==========================================
    # Draw Battery
    # ==========================================

    def battery(

        self,

        image,

        battery

    ):

        text = f"Battery : {battery.percentage()} %"

        cv2.putText(

            image,

            text,

            (15,180),

            self.font,

            self.font_scale,

            (0,255,255),

            self.thickness

        )

        return image

    # ==========================================
    # Draw Battery Status
    # ==========================================

    def battery_status(

        self,

        image,

        battery

    ):

        text = f"Battery Status : {battery.battery_status()}"

        cv2.putText(

            image,

            text,

            (15,210),

            self.font,

            self.font_scale,

            (0,255,255),

            self.thickness

        )

        return image
          # ==========================================
    # Draw Face Count
    # ==========================================

    def face_count(

        self,

        image,

        faces

    ):

        text = f"Faces Detected : {len(faces)}"

        cv2.putText(

            image,

            text,

            (15,240),

            self.font,

            self.font_scale,

            (255,255,255),

            self.thickness

        )

        return image

    # ==========================================
    # Draw FPS
    # ==========================================

    def fps(

        self,

        image,

        fps

    ):

        text = f"FPS : {fps:.2f}"

        cv2.putText(

            image,

            text,

            (15,270),

            self.font,

            self.font_scale,

            (255,255,0),

            self.thickness

        )

        return image

    # ==========================================
    # Draw Obstacle Count
    # ==========================================

    def obstacle_count(

        self,

        image,

        obstacle

    ):

        text = f"Obstacles : {obstacle.count()}"

        cv2.putText(

            image,

            text,

            (15,300),

            self.font,

            self.font_scale,

            (0,255,255),

            self.thickness

        )

        return image

    # ==========================================
    # Draw Sensor Information
    # ==========================================

    def sensor_info(

        self,

        image,

        sensors

    ):

        text = (

            f"Front:{sensors.front():.1f}  "

            f"Left:{sensors.left():.1f}  "

            f"Right:{sensors.right():.1f}"

        )

        cv2.putText(

            image,

            text,

            (15,330),

            self.font,

            0.5,

            (255,255,255),

            1

        )

        return image

    # ==========================================
    # Draw Camera Resolution
    # ==========================================

    def resolution(

        self,

        image

    ):

        h, w = image.shape[:2]

        text = f"Resolution : {w} x {h}"

        cv2.putText(

            image,

            text,

            (15,360),

            self.font,

            self.font_scale,

            (255,255,0),

            self.thickness

        )

        return image

    # ==========================================
    # Draw Tracking Status
    # ==========================================

    def tracking(

        self,

        image,

        tracking

    ):

        text = f"Tracking : {tracking}"

        color = (

            (0,255,0)

            if tracking

            else

            (0,0,255)

        )

        cv2.putText(

            image,

            text,

            (15,390),

            self.font,

            self.font_scale,

            color,

            self.thickness

        )

        return image

    # ==========================================
    # Draw Warning Message
    # ==========================================

    def warning(

        self,

        image,

        message

    ):

        cv2.putText(

            image,

            message,

            (15,420),

            self.font,

            0.7,

            (0,0,255),

            2

        )

        return image

    # ==========================================
    # Draw Robot Heading
    # ==========================================

    def heading(

        self,

        image,

        robot

    ):

        text = f"Heading : {robot.heading()}°"

        cv2.putText(

            image,

            text,

            (15,450),

            self.font,

            self.font_scale,

            (255,255,255),

            self.thickness

        )

        return image
          # ==========================================
    # Draw Battery Health
    # ==========================================

    def battery_health(
        self,
        image,
        battery
    ):

        text = f"Battery Health : {battery.health()}"

        cv2.putText(
            image,
            text,
            (15, 480),
            self.font,
            self.font_scale,
            (0,255,255),
            self.thickness
        )

        return image

    # ==========================================
    # Draw Sensor Status
    # ==========================================

    def sensor_status(
        self,
        image,
        sensors
    ):

        status = "OK"

        if sensors.collision:

            status = "COLLISION"

        elif not sensors.safe():

            status = "WARNING"

        text = f"Sensors : {status}"

        cv2.putText(
            image,
            text,
            (15,510),
            self.font,
            self.font_scale,
            (255,255,255),
            self.thickness
        )

        return image

    # ==========================================
    # Draw AI Decision
    # ==========================================

    def ai_decision(
        self,
        image,
        decision
    ):

        text = f"AI Decision : {decision}"

        cv2.putText(
            image,
            text,
            (15,540),
            self.font,
            self.font_scale,
            (0,255,0),
            self.thickness
        )

        return image

    # ==========================================
    # Draw Robot Path
    # ==========================================

    def path_statistics(
        self,
        image,
        robot
    ):

        path = robot.get_path()

        text = f"Path Points : {len(path)}"

        cv2.putText(
            image,
            text,
            (15,570),
            self.font,
            self.font_scale,
            (255,255,0),
            self.thickness
        )

        return image

    # ==========================================
    # Draw Complete Dashboard
    # ==========================================

    def draw(
        self,
        image,
        robot,
        battery,
        detector_faces,
        obstacle,
        sensors,
        fps,
        decision,
        tracking
    ):

        self.title(image)

        self.robot_position(image, robot)

        self.robot_direction(image, robot)

        self.robot_speed(image, robot)

        self.robot_status(image, robot)

        self.battery(image, battery)

        self.battery_status(image, battery)

        self.face_count(image, detector_faces)

        self.fps(image, fps)

        self.obstacle_count(image, obstacle)

        self.sensor_info(image, sensors)

        self.resolution(image)

        self.tracking(image, tracking)

        self.warning(
            image,
            sensors.warning()
        )

        self.heading(image, robot)

        self.battery_health(
            image,
            battery
        )

        self.sensor_status(
            image,
            sensors
        )

        self.ai_decision(
            image,
            decision
        )

        self.path_statistics(
            image,
            robot
        )

        return image

    # ==========================================
    # Dashboard Summary
    # ==========================================

    def summary(
        self,
        robot,
        battery
    ):

        return {

            "Robot Status": robot.status,

            "Battery": battery.percentage(),

            "Direction": robot.direction,

            "Speed": robot.speed

        }

    # ==========================================
    # Print Summary
    # ==========================================

    def print_summary(
        self,
        robot,
        battery
    ):

        summary = self.summary(
            robot,
            battery
        )

        print("=" * 45)

        print("AI VisionBot Dashboard Summary")

        print("=" * 45)

        for key, value in summary.items():

            print(f"{key:<15}: {value}")

        print("=" * 45)

    # ==========================================
    # Dashboard Test
    # ==========================================

    def test(
        self,
        robot,
        battery
    ):

        print("Testing Dashboard Module...\n")

        self.print_summary(
            robot,
            battery
        )

        print("\nDashboard Test Completed.")
      
