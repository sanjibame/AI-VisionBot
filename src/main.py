"""
=========================================================
AI VisionBot

main.py

Main Entry Point

Author : Your Name
Version : 1.0
=========================================================
"""

import sys

from src.simulator import RobotSimulator


# ==========================================
# Project Banner
# ==========================================

def banner():

    print("=" * 60)

    print("            AI VisionBot")

    print("   Face Following Robot Simulator")

    print("=" * 60)

    print("Version : 1.0")

    print("Language: Python")

    print("Libraries: OpenCV, NumPy")

    print("=" * 60)

    print()

    print("Keyboard Controls")

    print("-------------------------------")

    print("Q  -> Quit")

    print("R  -> Reset Robot")

    print("C  -> Charge Battery")

    print("O  -> Generate Obstacles")

    print()


# ==========================================
# Main Function
# ==========================================

def main():

    banner()

    simulator = RobotSimulator()

    try:

        simulator.run()

    except KeyboardInterrupt:

        print("\nKeyboard Interrupt Detected.")

        simulator.shutdown()

    except Exception as error:

        print("\nUnexpected Error")

        print(error)

        simulator.shutdown()

        sys.exit(1)


# ==========================================
# Program Starts Here
# ==========================================

if __name__ == "__main__":

    main()
  
