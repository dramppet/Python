from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(22.5, 55.5)

    def test_default_class_atr(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)
    def test_correct_init(self):
        self.assertEqual(22.5, self.vehicle.fuel)
        self.assertEqual(self.vehicle.fuel, self.vehicle.capacity)
        self.assertEqual(55.5, self.vehicle.horse_power)
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_raise(self):
        self.vehicle.fuel = 0
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)
        self.assertEqual("Not enough fuel",str(ex.exception))




if __name__ == "__main__":
    main()
