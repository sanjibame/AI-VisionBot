"""
=========================================================
AI VisionBot

sensors.py

Robot Sensor Simulation Module

Author : Your Name
Version : 1.0
=========================================================
"""

import math

from src.config import *


class Sensors:

    """
    Robot Sensor Simulation
    """

    def __init__(self):

        self.front_distance = float("inf")

        self.left_distance = float("inf")

        self.right_distance = float("inf")

        self.rear_distance = float("inf")

        self.collision = False

    # ==========================================
    # Euclidean Distance
    # ==========================================

    def distance(

        self,

        x1,

        y1,

        x2,

        y2

    ):

        return math.sqrt(

            (x2-x1)**2 +

            (y2-y1)**2

        )

    # ==========================================
    # Scan Environment
    # ==========================================

    def scan(

        self,

        robot_x,

        robot_y,

        obstacles

    ):

        """
        Scan nearby obstacles.
        """

        if len(obstacles) == 0:

            self.reset()

            return

        nearest = float("inf")

        for ox, oy, radius in obstacles:

            d = self.distance(

                robot_x,

                robot_y,

                ox,

                oy

            ) - radius

            if d < nearest:

                nearest = d

        self.front_distance = max(0, nearest)

        self.left_distance = self.front_distance

        self.right_distance = self.front_distance

        self.rear_distance = self.front_distance

    # ==========================================
    # Collision Check
    # ==========================================

    def check_collision(

        self,

        threshold=10

    ):

        self.collision = (

            self.front_distance <= threshold

        )

        return self.collision

    # ==========================================
    # Reset Sensors
    # ==========================================

    def reset(self):

        self.front_distance = float("inf")

        self.left_distance = float("inf")

        self.right_distance = float("inf")

        self.rear_distance = float("inf")

        self.collision = False

    # ==========================================
    # Front Sensor
    # ==========================================

    def front(self):

        return self.front_distance

    # ==========================================
    # Left Sensor
    # ==========================================

    def left(self):

        return self.left_distance

    # ==========================================
    # Right Sensor
    # ==========================================

    def right(self):

        return self.right_distance

    # ==========================================
    # Rear Sensor
    # ==========================================

    def rear(self):

        return self.rear_distance
          # ==========================================
    # Sensor Status
    # ==========================================

    def status(self):

        """
        Return current sensor readings.
        """

        return {

            "Front": round(self.front_distance, 2),

            "Left": round(self.left_distance, 2),

            "Right": round(self.right_distance, 2),

            "Rear": round(self.rear_distance, 2),

            "Collision": self.collision

        }

    # ==========================================
    # Obstacle Direction
    # ==========================================

    def obstacle_direction(self):

        """
        Determine the nearest obstacle direction.
        """

        distances = {

            "FRONT": self.front_distance,

            "LEFT": self.left_distance,

            "RIGHT": self.right_distance,

            "REAR": self.rear_distance

        }

        direction = min(

            distances,

            key=distances.get

        )

        return direction

    # ==========================================
    # Safe To Move
    # ==========================================

    def safe(self, minimum_distance=30):

        """
        Check whether the robot
        can move safely.
        """

        return self.front_distance > minimum_distance

    # ==========================================
    # Warning Message
    # ==========================================

    def warning(self):

        """
        Return warning based on sensor.
        """

        if self.collision:

            return "COLLISION DETECTED"

        if self.front_distance < 30:

            return "OBSTACLE AHEAD"

        if self.front_distance < 60:

            return "MOVE CAREFULLY"

        return "PATH CLEAR"

    # ==========================================
    # Sensor Information
    # ==========================================

    def info(self):

        return {

            "Front": self.front_distance,

            "Left": self.left_distance,

            "Right": self.right_distance,

            "Rear": self.rear_distance,

            "Direction":

                self.obstacle_direction(),

            "Safe":

                self.safe(),

            "Warning":

                self.warning()

        }

    # ==========================================
    # Print Sensor Information
    # ==========================================

    def print_info(self):

        info = self.info()

        print("=" * 40)

        print("SENSOR INFORMATION")

        print("=" * 40)

        for key, value in info.items():

            print(f"{key:<12}: {value}")

        print("=" * 40)

    # ==========================================
    # Sensor Diagnostics
    # ==========================================

    def diagnostics(self):

        """
        Perform simple sensor diagnostics.
        """

        if (

            self.front_distance < 0 or

            self.left_distance < 0 or

            self.right_distance < 0 or

            self.rear_distance < 0

        ):

            return False

        return True

    # ==========================================
    # Sensor Summary
    # ==========================================

    def summary(self):

        return {

            "Direction":

                self.obstacle_direction(),

            "Collision":

                self.collision,

            "Warning":

                self.warning(),

            "Healthy":

                self.diagnostics()

        }

    # ==========================================
    # Print Summary
    # ==========================================

    def print_summary(self):

        summary = self.summary()

        print("=" * 40)

        print("SENSOR SUMMARY")

        print("=" * 40)

        for key, value in summary.items():

            print(f"{key:<12}: {value}")

        print("=" * 40)
          # ==========================================
    # Initialize History
    # ==========================================

    def initialize_history(self):

        """
        Initialize sensor history.
        """

        self.history = []

    # ==========================================
    # Record Sensor Data
    # ==========================================

    def record(self):

        """
        Save current sensor readings.
        """

        if not hasattr(self, "history"):

            self.initialize_history()

        self.history.append({

            "front": self.front_distance,

            "left": self.left_distance,

            "right": self.right_distance,

            "rear": self.rear_distance,

            "collision": self.collision

        })

    # ==========================================
    # Get History
    # ==========================================

    def get_history(self):

        """
        Return recorded history.
        """

        if not hasattr(self, "history"):

            self.initialize_history()

        return self.history

    # ==========================================
    # Clear History
    # ==========================================

    def clear_history(self):

        """
        Remove all recorded history.
        """

        self.history = []

    # ==========================================
    # Update Sensors
    # ==========================================

    def update(

        self,

        robot_x,

        robot_y,

        obstacles

    ):

        """
        Update sensor readings.
        """

        self.scan(

            robot_x,

            robot_y,

            obstacles

        )

        self.check_collision()

        self.record()

    # ==========================================
    # Reset Statistics
    # ==========================================

    def reset_statistics(self):

        """
        Reset sensor history.
        """

        self.clear_history()

    # ==========================================
    # Sensor Statistics
    # ==========================================

    def statistics(self):

        """
        Return sensor statistics.
        """

        history = self.get_history()

        return {

            "Samples": len(history),

            "Collision":

                self.collision,

            "Direction":

                self.obstacle_direction(),

            "Safe":

                self.safe()

        }

    # ==========================================
    # Print Statistics
    # ==========================================

    def print_statistics(self):

        stats = self.statistics()

        print("=" * 45)

        print("SENSOR STATISTICS")

        print("=" * 45)

        for key, value in stats.items():

            print(f"{key:<15}: {value}")

        print("=" * 45)

    # ==========================================
    # Self Test
    # ==========================================

    def test(self):

        """
        Test sensor module.
        """

        print("Testing Sensors...\n")

        sample_obstacles = [

            (120, 150, 20),

            (300, 250, 30),

            (500, 350, 25)

        ]

        self.update(

            100,

            100,

            sample_obstacles

        )

        self.print_info()

        self.print_statistics()

        print("\nSensor Test Completed.")

    # ==========================================
    # Module Summary
    # ==========================================

    def module_summary(self):

        """
        Return overall module summary.
        """

        return {

            "Front Sensor":

                self.front_distance,

            "Left Sensor":

                self.left_distance,

            "Right Sensor":

                self.right_distance,

            "Rear Sensor":

                self.rear_distance,

            "Collision":

                self.collision,

            "History":

                len(self.get_history())

        }

    # ==========================================
    # Print Module Summary
    # ==========================================

    def print_module_summary(self):

        summary = self.module_summary()

        print("=" * 50)

        print("AI VisionBot Sensor Module Summary")

        print("=" * 50)

        for key, value in summary.items():

            print(f"{key:<18}: {value}")

        print("=" * 50)
      
