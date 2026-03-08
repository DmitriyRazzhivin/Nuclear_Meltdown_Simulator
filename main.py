
class Reactor:
    def __init__(self, level=1):
        self.temp = 500.0       #celcius
        self.pressure = 101.3   #kPa (Normal atmospheric)
        self.meltdown_point = 2500.0
        self.level = level

    def update_physics(self):
        #
        self.temp += (1.5 * self.level)

        if self.temp > self.meltdown_point:
            return True      #Meltdown triggered
        else:
            return False

    class player:
        def __init__(self):
            self.inventory = []
            self.radiation_dose = 0.0 # in mSv
            self.current_room = "Control Room"

    def move(self, new_room, room_rad):
        self.current_room = new_room
        self.radiation_dose += room_rad

world_map = {
            'Control Room': {'North': 'Turbine Hall', 'rad': 0.05, 'item': None},
            'Turbine Hall': {'South': 'Control Room', 'East': 'Reactor Core', 'rad': 1.5, 'item': 'Lead Shield'},
            'Reactor Core': {'West': 'Turbine Hall', 'rad': 10.0, 'item': 'Boron Rod'}
        }