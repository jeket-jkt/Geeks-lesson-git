from database import create_table
from fleet_manager import FleetManager
from car import Car
from motocycle import Motocycle

create_table()

fm = FleetManager()

car1 = Car("Toyota", "Camry", 2020, 5)
bike1 = Motocycle("Yamaha", "R3", 2019, False)

fm.add_vehicle(car1)
fm.add_vehicle(bike1)

fm.list_vehicles()
fm.find_vehicle("Toyota")
fm.update_vehicle("Toyota", "Corolla")
fm.remove_vehicle("Yamaha")

fm.list_vehicles()