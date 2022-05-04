import unittest
from testfile import *


class CheckRideTestOne(unittest.TestCase):
    def test_parks(self):
        stateParks = [{"state":"Texas", "park":"Guadalupe", "cost": 12.50},
              {"state":"Michigan", "park":"Sterling", "cost": 8.50},
              {"state":"Texas", "park":"Pedernales", "cost": 13.50},
              {"state":"Texas", "park":"Blanco", "cost": 15.00},
              {"state":"Georgia", "park":"Macon", "cost": 13.50},
              {"state":"California", "park":"Compton", "cost": 16.50},
              {"state":"texas", "park":"Hill Country", "cost": 10.50},
              {"state":"texas", "park":"Lost Maples", "cost": 8.00}]

        parkSet = {"Guadalupe", "Pedernales", "Hill Country", "Lost Maples"}
        self.assertEqual(parkSet, find_parks(stateParks, "Texas"))

    def test_bad_parks(self):
        stateParks = [{"state":"Texas", "park":"Guadalupe", "cost": 12.50},
              {"state":"Michigan", "park":"Sterling", "cost": 8.50},
              {"state":"Texas", "park":"Pedernales", "cost": 13.50},
              {"state":"Texas", "park":"Blanco", "cost": 15.00},
              {"state":"Georgia", "park":"Macon", "cost": 13.50},
              {"state":"California", "park":"Compton", "cost": 16.50},
              {"state":"texas", "park":"Hill Country", "cost": 10.50},
              {"state":"texas", "park":"Lost Maples", "cost": 8.00}]
        self.assertEqual("INVALID_DATA", find_parks(stateParks, ""))
        self.assertEqual("INVALID_DATA", find_parks(None, "Texas"))
        self.assertEqual("INVALID_DATA", find_parks(stateParks, None))

        stateParks = [{"state":"Texas", "park":"Guadalupe", "cost": 12.50},
              {"state":"Michigan", "park":"Sterling", "cost": 8.50},
              {"stat":"Texas", "park":"Pedernales", "cost": 13.50}]

        self.assertEqual("KEY_ERROR", find_parks(stateParks, "Texas"))

        stateParks = []
        self.assertEqual("INVALID_DATA", find_parks(stateParks, "Texas"))        

        stateParks = [{"state":"Texas", "park":"Guadalupe", "cost": 15.00},
              {"state":"Michigan", "park":"Sterling", "cost": 8.50},
              {"state":"Tekas", "park":"Pedernales", "cost": 13.50}]
        temp = set()
        self.assertEqual(temp, find_parks(stateParks, "Georgia"))
        self.assertEqual(temp, find_parks(stateParks, "Texas"))

        stateParks = [{"state":"Texas", "park":"Guadalupe", "cost": 12.50},
              {"state":"Michigan", "park":"Sterling", "cost": 7.50},
              {"state":"Texas", "park":"Pedernales", "cost": 13.50}]

        self.assertEqual("INVALID_DATA", find_parks(stateParks, "Texas"))


if __name__ == '__main__':
    unittest.main()
