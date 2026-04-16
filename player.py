class Player:

    def __init__(self):
        self.location = [0, 0]  # X, Y coordinates
        self.inventory = []
        self.radiation_dose = 0.0  # in mSv
        self.current_room = "Control Room"

    def move(self, direction, world_map):
        current_data = world_map[self.current_room]

        if direction in current_data:
            new_room_name = current_data[direction]
            new_room_data = world_map[new_room_name]

            # CHECK: Does the player have the required item to enter?
            requirement = new_room_data.get('required_item')
            if requirement and requirement not in self.inventory:
                print(f"\n[ACCESS DENIED] You need a {requirement} to enter {new_room_name}!")
                return

            # Proceed with movement
            self.current_room = new_room_name

            # Map Logic: Update Coordinates (X, Y)
            if direction == 'North': self.location[1] += 1
            elif direction == 'South': self.location[1] -= 1
            elif direction == 'East': self.location[0] += 1
            elif direction == 'West': self.location[0] -= 1

            # Applied Radiation Logic
            room_rad = new_room_data['rad']
            if "Lead Shield" in self.inventory:
                room_rad /= 2

            self.radiation_dose += room_rad

            print(f"\n--- {self.current_room} ---")
            print(new_room_data['description'])
            print(f"Radiation Dose: {self.radiation_dose:.2f} mSv")
        else:
            print("\n[!] You can't go that way.")

    def pickup_item(self, world_map):
                """TASK: The Pickup Logic"""
                item = world_map[self.current_room].get('item')
                if item:
                    self.inventory.append(item)
                    world_map[self.current_room]['item'] = None  # Remove from room
                    print(f"Retrieved: {item}")
                else:
                    print("No useful technical components found here.")
