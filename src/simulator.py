"""
=========================================================
AI VisionBot

simulator.py

Main Robot Simulator

Author : Your Name
Version : 1.0
=========================================================
"""

import time
import cv2

from src.camera import Camera
from src.detector import FaceDetector
from src.robot import Robot
from src.battery import Battery
from src.obstacle import Obstacle
from src.sensors import Sensors
from src.dashboard import Dashboard
from src.config import *


class RobotSimulator:

    """
    AI VisionBot Simulator
    """

    def __init__(self):

        self.camera = Camera()

        self.detector = FaceDetector()

        self.robot = Robot()

        self.battery = Battery()

        self.obstacle = Obstacle()

        self.sensors = Sensors()

        self.dashboard = Dashboard()

        self.running = False

        self.fps = 0

        self.previous_time = time.time()

    # ==========================================
    # Initialize Simulator
    # ==========================================

    def initialize(self):

        """
        Initialize simulator.
        """

        self.camera.start()

        self.robot.initialize_path()

        self.obstacle.generate(

            WIDTH,

            HEIGHT,

            number=5

        )

        self.running = True

    # ==========================================
    # Calculate FPS
    # ==========================================

    def calculate_fps(self):

        current = time.time()

        elapsed = current - self.previous_time

        if elapsed > 0:

            self.fps = 1 / elapsed

        self.previous_time = current

    # ==========================================
    # Update Sensors
    # ==========================================

    def update_sensors(self):

        self.sensors.update(

            self.robot.x,

            self.robot.y,

            self.obstacle.get()

        )

    # ==========================================
    # Update Battery
    # ==========================================

    def update_battery(self):

        moving = (

            self.robot.direction != "STOP"

        )

        self.battery.update(

            robot_moving=moving

        )

    # ==========================================
    # Read Camera Frame
    # ==========================================

    def get_frame(self):

        success, frame = self.camera.read()

        if not success:

            return None

        frame = cv2.resize(

            frame,

            (WIDTH, HEIGHT)

        )

        return frame
          # ==========================================
    # Process One Simulation Frame
    # ==========================================

    def process_frame(self):

        """
        Capture one frame and process it.
        """

        frame = self.get_frame()

        if frame is None:

            return None

        # Detect faces
        faces = self.detector.detect(frame)

        # AI decision
        decision = self.detector.decide_direction(
            faces,
            WIDTH
        )

        # Move robot
        self.robot.update(
            decision,
            WIDTH,
            HEIGHT
        )

        # Update sensors
        self.update_sensors()

        # Collision check
        if self.obstacle.collision(
            self.robot.x,
            self.robot.y
        ):

            self.robot.stop()

            decision = "OBSTACLE"

        # Update battery
        self.update_battery()

        # Low battery protection
        if self.battery.is_low():

            self.robot.return_home()

            decision = "RETURN HOME"

        # Draw detected faces
        frame = self.detector.draw(
            frame,
            faces
        )

        # Draw obstacles
        frame = self.obstacle.update(
            frame,
            self.robot.x,
            self.robot.y
        )

        # Draw robot
        cv2.circle(
            frame,
            (self.robot.x, self.robot.y),
            15,
            (255, 0, 0),
            -1
        )

        # Calculate FPS
        self.calculate_fps()

        # Draw dashboard
        frame = self.dashboard.draw(
            frame,
            self.robot,
            self.battery,
            faces,
            self.obstacle,
            self.sensors,
            self.fps,
            decision,
            len(faces) > 0
        )

        return frame

    # ==========================================
    # Main Simulation Loop
    # ==========================================

    def run(self):

        """
        Start the simulator.
        """

        self.initialize()

        while self.running:

            frame = self.process_frame()

            if frame is None:

                break

            cv2.imshow(
                "AI VisionBot",
                frame
            )

            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):

                self.running = False

            elif key == ord("r"):

                self.robot.return_home()

            elif key == ord("c"):

                self.battery.full_charge()

            elif key == ord("o"):

                self.obstacle.regenerate(
                    WIDTH,
                    HEIGHT,
                    5
                )

        self.shutdown()
          # ==========================================
    # Reset Simulator
    # ==========================================

    def reset(self):
        """
        Reset simulator to initial state.
        """

        self.robot.return_home()

        self.robot.clear_path()

        self.robot.initialize_path()

        self.battery.reset()

        self.sensors.reset()

        self.sensors.clear_history()

        self.obstacle.regenerate(
            WIDTH,
            HEIGHT,
            number=5
        )

        self.fps = 0

        print("Simulator Reset Complete.")

    # ==========================================
    # Simulator Summary
    # ==========================================

    def summary(self):

        return {

            "Robot Position":
                (self.robot.x, self.robot.y),

            "Robot Status":
                self.robot.status,

            "Battery":
                self.battery.percentage(),

            "Battery Status":
                self.battery.battery_status(),

            "Obstacles":
                self.obstacle.count(),

            "Sensor Warning":
                self.sensors.warning(),

            "FPS":
                round(self.fps, 2)

        }

    # ==========================================
    # Print Summary
    # ==========================================

    def print_summary(self):

        summary = self.summary()

        print("=" * 50)

        print("AI VisionBot Simulator Summary")

        print("=" * 50)

        for key, value in summary.items():

            print(f"{key:<18}: {value}")

        print("=" * 50)

    # ==========================================
    # Save Statistics
    # ==========================================

    def save_statistics(
        self,
        filename="simulation_report.txt"
    ):

        summary = self.summary()

        with open(filename, "w") as file:

            file.write(
                "AI VisionBot Simulation Report\n"
            )

            file.write("=" * 40 + "\n")

            for key, value in summary.items():

                file.write(
                    f"{key}: {value}\n"
                )

        print(
            f"Statistics saved to {filename}"
        )

    # ==========================================
    # Shutdown Simulator
    # ==========================================

    def shutdown(self):

        """
        Release all resources.
        """

        self.camera.release()

        cv2.destroyAllWindows()

        self.print_summary()

        print("\nSimulator Closed Successfully.")

    # ==========================================
    # Self Test
    # ==========================================

    def test(self):

        """
        Test simulator components.
        """

        print("Testing Simulator...\n")

        self.initialize()

        self.update_sensors()

        self.update_battery()

        self.print_summary()

        self.shutdown()

        print("\nSimulator Test Completed.")
      
