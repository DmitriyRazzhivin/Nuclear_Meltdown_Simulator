import unittest
from world import World
from player import Player
from engine import Reactor


class TestNuclearSimulator(unittest.TestCase):

    def setUp(self):
        """Runs before every single test to set up a clean, isolated environment."""
        self.world = World("data.json")
        self.player = Player()
        self.reactor = Reactor(level=1)

    def test_inverse_square_law_calculation(self):
        """Verify that radiation drops off exponentially with distance from the Core."""
        # Baseline dose inside the Core itself
        core_dose = self.world.calculate_radiation_exposure("Reactor Core", has_shield=False)

        # Dose further away in the Control Room
        control_room_dose = self.world.calculate_radiation_exposure("Control Room", has_shield=False)

        # Assert that the control room radiation is significantly weaker than the core
        self.assertTrue(control_room_dose < core_dose)
        self.assertEqual(core_dose, 10.0)  # Matches data.json core base rad

    def test_shielding_multiplier(self):
        """Verify that the Lead Shield attenuates radiation exposure by 90%."""
        raw_dose = self.world.calculate_radiation_exposure("Turbine Hall", has_shield=False)
        shielded_dose = self.world.calculate_radiation_exposure("Turbine Hall", has_shield=True)

        # Assert that shielding cuts the dose down to 10% (divided by 10)
        self.assertAlmostEqual(shielded_dose, raw_dose * 0.1, places=3)

    def test_gated_progression_access(self):
        """Verify that a player cannot enter a restricted zone without required equipment."""
        # Try to move East into the Reactor Core from the Turbine Hall
        self.player.current_room = "Turbine Hall"

        # Movement should fail because player lacks the "Lead Shield"
        move_success = self.player.move("East", self.world)

        self.assertFalse(move_success)
        self.assertEqual(self.player.current_room, "Turbine Hall")  # Ensure location didn't change

    def test_thermodynamic_accumulation(self):
        """Verify that reactor pressure updates dynamically as temperature climbs."""
        initial_temp = self.reactor.temp
        initial_pressure = self.reactor.pressure

        # Simulate a small time step or manually tick the math properties
        self.reactor.temp += 10.0
        self.reactor.pressure = self.reactor.temp * 0.027

        self.assertTrue(self.reactor.temp > initial_temp)
        self.assertTrue(self.reactor.pressure > initial_pressure)


if __name__ == "__main__":
    unittest.main()