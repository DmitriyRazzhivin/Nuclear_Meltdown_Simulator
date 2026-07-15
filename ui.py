import os


class SCADAInterface:
    """A terminal-based SCADA HMI dashboard for the reactor facility."""

    @staticmethod
    def clear_screen():
        # Cross-platform terminal clear
        os.system('cls' if os.name == 'nt' else 'clear')

    def render(self, player, reactor, world):
        self.clear_screen()
        room_data = world.get_room_data(player.current_room)

        # Calculate real-time dynamic rad exposure for this room
        current_exposure_rate = world.calculate_radiation_exposure(
            player.current_room,
            has_shield="Lead Shield" in player.inventory
        )

        print("=" * 60)
        print("         AETHER-7 OUTPOST: SYSTEM RELIABILITY MONITOR          ")
        print("=" * 60)

        # REACTOR CORE CRITICAL STATUS (REAL-TIME ENGINE)
        status_alert = "NORMAL"
        if reactor.temp > 1500.0:
            status_alert = "CRITICAL LIMIT"
        elif reactor.temp > 1000.0:
            status_alert = "WARNING: THERMAL ACCUMULATION"

        print(f" [REACTOR STATE]   Status: {status_alert}")
        print(f"                   Core Temp: {reactor.temp:.2f} K")
        print(f"                   Core Pressure: {reactor.pressure:.2f} MPa")
        print("-" * 60)

        # PLAYER STATUS PANEL
        print(f" [OPERATOR DOSSIER] Current Location: {player.current_room} {player.location}")
        print(f"                    Accumulated Dose: {player.radiation_dose:.3f} mSv")
        print(f"                    Current Exposure Rate: {current_exposure_rate:.3f} mSv/sec")
        print(f"                    Inventory: {', '.join(player.inventory) if player.inventory else 'Empty'}")
        print("-" * 60)

        # ENVIRONMENT BRIEFING
        print(f" [LOCATION DESCRIPTION]")
        print(f" {room_data['description']}")
        if room_data.get('item'):
            print(f" >>> [ALERT] Detached Technical Component Detected: {room_data['item']}")
        print("=" * 60)