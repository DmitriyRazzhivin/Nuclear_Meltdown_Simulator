class Player:
    def __init__(self):
        self.location = [0, 0]  # [X, Y] Coordinate plane mapping
        self.inventory = []
        self.radiation_dose = 0.0  # in mSv
        self.current_room = "Control Room"

    def move(self, direction, world):
        current_data = world.get_room_data(self.current_room)

        if direction in current_data:
            new_room_name = current_data[direction]
            new_room_data = world.get_room_data(new_room_name)

            # Check access restrictions
            requirement = new_room_data.get('required_item')
            if requirement and requirement not in self.inventory:
                print(f"\n[ACCESS DENIED] Sealed Bulkhead. Requires: {requirement} to enter {new_room_name}!")
                return False

            # Complete step execution
            self.current_room = new_room_name
            self.location = list(world.get_coordinates(self.current_room))

            # Calculate exposure using Inverse Square Law physics
            has_shield = "Lead Shield" in self.inventory
            exposure_dose = world.calculate_radiation_exposure(self.current_room, has_shield)
            self.radiation_dose += exposure_dose
            return True
        else:
            print("\n[!] Path obstructed by structural containment.")
            return False

    def pickup_item(self, world):
        room_data = world.get_room_data(self.current_room)
        item = room_data.get('item')
        if item:
            self.inventory.append(item)
            room_data['item'] = None  # Mutate data.json state in runtime memory
            print(f"\n[SUCCESS] Retrieved: {item}")
        else:
            print("\n[!] No scrap or technical components detected here.")