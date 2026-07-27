"""
=========================================================
AI VisionBot

robot.py

Robot Control Module

Author : Your Name
Version : 1.0
=========================================================
"""

from src.config import *


class Robot:

    """
    Robot Controller
    """

    def __init__(self):

        self.x = ROBOT_START_X

        self.y = ROBOT_START_Y

        self.speed = ROBOT_SPEED

        self.direction = "STOP"

        self.status = "Idle"

    # ==========================================
    # Move Left
    # ==========================================

    def move_left(self):

        self.x -= self.speed

        self.direction = "LEFT"

        self.status = "Turning Left"

    # ==========================================
    # Move Right
    # ==========================================

    def move_right(self):

        self.x += self.speed

        self.direction = "RIGHT"

        self.status = "Turning Right"

    # ==========================================
    # Move Forward
    # ==========================================

    def move_forward(self):

        self.y -= self.speed

        self.direction = "FORWARD"

        self.status = "Moving Forward"

    # ==========================================
    # Move Backward
    # ==========================================

    def move_backward(self):

        self.y += self.speed

        self.direction = "BACKWARD"

        self.status = "Moving Backward"

    # ==========================================
    # Stop Robot
    # ==========================================

    def stop(self):

        self.direction = "STOP"

        self.status = "Stopped"

    # ==========================================
    # Reset Robot
    # ==========================================

    def reset(self):

        self.x = ROBOT_START_X

        self.y = ROBOT_START_Y

        self.direction = "STOP"

        self.status = "Idle"

    # ==========================================
    # Robot Position
    # ==========================================

    def position(self):

        return self.x, self.y

    # ==========================================
    # Robot Information
    # ==========================================

    def info(self):

        return {

            "x": self.x,

            "y": self.y,

            "speed": self.speed,

            "direction": self.direction,

            "status": self.status

        }

    # ==========================================
    # Print Robot Information
    # ==========================================

    def print_info(self):

        print("=" * 35)

        print("ROBOT INFORMATION")

        print("=" * 35)

        print("X :", self.x)

        print("Y :", self.y)

        print("Speed :", self.speed)

        print("Direction :", self.direction)

        print("Status :", self.status)

        print("=" * 35)
          # ==========================================
    # Execute Robot Decision
    # ==========================================

    def execute(self, decision):

        """
        Execute robot movement based
        on detector decision.
        """

        if decision == "LEFT":

            self.move_left()

        elif decision == "RIGHT":

            self.move_right()

        elif decision == "FORWARD":

            self.move_forward()

        elif decision == "BACKWARD":

            self.move_backward()

        else:

            self.stop()

    # ==========================================
    # Boundary Check
    # ==========================================

    def keep_inside(
        self,
        width,
        height
    ):

        """
        Keep robot inside simulation area.
        """

        if self.x < 0:

            self.x = 0

        if self.x > width:

            self.x = width

        if self.y < 0:

            self.y = 0

        if self.y > height:

            self.y = height

    # ==========================================
    # Set Speed
    # ==========================================

    def set_speed(self, speed):

        self.speed = max(1, speed)

    # ==========================================
    # Increase Speed
    # ==========================================

    def increase_speed(self, value=1):

        self.speed += value

    # ==========================================
    # Decrease Speed
    # ==========================================

    def decrease_speed(self, value=1):

        self.speed = max(

            1,

            self.speed - value

        )

    # ==========================================
    # Robot Heading Angle
    # ==========================================

    def heading(self):

        directions = {

            "FORWARD": 90,

            "BACKWARD": 270,

            "LEFT": 180,

            "RIGHT": 0,

            "STOP": -1

        }

        return directions.get(

            self.direction,

            -1

        )

    # ==========================================
    # Save Current Position
    # ==========================================

    def save_position(self):

        return (

            self.x,

            self.y

        )

    # ==========================================
    # Restore Position
    # ==========================================

    def restore_position(

        self,

        position

    ):

        self.x = position[0]

        self.y = position[1]

    # ==========================================
    # Distance Travelled
    # ==========================================

    def distance_from(

        self,

        start_position

    ):

        dx = self.x - start_position[0]

        dy = self.y - start_position[1]

        return (dx ** 2 + dy ** 2) ** 0.5

    # ==========================================
    # Robot State
    # ==========================================

    def state(self):

        return {

            "position": (

                self.x,

                self.y

            ),

            "speed": self.speed,

            "direction": self.direction,

            "status": self.status,

            "heading": self.heading()

        }

    # ==========================================
    # Print Robot State
    # ==========================================

    def print_state(self):

        state = self.state()

        print("=" * 40)

        print("CURRENT ROBOT STATE")

        print("=" * 40)

        print("Position :", state["position"])

        print("Speed :", state["speed"])

        print("Direction :", state["direction"])

        print("Heading :", state["heading"])

        print("Status :", state["status"])

        print("=" * 40)
          # ==========================================
    # Initialize Robot Path
    # ==========================================

    def initialize_path(self):

        """
        Initialize robot path history.
        """

        self.path = []

    # ==========================================
    # Store Current Position
    # ==========================================

    def update_path(self):

        """
        Save current robot position.
        """

        if not hasattr(self, "path"):

            self.initialize_path()

        self.path.append((self.x, self.y))

    # ==========================================
    # Get Path
    # ==========================================

    def get_path(self):

        """
        Return robot path.
        """

        if not hasattr(self, "path"):

            self.initialize_path()

        return self.path

    # ==========================================
    # Clear Path
    # ==========================================

    def clear_path(self):

        """
        Remove all stored positions.
        """

        self.path = []

    # ==========================================
    # Return Home
    # ==========================================

    def return_home(self):

        """
        Move robot back to start position.
        """

        self.x = ROBOT_START_X

        self.y = ROBOT_START_Y

        self.direction = "HOME"

        self.status = "Returned Home"

    # ==========================================
    # Battery Safe Mode
    # ==========================================

    def battery_safe_mode(self, battery_level):

        """
        Stop robot if battery is too low.
        """

        if battery_level <= LOW_BATTERY_LEVEL:

            self.stop()

            self.status = "Low Battery"

            return False

        return True

    # ==========================================
    # Obstacle Avoidance
    # ==========================================

    def avoid_obstacle(self):

        """
        Simple obstacle avoidance.
        """

        self.move_right()

        self.move_forward()

        self.status = "Avoiding Obstacle"

    # ==========================================
    # Update Robot
    # ==========================================

    def update(
        self,
        decision,
        width,
        height
    ):

        """
        Update robot state.
        """

        self.execute(decision)

        self.keep_inside(width, height)

        self.update_path()

    # ==========================================
    # Robot Summary
    # ==========================================

    def summary(self):

        return {

            "Position": (self.x, self.y),

            "Direction": self.direction,

            "Speed": self.speed,

            "Status": self.status,

            "Heading": self.heading(),

            "Path Points": len(self.get_path())

        }

    # ==========================================
    # Print Summary
    # ==========================================

    def print_summary(self):

        summary = self.summary()

        print("=" * 45)

        print("AI VisionBot Robot Summary")

        print("=" * 45)

        for key, value in summary.items():

            print(f"{key:<15}: {value}")

        print("=" * 45)

    # ==========================================
    # Test Robot
    # ==========================================

    def test(self):

        print("Testing Robot...\n")

        self.initialize_path()

        self.execute("FORWARD")

        self.execute("LEFT")

        self.execute("RIGHT")

        self.execute("STOP")

        self.update_path()

        self.print_summary()

        print("Robot Test Completed.")
