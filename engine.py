import time

class Reactor:
    """Simulates the physical state of the nuclear core."""
    def __init__(self, level=1):
        self.temp = 573.15      #Kelvin
        self.pressure = 15.5   #MPa
        self.meltdown_point = 2500.0
        self.level = level
        self.is_active = True # The kill switch for the thread

    def core_loop(self):
        """Background thread that increases heat over time."""
        while self.is_active:
            self.temp += (0.5 * self.level)  # Constant heat rise
            self.pressure = self.temp * 0.027  # Simple PV=nRT relationship

            if self.temp > self.meltdown_point:
                print("\n[CRITICAL] MELTDOWN OCCURRED! CONTAINMENT BREACH!")
                self.is_active = False
            time.sleep(2)

    def emergency_shutdown(self):
        """Manually flips the kills switch """
        self.is_active = False
        print("\n[SYSTEM] Emergency shutdown initiated! Controls rods deployed.")

