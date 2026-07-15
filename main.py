import threading
import time
from engine import Reactor
from player import Player
from world import World
from ui import SCADAInterface

if __name__ == "__main__":
    # Initialize OOP architecture
    world = World("data.json")
    reactor = Reactor(level=1)
    player = Player()
    gui = SCADAInterface()

    # Start multi-threaded core thermal model
    physics_thread = threading.Thread(target=reactor.core_loop, daemon=True)
    physics_thread.start()

    # Initial screen draw
    gui.render(player, reactor, world)

    while reactor.is_active:
        action = input("\nSCADA-Command (North/South/East/West, Pickup, Look, Stop): ").strip().title()

        if action in ["North", "South", "East", "West"]:
            player.move(action, world)
        elif action == "Pickup":
            player.pickup_item(world)
        elif action == "Look":
            pass  # The GUI render naturally updates descriptions
        elif action == "Stop":
            if "Boron Rod" in player.inventory:
                print("\n" + "=" * 50)
                print("[SUCCESS] Manual SCRAM Successful! Core stabilized!")
                print("=" * 50)
                reactor.emergency_shutdown()
            else:
                print("\n" + "=" * 50)
                print("[FATAL] Emergency SCRAM aborted! Insufficient coolant medium (Boron Rod).")
                print("=" * 50)
                reactor.is_active = False
            break

        # Guard clause: If thread killed reactor while waiting for input
        if not reactor.is_active:
            break

        # Redraw terminal screen
        time.sleep(0.1)  # Small sleep buffer to allow user feedback messages to be read
        gui.render(player, reactor, world)

    print(f"\nSimulation Terminated. Final Operator Dosimetry: {player.radiation_dose:.3f} mSv")