"""
=========================================================
AI VisionBot

obstacle.py

Obstacle Simulation Module

Author : Your Name
Version : 1.0
=========================================================
"""

import random
import math
import cv2

from src.config import *


class Obstacle:

    """
    Obstacle Simulation Class
    """

    def __init__(self):

        self.obstacles = []

    # ==========================================
    # Create Random Obstacles
    # ==========================================

    def generate(
        self,
        width,
        height,
        number=5
    ):

        self.obstacles = []

        for _ in range(number):

            radius = random.randint(15, 40)

            x = random.randint(radius, width-radius)

            y = random.randint(radius, height-radius)

            self.obstacles.append(

                (x, y, radius)

            )

        return self.obstacles

    # ==========================================
    # Add Obstacle
    # ==========================================

    def add(

        self,

        x,

        y,

        radius=20

    ):

        self.obstacles.append(

            (x, y, radius)

        )

    # ==========================================
    # Remove All Obstacles
    # ==========================================

    def clear(self):

        self.obstacles = []

    # ==========================================
    # Get Obstacles
    # ==========================================

    def get(self):

        return self.obstacles

    # ==========================================
    # Count Obstacles
    # ==========================================

    def count(self):

        return len(self.obstacles)

    # ==========================================
    # Draw Obstacles
    # ==========================================

    def draw(

        self,

        image

    ):

        for x, y, r in self.obstacles:

            cv2.circle(

                image,

                (x, y),

                r,

                (0, 0, 255),

                -1

            )

            cv2.circle(

                image,

                (x, y),

                r,

                (255,255,255),

                2

            )

        return image

    # ==========================================
    # Distance
    # ==========================================

    def distance(

        self,

        robot_x,

        robot_y,

        obstacle

    ):

        ox, oy, _ = obstacle

        return math.sqrt(

            (robot_x-ox)**2 +

            (robot_y-oy)**2

        )
          # ==========================================
    # Collision Detection
    # ==========================================

    def collision(
        self,
        robot_x,
        robot_y,
        robot_radius=20
    ):

        """
        Check whether the robot has collided
        with any obstacle.
        """

        for obstacle in self.obstacles:

            ox, oy, radius = obstacle

            d = self.distance(
                robot_x,
                robot_y,
                obstacle
            )

            if d <= (robot_radius + radius):

                return True

        return False

    # ==========================================
    # Nearest Obstacle
    # ==========================================

    def nearest(
        self,
        robot_x,
        robot_y
    ):

        """
        Return the nearest obstacle.
        """

        if len(self.obstacles) == 0:

            return None

        nearest_obstacle = min(

            self.obstacles,

            key=lambda obstacle:
            self.distance(
                robot_x,
                robot_y,
                obstacle
            )

        )

        return nearest_obstacle

    # ==========================================
    # Warning Distance
    # ==========================================

    def warning(
        self,
        robot_x,
        robot_y,
        warning_distance=80
    ):

        """
        Check if an obstacle is
        within warning distance.
        """

        obstacle = self.nearest(
            robot_x,
            robot_y
        )

        if obstacle is None:

            return False

        d = self.distance(
            robot_x,
            robot_y,
            obstacle
        )

        return d <= warning_distance

    # ==========================================
    # Safe To Move
    # ==========================================

    def safe_move(
        self,
        robot_x,
        robot_y,
        robot_radius=20
    ):

        """
        Return True if movement is safe.
        """

        return not self.collision(

            robot_x,

            robot_y,

            robot_radius

        )

    # ==========================================
    # Obstacle Information
    # ==========================================

    def obstacle_info(
        self,
        obstacle
    ):

        """
        Return obstacle information.
        """

        if obstacle is None:

            return None

        x, y, radius = obstacle

        return {

            "x": x,

            "y": y,

            "radius": radius

        }

    # ==========================================
    # Print Obstacle Information
    # ==========================================

    def print_info(
        self,
        obstacle
    ):

        info = self.obstacle_info(obstacle)

        if info is None:

            print("No obstacle found.")

            return

        print("=" * 35)

        print("OBSTACLE INFORMATION")

        print("=" * 35)

        print("X      :", info["x"])

        print("Y      :", info["y"])

        print("Radius :", info["radius"])

        print("=" * 35)

    # ==========================================
    # Draw Warning Zone
    # ==========================================

    def draw_warning(
        self,
        image,
        robot_x,
        robot_y,
        warning_distance=80
    ):

        """
        Draw a warning circle around
        the robot.
        """

        cv2.circle(

            image,

            (robot_x, robot_y),

            warning_distance,

            (0, 255, 255),

            1

        )

        return image

    # ==========================================
    # Draw Nearest Obstacle
    # ==========================================

    def draw_nearest(
        self,
        image,
        robot_x,
        robot_y
    ):

        obstacle = self.nearest(
            robot_x,
            robot_y
        )

        if obstacle is None:

            return image

        x, y, radius = obstacle

        cv2.circle(

            image,

            (x, y),

            radius + 5,

            (0, 255, 255),

            2

        )

        return image 
    # ==========================================
    # Remove Obstacle
    # ==========================================

    def remove(self, index):

        """
        Remove an obstacle by index.
        """

        if 0 <= index < len(self.obstacles):

            self.obstacles.pop(index)

    # ==========================================
    # Robot Avoidance Direction
    # ==========================================

    def avoidance_direction(
        self,
        robot_x,
        robot_y
    ):

        """
        Suggest a simple avoidance direction.
        """

        obstacle = self.nearest(
            robot_x,
            robot_y
        )

        if obstacle is None:

            return "SAFE"

        ox, oy, _ = obstacle

        dx = robot_x - ox

        dy = robot_y - oy

        if abs(dx) > abs(dy):

            if dx > 0:

                return "MOVE RIGHT"

            else:

                return "MOVE LEFT"

        else:

            if dy > 0:

                return "MOVE DOWN"

            else:

                return "MOVE UP"

    # ==========================================
    # Regenerate Obstacles
    # ==========================================

    def regenerate(
        self,
        width,
        height,
        number=5
    ):

        """
        Create a new random obstacle map.
        """

        self.clear()

        self.generate(
            width,
            height,
            number
        )

    # ==========================================
    # Obstacle Statistics
    # ==========================================

    def statistics(self):

        """
        Return obstacle statistics.
        """

        if len(self.obstacles) == 0:

            return {

                "count": 0,

                "average_radius": 0

            }

        total_radius = sum(

            obstacle[2]

            for obstacle in self.obstacles

        )

        average = total_radius / len(self.obstacles)

        return {

            "count": len(self.obstacles),

            "average_radius": round(
                average,
                2
            )

        }

    # ==========================================
    # Print Statistics
    # ==========================================

    def print_statistics(self):

        stats = self.statistics()

        print("=" * 40)

        print("OBSTACLE STATISTICS")

        print("=" * 40)

        print("Total Obstacles :", stats["count"])

        print("Average Radius  :", stats["average_radius"])

        print("=" * 40)

    # ==========================================
    # Update Simulation
    # ==========================================

    def update(
        self,
        image,
        robot_x,
        robot_y
    ):

        """
        Draw all simulation objects.
        """

        image = self.draw(image)

        image = self.draw_warning(

            image,

            robot_x,

            robot_y

        )

        image = self.draw_nearest(

            image,

            robot_x,

            robot_y

        )

        return image

    # ==========================================
    # Summary
    # ==========================================

    def summary(self):

        stats = self.statistics()

        return {

            "Obstacles": stats["count"],

            "Average Radius":
                stats["average_radius"]

        }

    # ==========================================
    # Print Summary
    # ==========================================

    def print_summary(self):

        summary = self.summary()

        print("=" * 45)

        print("AI VisionBot Obstacle Summary")

        print("=" * 45)

        for key, value in summary.items():

            print(f"{key:<20}: {value}")

        print("=" * 45)

    # ==========================================
    # Test Module
    # ==========================================

    def test(self):

        print("Testing Obstacle Module...\n")

        self.generate(

            640,

            480,

            5

        )

        self.print_statistics()

        print("Obstacle Module Test Completed.")
