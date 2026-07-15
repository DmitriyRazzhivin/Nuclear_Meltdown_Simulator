import json
import math


class World:
    """Manages the physical coordinate grid and spatial radiation calculations."""

    def __init__(self, data_path="data.json"):
        with open(data_path, 'r') as file:
            self.rooms = json.load(file)

        # Hardcode layout coordinates for Inverse Square Law calculations
        self.coordinates = {
            "Control Room": (0, 0),
            "Turbine Hall": (0, 1),
            "Maintenance Closet": (-1, 1),
            "Reactor Core": (1, 1),  # The radiation source!
            "Cooling Pump Station": (1, 2)
        }
        self.source_room = "Reactor Core"

    def get_room_data(self, room_name):
        return self.rooms.get(room_name)

    def get_coordinates(self, room_name):
        return self.coordinates.get(room_name, (0, 0))

    def calculate_radiation_exposure(self, current_room, has_shield=False):
        """
        Calculates dosage using a simplified Inverse Square Law based on distance
        from the Reactor Core.
        Formula: Dose = Source_Intensity / (Distance^2)
        """
        if current_room == self.source_room:
            # Inside the core, radiation is maxed out
            base_rad = self.rooms[self.source_room]['rad']
        else:
            x1, y1 = self.get_coordinates(current_room)
            x2, y2 = self.get_coordinates(self.source_room)

            # Calculate Euclidean distance
            distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

            # Prevent DivisionByZero and apply inverse square logic
            if distance == 0:
                distance = 0.5

                # Core radiation scales down exponentially over distance
            core_rad_source = self.rooms[self.source_room]['rad']
            base_rad = core_rad_source / (distance ** 2)

        # Apply protective equipment multiplier
        if has_shield:
            base_rad *= 0.1  # Lead Shield cuts dose by 90% (industrial standard)

        return round(base_rad, 3)