import time
import threading


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


class player:

        def __init__(self):
            self.location = (0, 0) # X, Y coordinates
            self.inventory = []
            self.radiation_dose = 0.0 # in mSv
            self.current_room = "Control Room"

            def move(self, direction, world_map):
                if direction in world_map[self.current_room]:
                    self.current_room = world_map[self.current_room][direction]

                    # Map Logic: Update Coordinates
                    if direction == 'North':
                        self.location[1] += 1
                    elif direction == 'South':
                        self.location[1] -= 1
                    elif direction == 'East':
                        self.location[0] += 1
                    elif direction == 'West':
                        self.location[0] -= 1

                    # Applied Radiation Logic
                    room_rad = world_map[self.current_room]['rad']
                    self.radiation_dose += room_rad

                    print(f"Moved to {self.current_room}. Total Dose: {self.radiation_dose:.2f} mSv")
                else:
                    print("Path blocked! Choose another direction.")

        world_map = {
            'Control Room': {'North': 'Turbine Hall', 'rad': 0.05, 'item': None},
            'Turbine Hall': {'South': 'Control Room', 'East': 'Reactor Core', 'rad': 1.5, 'item': 'Lead Shield'},
            'Reactor Core': {'West': 'Turbine Hall', 'rad': 10.0, 'item': 'Boron Rod'}
        }