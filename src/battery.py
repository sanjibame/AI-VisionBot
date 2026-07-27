"""
=========================================================
AI VisionBot

battery.py

Battery Management Module

Author : Your Name
Version : 1.0
=========================================================
"""

from src.config import *


class Battery:

    """
    Battery Simulation Class
    """

    def __init__(self):

        self.level = BATTERY_MAX

        self.maximum = BATTERY_MAX

        self.minimum = BATTERY_MIN

        self.drain_rate = BATTERY_DRAIN

        self.charge_rate = BATTERY_CHARGE_RATE

        self.low_level = LOW_BATTERY_LEVEL

        self.status = "FULL"

    # ==========================================
    # Battery Percentage
    # ==========================================

    def percentage(self):

        return round(self.level, 1)

    # ==========================================
    # Battery Status
    # ==========================================

    def battery_status(self):

        if self.level >= 80:

            self.status = "FULL"

        elif self.level >= 50:

            self.status = "GOOD"

        elif self.level >= 20:

            self.status = "LOW"

        else:

            self.status = "CRITICAL"

        return self.status

    # ==========================================
    # Drain Battery
    # ==========================================

    def drain(self, amount=None):

        if amount is None:

            amount = self.drain_rate

        self.level -= amount

        if self.level < self.minimum:

            self.level = self.minimum

        self.battery_status()

    # ==========================================
    # Charge Battery
    # ==========================================

    def charge(self, amount=None):

        if amount is None:

            amount = self.charge_rate

        self.level += amount

        if self.level > self.maximum:

            self.level = self.maximum

        self.battery_status()

    # ==========================================
    # Full Charge
    # ==========================================

    def full_charge(self):

        self.level = self.maximum

        self.status = "FULL"

    # ==========================================
    # Empty Battery
    # ==========================================

    def empty(self):

        self.level = self.minimum

        self.status = "CRITICAL"

    # ==========================================
    # Is Low Battery
    # ==========================================

    def is_low(self):

        return self.level <= self.low_level

    # ==========================================
    # Is Empty
    # ==========================================

    def is_empty(self):

        return self.level <= self.minimum
          # ==========================================
    # Start Charging
    # ==========================================

    def start_charging(self):

        """
        Put battery into charging mode.
        """

        self.status = "CHARGING"

    # ==========================================
    # Stop Charging
    # ==========================================

    def stop_charging(self):

        """
        Stop charging.
        """

        self.battery_status()

    # ==========================================
    # Charge Until Full
    # ==========================================

    def charge_full(self):

        """
        Charge battery to 100%.
        """

        while self.level < self.maximum:

            self.charge()

        self.level = self.maximum

        self.status = "FULL"

    # ==========================================
    # Battery Health
    # ==========================================

    def health(self):

        """
        Estimate battery health.
        """

        if self.level >= 80:

            return "Excellent"

        elif self.level >= 60:

            return "Good"

        elif self.level >= 40:

            return "Fair"

        elif self.level >= 20:

            return "Poor"

        else:

            return "Critical"

    # ==========================================
    # Estimated Runtime
    # ==========================================

    def runtime(self):

        """
        Estimate remaining operating time.
        """

        if self.drain_rate == 0:

            return float("inf")

        return round(

            self.level / self.drain_rate,

            1

        )

    # ==========================================
    # Battery Information
    # ==========================================

    def info(self):

        """
        Return battery information.
        """

        return {

            "Level": round(self.level, 1),

            "Status": self.battery_status(),

            "Health": self.health(),

            "Runtime": self.runtime()

        }

    # ==========================================
    # Print Battery Information
    # ==========================================

    def print_info(self):

        info = self.info()

        print("=" * 40)

        print("BATTERY INFORMATION")

        print("=" * 40)

        for key, value in info.items():

            print(f"{key:<10}: {value}")

        print("=" * 40)

    # ==========================================
    # Update Battery
    # ==========================================

    def update(

        self,

        robot_moving=True

    ):

        """
        Update battery every frame.
        """

        if robot_moving:

            self.drain()

        self.battery_status()

    # ==========================================
    # Battery Warning
    # ==========================================

    def warning(self):

        """
        Return warning message.
        """

        if self.level <= self.low_level:

            return "LOW BATTERY"

        return "OK"
          # ==========================================
    # Reset Battery
    # ==========================================

    def reset(self):

        """
        Reset battery to factory state.
        """

        self.level = self.maximum

        self.status = "FULL"

        self.cycles = 0

        self.total_drain = 0

        self.total_charge = 0

        self.history = []

    # ==========================================
    # Record Battery History
    # ==========================================

    def record(self):

        """
        Save current battery level.
        """

        if not hasattr(self, "history"):

            self.history = []

        self.history.append(

            round(self.level, 1)

        )

    # ==========================================
    # Total Battery Drain
    # ==========================================

    def add_drain(self, amount):

        if not hasattr(self, "total_drain"):

            self.total_drain = 0

        self.total_drain += amount

    # ==========================================
    # Total Battery Charge
    # ==========================================

    def add_charge(self, amount):

        if not hasattr(self, "total_charge"):

            self.total_charge = 0

        self.total_charge += amount

    # ==========================================
    # Charging Cycle
    # ==========================================

    def add_cycle(self):

        if not hasattr(self, "cycles"):

            self.cycles = 0

        self.cycles += 1

    # ==========================================
    # Battery Statistics
    # ==========================================

    def statistics(self):

        return {

            "Level": round(self.level, 1),

            "Status": self.status,

            "Health": self.health(),

            "Charge Cycles":

                getattr(self, "cycles", 0),

            "Total Drain":

                getattr(self, "total_drain", 0),

            "Total Charge":

                getattr(self, "total_charge", 0),

            "History Samples":

                len(

                    getattr(

                        self,

                        "history",

                        []

                    )

                )

        }

    # ==========================================
    # Print Statistics
    # ==========================================

    def print_statistics(self):

        stats = self.statistics()

        print("=" * 45)

        print("BATTERY STATISTICS")

        print("=" * 45)

        for key, value in stats.items():

            print(f"{key:<18}: {value}")

        print("=" * 45)

    # ==========================================
    # Summary
    # ==========================================

    def summary(self):

        return {

            "Battery (%)":

                round(self.level, 1),

            "Status":

                self.status,

            "Health":

                self.health(),

            "Runtime":

                self.runtime(),

            "Warning":

                self.warning()

        }

    # ==========================================
    # Print Summary
    # ==========================================

    def print_summary(self):

        summary = self.summary()

        print("=" * 45)

        print("AI VisionBot Battery Summary")

        print("=" * 45)

        for key, value in summary.items():

            print(f"{key:<15}: {value}")

        print("=" * 45)

    # ==========================================
    # Self Test
    # ==========================================

    def test(self):

        print("Testing Battery Module...\n")

        self.reset()

        self.drain(10)

        self.record()

        self.charge(5)

        self.record()

        self.add_cycle()

        self.print_statistics()

        print("\nBattery Test Completed.")
      
