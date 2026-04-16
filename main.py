import threading
import json
from engine import Reactor
from player import Player

def load_data():
    with open("data.json", 'r') as file:
        return json.load(file)

if __name__ == "__main__":
    # 1. Create the objects
    world_map = load_data()
    my_reactor = Reactor(level=1)
    my_player = Player()

    # 2. Start the Physics Thread (The reactor starts heating up!)
    # daemon=True means the thread closes automatically when you quit the game
    physics_thread = threading.Thread(target=my_reactor.core_loop, daemon=True)
    physics_thread.start()

    print("--- NUCLEAR CORE SIMULATOR STARTING ---")
    #print("Commands: North, South, East, West, Status, Quit")

    # 3. The Main Game Loop
    while my_reactor.is_active:
        print(f"\nLocation: {my_player.current_room}")
        action = input("Command (North/South/East/West, Pickup, Status, Look, Stop): ").strip().capitalize()

        if action == "Look":
            # Shows the room description again
            print(f"\n{world_map[my_player.current_room]['description']}")
            if world_map[my_player.current_room]['item']:
                print(f"You see a {world_map[my_player.current_room]['item']} here.")

        elif action == "Stop":
            # The WIN CONDITION
            if "Boron Rod" in my_player.inventory:
                print("\n[SUCCESS] You inserted the Boron Rod and stabilized the core!")
                my_reactor.emergency_shutdown()
                print("YOU SAVED THE FACILITY.")
            else:
                print("\n[FAILURE] You shut down the console, but the core is still critical!")
                my_reactor.is_active = False  # Reactor melts down anyway
            break

    print("\nGame Over. Final Radiation Dose:", my_player.radiation_dose)